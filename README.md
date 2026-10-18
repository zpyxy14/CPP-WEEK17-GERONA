Simulated Device Monitoring and Alert System

Student Name: Gerona, Xyver James D.

Student Number: 2601295

Section: 1CPE-B

Project Description

This program monitors simulated device temperature readings for a Computer Engineering laboratory. It stores a list of readings, accepts new valid readings, and classifies each reading as NORMAL, WARNING, or CRITICAL. It also prints a numerical summary and an overall monitoring status. It was written for CPP102 Week 17 using only the concepts learned in the course.

Features

- View all stored temperature readings with their position numbers
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading (below 30 = NORMAL, 30 to 35 = WARNING, above 35 = CRITICAL)
- Generate a numerical summary: count, total, average, minimum, maximum, category counts and percentages, and overall status
- Reject invalid menu choices and invalid readings (empty, non-numeric, decimal, negative, above 100) without crashing
- Total, minimum, and maximum are computed with loops (no `sum()`, `min()`, or `max()`)

Requirements

- Python 3
- A terminal or code editor, Visual Studio Code

How to Run

1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py`
   (On macOS or Linux, type: `python3 device_monitor.py`)

Sample Output

```
MONITORING SUMMARY
------------------
Number of readings  : 6
Total of readings   : 193
Average temperature : 32.17 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (33.33%)
WARNING  : 3 (50.00%)
CRITICAL : 1 (16.67%)

Overall Status: ATTENTION REQUIRED
```
This output appeared after adding the reading 33 to the initial list.

Test Cases

I performed 10 tests. 10 passed and 0 failed. Full details are in [test_cases.md](test_cases.md).

Known Limitations

- Readings are lost when the program closes (file handling is not allowed in this project).
- Readings can only be added. They cannot be edited or deleted.
- The limits (30, 35, 0, and 100) are for this classroom simulation only. They are not real device-safety standards.

Reflection

I learned how to combine functions, lists, loops, and if statements in one complete program. One important lesson was that invalid values must be checked before they are added to the list, so the readings stay correct. Testing the boundary values of 30 °C and 35 °C helped me understand how conditional statements work, because both values must be classified as WARNING. The most challenging part of this project was combining the menu, input validation, classification rules, and summary calculations into one working program, and I used loops to calculate the total, minimum, and maximum instead of built-in functions. In the future, I would like to add a feature that saves the readings so the data is still available after the program closes.
