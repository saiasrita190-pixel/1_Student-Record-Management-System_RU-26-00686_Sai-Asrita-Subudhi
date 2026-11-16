# Student Record Management System
# Menu aligned with Test Cases 1, 2, 3, and 4

student_dict = {}
roll_list = []


def add_record(roll_no, name, course, marks):
  """Add a new student record with unique roll number and valid marks."""
  if roll_no in student_dict:
    print(f"(a) Roll number {roll_no} already exists.")
    return

  if not (0 <= marks <= 100):
    print("Marks must be between 0 and 100.")
    return

  student_dict[roll_no] = (name, course, marks)
  roll_list.append(roll_no)
  print(f"Record added: {roll_no} | {name} | {course} | {marks}")


def search_record(roll_no):
  """Search for a student record by roll number."""
  if roll_no in student_dict:
    name, course, marks = student_dict[roll_no]
    print(f"(a) {roll_no} | {name} | {course} | {marks}")
  else:
    print(f"Roll number {roll_no} not found.")


def update_record(roll_no, new_marks):
  """Update the marks of an existing student record."""
  if roll_no not in student_dict:
    print(f"Roll number {roll_no} not found.")
    return

  if not (0 <= new_marks <= 100):
    print("Marks must be between 0 and 100.")
    return

  name, course, _ = student_dict[roll_no]
  student_dict[roll_no] = (name, course, new_marks)
  print(f"(b) Marks updated: {new_marks}")


def delete_record(roll_no):
  """Delete a student record by roll number."""
  if roll_no not in student_dict:
    print(f"(c) Roll number {roll_no} not found.")
    return

  del student_dict[roll_no]
  roll_list.remove(roll_no)
  print(f"Record deleted for roll number {roll_no}.")


def main():
  while True:
    print("\n--- Student Record Management System ---")
    print("1. Test Case 1: Normal Input (Add Record)")
    print("2. Test Case 2: Boundary / Minimum Input (Add Max/Min Marks)")
    print("3. Test Case 3: Invalid Input (Duplicate / Out of Range Marks)")
    print("4. Test Case 4: Different Valid Scenario (Search, Update, Delete)")
    print("5. View All Records")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
      print("\n--- Running Test Case 1: Normal Input ---")
      # Example matching test case: 101, Aman, BTech, 78
      try:
        roll = int(input("Enter Roll No (e.g. 101): "))
        name = input("Enter Name (e.g. Aman): ")
        course = input("Enter Course (e.g. BTech): ")
        marks = float(input("Enter Marks (e.g. 78): "))
        add_record(roll, name, course, marks)
      except ValueError:
        print("Invalid input!")

    elif choice == "2":
      print("\n--- Running Test Case 2: Boundary / Minimum Input ---")
      # Example matching test case: 102, Riya, BTech, 100
      try:
        roll = int(input("Enter Roll No (e.g. 102): "))
        name = input("Enter Name (e.g. Riya): ")
        course = input("Enter Course (e.g. BTech): ")
        marks = float(
            input("Enter Marks [Boundary limit 0 to 100] (e.g. 100): ")
        )
        add_record(roll, name, course, marks)
      except ValueError:
        print("Invalid input!")

    elif choice == "3":
      print("\n--- Running Test Case 3: Invalid Input ---")
      print("Sub-options:")
      print("(a) Test duplicate roll number")
      print("(b) Test marks out of range (> 100 or < 0)")
      sub = input("Choose sub-option (a/b): ")

      if sub == "a":
        try:
          roll = int(
              input("Enter an existing Roll No to test duplicate (e.g. 101): ")
          )
          add_record(roll, "Neha", "BTech", 70)
        except ValueError:
          print("Invalid input!")
      elif sub == "b":
        try:
          roll = int(input("Enter Roll No: "))
          name = input("Enter Name: ")
          course = input("Enter Course: ")
          marks = float(
              input("Enter invalid marks (e.g. 150 or -5): ")
          )  # e.g., 150
          if not (0 <= marks <= 100):
            print("(b) Marks must be between 0 and 100.")
          else:
            add_record(roll, name, course, marks)
        except ValueError:
          print("Invalid input!")

    elif choice == "4":
      print("\n--- Running Test Case 4: Different Valid Scenario ---")
      print("(a) Search record")
      print("(b) Update marks")
      print("(c) Delete non-existent record")
      sub = input("Choose sub-option (a/b/c): ")

      if sub == "a":
        try:
          roll = int(input("Enter Roll No to search (e.g. 101): "))
          search_record(roll)
        except ValueError:
          print("Invalid input!")
      elif sub == "b":
        try:
          roll = int(input("Enter Roll No to update marks (e.g. 101): "))
          new_marks = float(input("Enter new marks (e.g. 85): "))
          update_record(roll, new_marks)
        except ValueError:
          print("Invalid input!")
      elif sub == "c":
        try:
          roll = int(
              input("Enter non-existent Roll No to delete (e.g. 999): ")
          )
          delete_record(roll)
        except ValueError:
          print("Invalid input!")

    elif choice == "5":
      print("\n--- All Records ---")
      if not student_dict:
        print("No records found.")
      else:
        print("-" * 50)
        print(f"{'Roll No':<10} | {'Name':<15} | {'Course':<10} | {'Marks':<5}")
        print("-" * 50)
        for roll in roll_list:
          name, course, marks = student_dict[roll]
          print(f"{roll:<10} | {name:<15} | {course:<10} | {marks:<5}")
        print("-" * 50)

    elif choice == "6":
      print("Exiting program.")
      break
    else:
      print("Invalid choice! Choose between 1 and 6.")

if __name__ == "__main__":
  main()