# EGN 321: Module 1 Defect Report

## Student Information
- **Name:** Marco Ruiz
- **Student ID:** MARUIZF52B
- **Date:** 2026-09-05

## Workbook Reviewed
- **Workbook:** `TANK_FILL_rev4.xlsx`
- **Worksheets Reviewed:** `Tank Fill`, `Field Notes`, and `Read Me`

## 1. Workbook Purpose

The purpose of this workbook is to keep track of different liquid filling runs. Each row in the `Tank Fill` sheet represents one run, identified by a Run ID from R-101 through R-118 and a date. The sheet includes the tank length and width, along with the fill depth for each run.

The `Calculated Volume (gal)` column calculates the volume in gallons using this formula:

`Volume (gal) = Length (ft) × Width (ft) × (Depth (in) / 12) × 7.48052`

The depth is divided by 12 to convert inches into feet, and 7.48052 converts cubic feet into gallons.

Cell G25, labeled `TOTAL RECORDED VOLUME`, is supposed to add the calculated volume from all of the runs.

The `Field Notes` sheet contains the original measurements that were used to enter the information into the `Tank Fill` sheet. I used this sheet to compare the data and check whether the values in `Tank Fill` matched the original records.

There are 18 runs total. Runs R-101 through R-112 use a 10 ft × 6 ft tank, while runs R-113 through R-118 use a 12 ft × 5 ft tank.

## 2. Defect Summary

| # | Location | Defect | Correct Behavior | Impact | Confidence |
|---|---|---|---|---|---|
| 1 | Field Notes!E11 (R-108) | Depth is recorded as `2.5 ft` while all other measurements are in inches | Should be `30.0 in` | This causes the next defect when the value is copied into the main sheet | High |
| 2 | Tank Fill!E13 (R-108) | The value `2.5` was entered into a column that uses inches without converting feet to inches | Should be `30` | R-108 is understated by about 1,028.6 gallons | High |
| 3 | Tank Fill!G25 | The total formula only adds G6:G17 and leaves out rows G18:G23 | Should be `=SUM(G6:G23)` | About 4,619.22 gallons are left out of the total | High |

## 3. Defect 1

### Location
- **Worksheet:** `Field Notes`
- **Cell:** E11
- **Run ID:** R-108

### Existing Value
`E11 = "2.5 ft"`

### Problem Identified

Almost every depth measurement in the `Field Notes` sheet is recorded in inches. For example, the other values include measurements such as `8.0 in`, `24.0 in`, and `32.0 in`. R-108 is the only row that uses feet instead and shows `2.5 ft`.

### Why This Is a Defect

The problem is that the column is supposed to use the same unit for every measurement. Having one measurement in feet while all the others are in inches makes it easy for someone to copy the number without noticing the different unit.

The technician note says that the handwritten field value was entered as recorded. This probably explains how the value ended up being entered in feet instead of being converted into inches first.

Since the workbook does not appear to check for different units automatically, the value was later copied into the `Tank Fill` sheet and caused a calculation problem.

### Correct Value

The value should be:

`30.0 in`

because:

`2.5 ft × 12 in/ft = 30 in`

This keeps the measurement consistent with the rest of the column.

### Impact on the Result

The `Field Notes` cell itself is only a reference value, so it does not directly calculate anything. However, it caused the incorrect value in `Tank Fill!E13`.

The number `2.5` was copied into the main worksheet without converting it from feet to inches.

### Estimated Age of the Defect

The R-108 record is dated June 16, 2026, so the defect probably started when that measurement was originally entered.

It also appears to be a one-time data-entry problem because none of the other depth values use feet.

### Verification

I reviewed all 18 depth measurements in `Field Notes`. Seventeen use inches and only R-108 uses feet. This confirmed that R-108 is the only measurement with a different unit.

## 4. Defect 2

### Location
- **Worksheet:** `Tank Fill`
- **Cell:** E13
- **Run ID:** R-108

### Existing Value

`E13 = 2.5`

Since the column is labeled `Fill Depth (in)`, Excel treats this as 2.5 inches.

### Problem Identified

The original `Field Notes` value for R-108 is `2.5 ft`, but the `Tank Fill` sheet contains only the number `2.5`.

This means the number was copied over without converting the measurement from feet into inches.

### Why This Is a Defect

The value looks normal when looking only at the worksheet because `2.5` is still a valid number. However, comparing it with the original source shows that it does not represent the same measurement.

The notes also support this explanation. The Operator Note says the value was transferred from a handwritten field log, and the Field Notes say the handwritten value was entered as recorded.

I also compared this value with the other fill depths. Most of the measurements are between 14 and 32 inches, with one other run at 8 inches. A value of only 2.5 inches would be unusually low.

After converting 2.5 feet into 30 inches, the value fits much better with the rest of the data.

I also considered whether the intended value might have been 25 inches, but there is no evidence for that. The original source specifically says `2.5 ft`, so converting feet to inches is the most supported correction.

### Correct Value

E13 should be:

`30`

because:

`2.5 ft × 12 in/ft = 30 in`

### Impact on the Result

With the incorrect value:

