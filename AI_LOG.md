# AI Usage Log
## EGN 321 — Module 1

> AI is prohibited during the initial manual workbook inspection for Assignment 1.1.

## Interaction 1
- **Tool:**CHAT GPT
- **Date:**09/05/2026
- **Prompt:**We have some errors,one error is the cell e13 in tank fill because it should be showing the 30 inches , becasuse it has to be pull from the field notes. and in the fieldnotes it was wrong at first only showing 2.5 ft but we converted it to inches right so now it  has to show 30 in and the third error was in the sum because it should be sum (g6:g23)Also, in the Field Notes sheet, Run R-108 has a fill depth entered as 2.5 ft while all the other measurements in that column are in inches. I believe this should be 30 inches.
Second, that same value was copied into the Tank Fill sheet as 2.5, even though that column is supposed to be in inches. Because it was not converted from feet to inches, the calculated volume for R-108 is much lower than it should be.
Third, the TOTAL RECORDED VOLUME formula in G25 only adds G6, but the data continues through row 23. This means runs R-113 through R-118 are left out of the total.
I also checked a few other things. The workbook uses two different tank sizes but does not have a Tank ID column. I checked whether the fill depths could be cumulative readings, but the values drop from 30 inches to 26 inches between R-108 and R-109, so they appear to be separate fill runs. I also checked for hidden rows, columns, sheets, comments, formatting issues, and inconsistent formulas, but I did not find any other major defects.
Based on these findings, write the sections "Additional Suspected Defects," "Overall Assessment," and "What Should Become a Python Test?" for my college assignment. Explain the findings clearly and include Python test ideas for checking units between Field Notes and Tank Fill, checking the volume formula in each row, and checking that the total formula includes every populated run. attachh DEFECTS TEMPLATE
- **What the tool returned:** my DEFECTS FILE
- **What I used:** THE FILE         
- **What I changed:**WORDING
- **Why I changed it:**IT WAS CONFUSING FOR SOME PEOPLE 
- **How I verified it:**I GAVE IT TO MY GIRLFRIEND TO READ AND SHE UNDERSTOOD
