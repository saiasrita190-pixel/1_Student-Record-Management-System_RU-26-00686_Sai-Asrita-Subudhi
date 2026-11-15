# Student Record Management System

A command-line Python application to maintain student records (`roll_no`, `name`, `course`, `marks`) with full CRUD (Create, Read, Update, Delete) functionality and input validation.

## Project Details
- **PS No.:** 1
- **Project Title:** Student Record Management System
- **Language:** Python 3
- **Concepts Used:** Lists, Tuples, Dictionaries, CRUD Operations

## Features
1. **Add Record (`add_record`):** Adds a new student record stored as a tuple `(name, course, marks)` inside a dictionary mapped by unique `roll_no`, while tracking insertion order in a list. Validates that roll numbers are unique and marks fall within `0` to `100`.
2. **Search Record (`search_record`):** Looks up a student by roll number and displays their formatted details (`Roll No | Name | Course | Marks`).
3. **Update Record (`update_record`):** Updates the marks of an existing student record after validating the `0`–`100` range.
4. **Delete Record (`delete_record`):** Removes a student entry from both the dictionary and roll number list, or notifies if the roll number does not exist.
5. **View All Records:** Displays all stored student records in a clean, tabular console layout.

## Test Cases Covered
| Test Case | Scenario | Input | Expected Output |
| :--- | :--- | :--- | :--- |
| **Test Case 1** | Normal Input (Add) | `101`, `Aman`, `BTech`, `78` | `Record added: 101 \| Aman \| BTech \| 78` |
| **Test Case 2** | Boundary Input (Max Marks) | `102`, `Riya`, `BTech`, `100` | `Record added: 102 \| Riya \| BTech \| 100` |
| **Test Case 3 (a)** | Invalid Input (Duplicate Roll) | `101`, `Neha`, `BTech`, `70` | `(a) Roll number 101 already exists.` |
| **Test Case 3 (b)** | Invalid Input (Out-of-Range Marks) | `103`, `Ravi`, `BTech`, `150` | `(b) Marks must be between 0 and 100.` |
| **Test Case 4 (a)** | Search Record | Roll: `101` | `(a) 101 \| Aman \| BTech \| 78` |
| **Test Case 4 (b)** | Update Marks | Roll: `101`, New Marks: `85` | `(b) Marks updated: 85` |
| **Test Case 4 (c)** | Delete Non-Existent Record | Roll: `999` | `(c) Roll number 999 not found.` |

## How to Run
```bash
python3 student_record.py
