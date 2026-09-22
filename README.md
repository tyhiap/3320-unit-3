# 3320-unit-3

### Problem 1: Incrementing Counter with While Loop
* **File:** `u3problem1.py`
* **Task:** Print numbers 1 to 9 using a `while` loop that counts up, tracking variable mutation stages.

#### Execution Trace Chart

| Iteration Number | Value of x | Condition (`x <= 9`) | True or False | Value of x at the end of loop |
| :---: | :---: | :---: | :---: | :---: |
| 1st | 1 | `1 <= 9` | True | 2 |
| 2nd | 2 | `2 <= 9` | True | 3 |
| 3rd | 3 | `3 <= 9` | True | 4 |
| 4th | 4 | `4 <= 9` | True | 5 |
| 5th | 5 | `5 <= 9` | True | 6 |
| 6th | 6 | `6 <= 9` | True | 7 |
| 7th | 7 | `7 <= 9` | True | 8 |
| 8th | 8 | `8 <= 9` | True | 9 |
| 9th | 9 | `9 <= 9` | True | 10 |
| 10th | 10 | `10 <= 9` | False | *Loop Terminates* |

* **Final value of x after loop termination:** `10`

---

### Problem 3: Multi-Input Average Processor
* **File:** `u3problem3.py`
* **Task:** Gather 5 numeric entries dynamically and evaluate the mathematical mean.

#### Execution Trace Chart (Sample Run Input: 10, 20, 30, 40, 50)

| Iteration Number | Value of x | Condition (`x <= 5`) | True or False | Value of x at the end of loop | Value of total at the end of loop |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1st | 1 | `1 <= 5` | True | 2 | 10.0 |
| 2nd | 2 | `2 <= 5` | True | 3 | 30.0 |
| 3rd | 3 | `3 <= 5` | True | 4 | 60.0 |
| 4th | 4 | `4 <= 5` | True | 5 | 100.0 |
| 5th | 5 | `5 <= 5` | True | 6 | 150.0 |
| 6th | 6 | `6 <= 5` | False | *Terminates* | 150.0 |

---

### Problem 4: Decrementing Counter with While Loop
* **File:** `u3problem4.py`
* **Task:** Countdown execution sequence from 10 to 5.

#### Execution Trace Chart

| Iteration Number | Value of x | Condition (`x >= 5`) | True or False | Value of x at the end of loop |
| :---: | :---: | :---: | :---: | :---: |
| 1st | 10 | `10 >= 5` | True | 9 |
| 2nd | 9 | `9 >= 5` | True | 8 |
| 3rd | 8 | `8 >= 5` | True | 7 |
| 4th | 7 | `7 >= 5` | True | 6 |
| 5th | 6 | `6 >= 5` | True | 5 |
| 6th | 5 | `5 >= 5` | True | 4 |
| 7th | 4 | `4 >= 5` | False | *Loop Terminates* |

* **Final value of x after loop termination:** `4`

---