`10 × 6 × (2.5 / 12) × 7.48052 = 93.51 gallons`

With the corrected value:

`10 × 6 × (30 / 12) × 7.48052 = 1,122.08 gallons`

This means the volume for R-108 is understated by about:

`1,028.6 gallons`

Since this value is also part of the total volume calculation, it affects the final workbook total too.

### Estimated Age of the Defect

The R-108 entry is dated June 16, 2026, so this defect most likely started when that row was entered.

It does not appear in any other row, so it looks like a single data-entry mistake instead of a repeated formula problem.

### Verification

I compared the length, width, depth, and date of all 18 runs between `Tank Fill` and `Field Notes`.

R-108 was the only run where I found this type of problem. The number `2.5` appears in both places, but the important difference is that the original measurement is in feet while the `Tank Fill` column expects inches.

## 5. Defect 3

### Location
- **Worksheet:** `Tank Fill`
- **Cell:** G25
- **Label:** `TOTAL RECORDED VOLUME`

### Existing Formula

`=SUM(G6:G17)`

### Problem Identified

The worksheet has 18 populated runs from rows 6 through 23, but the total formula only includes rows 6 through 17.

Because of this, runs R-113 through R-118 are completely left out of the total.

These six rows contain valid dates, tank dimensions, depths, and calculated volumes, so there does not appear to be a reason for excluding them.

### Why This Is a Defect

The total should represent all the runs in the worksheet. Since the formula stops at row 17, it only includes the first 12 runs.

The remaining six runs begin on row 18 and use the second tank size of 12 ft × 5 ft.

It looks like the total formula may have originally been created when the sheet only had data through row 17 and was not updated when more runs were added.

### Correct Formula

The formula should be:

`=SUM(G6:G23)`

This would include all 18 runs.

### Impact on the Result

The current formula reports:

**8,527.79 gallons**

If the total range is corrected to G6:G23, but the R-108 depth is still left incorrect, the total becomes:

**13,147.01 gallons**

This means the six missing rows account for:

**4,619.22 gallons**

After also correcting R-108 from 2.5 inches to 30 inches, the fully corrected total becomes:

**14,175.59 gallons**

Compared with the current reported total, the workbook is understating the total by:

**5,647.79 gallons, or about 39.8%.**

That is a large difference and could create problems if the total is being used for inventory, billing, or reporting.

### Estimated Age of the Defect

The first row excluded from the formula is dated June 26, 2026.

Because the SUM formula stops exactly before that row, it is likely that the formula was not updated when the second group of tank runs was added.

### Verification

I counted the populated rows and found 18 runs from rows 6 through 23.

The formula only includes 12 rows, G6 through G17.

I also checked the six excluded rows and confirmed that they contain complete data and calculated volumes. This means there is no clear reason why they should not be part of the total.

## 6. Additional Suspected Defects

One other issue I noticed is that the workbook uses two different tank sizes but does not have a `Tank ID` column. The first twelve runs use a 10 ft × 6 ft tank, while the last six use a 12 ft × 5 ft tank.

This does not directly cause a calculation error because the correct dimensions are entered for each run. However, adding a tank identifier could make it easier to see when the workbook changes from one tank to another.

I also checked whether the fill depths might represent a continuously increasing water level instead of separate runs. After correcting R-108, the values increase to 30 inches and then drop to 26 inches for R-109. Because of this decrease, the readings appear to represent separate fill runs rather than one continuously filling tank.

Finally, I checked for hidden rows, hidden columns, hidden worksheets, comments, defined names, and conditional formatting that could contain additional information. I did not find anything else that appeared to affect the calculations.

I also checked the formulas in G6:G23. They all follow the same calculation pattern and reference the correct row.

## 7. Overall Assessment

Based on the problems I found, I would not rely on the workbook's current total without correcting it first.

The biggest issue is that the reported total is about 39.8% lower than the corrected total. The workbook still opens normally and the formulas calculate without giving an Excel error, which makes these mistakes harder to notice.

Defects 1 and 2 show how one small unit mistake in the original data can affect a later calculation. Defect 3 shows how a formula range can become outdated when new rows are added.

The good part is that the fixes are fairly simple. One source value needs to be corrected, one depth value needs to be updated, and the total formula needs to include all populated rows.

However, since these errors were not caught earlier, adding some type of validation check would help prevent similar problems in the future.

## 8. What Should Become a Python Test?

1. **Unit and value test:**  
For every Run ID that appears in both `Tank Fill` and `Field Notes`, Python could check the measurement and its unit. If the source uses feet while the worksheet expects inches, the program should convert the value before comparing them. This would help catch problems like Defects 1 and 2.

2. **Formula consistency test:**  
Python could calculate the expected volume for every row using:

`Length × Width × (Depth / 12) × 7.48052`

Then it could compare that result with the value produced by the workbook. This would help catch incorrect formulas or cell references.

3. **Total completeness test:**  
Python could check how many rows contain Run IDs and make sure the `TOTAL RECORDED VOLUME` formula includes all of those rows. This would prevent the total formula from accidentally leaving out newly added runs like it does in Defect 3.
