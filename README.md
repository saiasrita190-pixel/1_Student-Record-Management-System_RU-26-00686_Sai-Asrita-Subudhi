# Student Record Management System

A command-line Python application to maintain student records (`roll_no`, `name`, `course`, `marks`) with full CRUD (Create, Read, Update, Delete) functionality and input validation[span_1](start_span)[span_1](end_span).

## Project Details
- **PS No.:** 1[span_2](start_span)[span_2](end_span)
- **Project Title:** Student Record Management System[span_3](start_span)[span_3](end_span)
- **Language:** Python 3[span_4](start_span)[span_4](end_span)
- **Concepts Used:** Lists, Tuples, Dictionaries, CRUD Operations[span_5](start_span)[span_5](end_span)

## Features
1. **Add Record (`add_record`):** Adds a new student record stored as a tuple `(name, course, marks)` inside a dictionary mapped by unique `roll_no`, while tracking insertion order in a list[span_6](start_span)[span_6](end_span). Validates that roll numbers are unique and marks fall within `0` to `100`[span_7](start_span)[span_7](end_span).
2. **Search Record (`search_record`):** Looks up a student by roll number and displays their formatted details (`Roll No | Name | Course | Marks`).
3. **Update Record (`update_record`):** Updates the marks of an existing student record after validating the `0`–`100` range.
4. **Delete Record (`delete_record`):** Removes a student entry from both the dictionary and roll number list, or notifies if the roll number does not exist.
5. **View All Records:** Displays all stored student records in a clean, tabular console layout[span_8](start_span)[span_8](end_span).

## Test Cases Covered
| Test Case | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **Test Case 1** | Normal Input (Add) | `101`, `Aman`, `BTech`, `78`[span_9](start_span)[span_9](end_span) | `Record added: 101 \| Aman \| BTech \| 78`[span_10](start_span)[span_10](end_span) |
| **Test Case 2** | Boundary Input (Max Marks) | `102`, `Riya`, `BTech`, `100`[span_11](start_span)[span_11](end_span) | `Record added: 102 \| Riya \| BTech \| 100`[span_12](start_span)[span_12](end_span) |
| **Test Case 3 (a)** | Invalid Input (Duplicate Roll) | `101`, `Neha`, `BTech`, `70`[span_13](start_span)[span_13](end_span) | `(a) Roll number 101 already exists.`[span_14](start_span)[span_14](end_span) |
| **Test Case 3 (b)** | Invalid Input (Out-of-Range Marks) | `103`, `Ravi`, `BTech`, `150`[span_15](start_span)[span_15](end_span) | `(b) Marks must be between 0 and 100.`[span_16](start_span)[span_16](end_span) |
| **Test Case 4 (a)** | Search Record | Roll: `101`[span_17](start_span)[span_17](end_span) | `(a) 101 \| Aman \| BTech \| 78`[span_18](start_span)[span_18](end_span) |
| **Test Case 4 (b)** | Update Marks | Roll: `101`, New Marks: `85`[span_19](start_span)[span_19](end_span) | `(b) Marks updated: 85`[span_20](start_span)[span_20](end_span) |
| **Test Case 4 (c)** | Delete Non-Existent Record | Roll: `999`[span_21](start_span)[span_21](end_span) | `(c) Roll number 999 not found.`[span_22](start_span)[span_22](end_span) |

## How to Run
```bash
python3 student_record.py
