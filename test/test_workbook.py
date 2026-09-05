from pathlib import Path
import sys

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from workbook_checks import (
    field_note_depth_units_are_inches,
    tank_fill_matches_field_notes,
    total_formula_includes_all_runs,
    volume_formulas_are_consistent,
)


def find_workbook(filename):
    """
    Look for the workbook in the original folder first, then in the repo root.

    This lets the tests work if both Excel files are placed in original/,
    or if the fixed copy is temporarily kept in the repository root.
    """
    locations = [
        REPO_ROOT / "original" / filename,
        REPO_ROOT / filename,
    ]

    for path in locations:
        if path.exists():
            return path

    pytest.fail(
        f"Could not find {filename}. Put it in the original/ folder "
        f"or in the repository root."
    )


@pytest.fixture(scope="module")
def original_workbook():
    return find_workbook("TANK_FILL_rev4.xlsx")


@pytest.fixture(scope="module")
def fixed_workbook():
    return find_workbook("TANK_FILL_copy.xlsx")


def test_original_workbook_defects_are_detected(original_workbook):
    """
    The original workbook should contain the three defects found in DEFECTS.md.
    This test passes when the checks successfully detect those problems.
    """
    units_ok, unit_problems = field_note_depth_units_are_inches(original_workbook)
    source_ok, source_problems = tank_fill_matches_field_notes(original_workbook)
    total_ok, total_problems = total_formula_includes_all_runs(original_workbook)

    assert not units_ok, "Defect 1 was not detected in the original workbook."
    assert any("R-108" in problem for problem in unit_problems)

    assert not source_ok, "Defect 2 was not detected in the original workbook."
    assert any("R-108" in problem for problem in source_problems)

    assert not total_ok, "Defect 3 was not detected in the original workbook."
    assert any("G25" in problem for problem in total_problems)


def test_original_volume_formulas_are_structurally_correct(original_workbook):
    """
    The original workbook's per-row volume formulas are mathematically
    consistent with the values entered in each row. The R-108 problem comes
    from the wrong depth unit/value, not from the formula in G13 itself.
    """
    passed, problems = volume_formulas_are_consistent(original_workbook)

    assert passed, "\n".join(problems)


def test_fixed_field_note_units_are_inches(fixed_workbook):
    passed, problems = field_note_depth_units_are_inches(fixed_workbook)

    assert passed, "\n".join(problems)


def test_fixed_tank_fill_matches_field_notes(fixed_workbook):
    passed, problems = tank_fill_matches_field_notes(fixed_workbook)

    assert passed, "\n".join(problems)


def test_fixed_volume_formulas_are_correct(fixed_workbook):
    passed, problems = volume_formulas_are_consistent(fixed_workbook)

    assert passed, "\n".join(problems)


def test_fixed_total_includes_every_run(fixed_workbook):
    passed, problems = total_formula_includes_all_runs(fixed_workbook)

    assert passed, "\n".join(problems)
