# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Gerona, Xyver James D.  **Date:** October 18, 2026

Each test was run on a fresh start of `python device_monitor.py`, so every test begins with the initial list `[28, 31, 35, 37, 29]`.

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Showed Reading 1 to Reading 5: 28, 31, 35, 37, 29 °C | Pass |
| TC02 | Choose 2, enter 33 | "Reading added successfully." | Showed "Reading added successfully." | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Showed "Invalid input. Enter a whole number only." Viewing the list afterward still showed 5 readings. | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | Showed "Invalid reading. Enter a value from 0 to 100." List still had 5 readings. | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | Showed "Invalid reading. Enter a value from 0 to 100." List still had 5 readings. | Pass |
| TC06 | Choose 2, add 30, then choose 3 | 30 °C -> WARNING | Reading added; classification showed "30 °C -> WARNING" | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | Showed "35 °C -> WARNING" | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Showed Total 160, Average 32.00 °C, Min 28 °C, Max 37 °C, NORMAL 2 (40.00%), WARNING 2 (40.00%), CRITICAL 1 (20.00%), Overall Status: ATTENTION REQUIRED | Pass |
| TC09 | Enter 9 at the menu | Error message; menu shown again | Showed "Invalid choice. Please enter a number from 1 to 5." and the menu appeared again | Pass |
| TC10 | Choose 5 | Exit message; program ends | Showed "Thank you for using the Device Monitoring System." and the program ended normally | Pass |

**Result: 10 tests, 10 passed, 0 failed.**

## Bugs Found and Fixed

- No test failed in the final run, so there was no bug to report from these results. **If you find and fix a bug when you test on your own computer, replace this line with what went wrong and how you fixed it.**
- The test that needed the most care was TC04 (-5). The text `-5` is a valid whole number, so it must pass the format check first and then be rejected by the range check. That is why `is_whole_number()` allows a minus sign at the front and `add_reading()` checks the range after the format.
