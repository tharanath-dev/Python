# ============================================================
#   STUDENT RECORD SYSTEM
#   Micro-Project | First Year Python
#   Team: Tharanath, Dev Siddharth, Rachanasri,
#         Tarun, Ankupalli Anish, Nadiya Tasneem
# ============================================================

# We use a list to store all student records.
# Each record is a dictionary (like a form with fields).
students = []


# ────────────────────────────────────────────────────────────
# FUNCTION 1 – Add a new student
# ────────────────────────────────────────────────────────────
def add_student():
    print("\n--- Add New Student ---")

    roll   = input("Enter Roll Number : ").strip()
    name   = input("Enter Name        : ").strip()
    dept   = input("Enter Department  : ").strip()
    phone  = input("Enter Phone Number: ").strip()

    # Collect previous year CGPA
    while True:
        cgpa_input = input("Enter Previous Year CGPA (0.0 to 10.0): ").strip()
        try:
            cgpa = float(cgpa_input)
            if 0.0 <= cgpa <= 10.0:
                break
            else:
                print("  Please enter a value between 0.0 and 10.0")
        except ValueError:
            print("  Invalid input! Please enter a number like 7.5")

    # Build the student record as a dictionary
    record = {
        "roll"    : roll,
        "name"    : name,
        "dept"    : dept,
        "phone"   : phone,
        "cgpa"    : cgpa
    }

    students.append(record)               # add to our list
    print(f"\n Student '{name}' added successfully!")


# ────────────────────────────────────────────────────────────
# FUNCTION 2 – Display one student's details nicely
# ────────────────────────────────────────────────────────────
def display_student(record):
    print("\n" + "=" * 40)
    print(f"  Roll Number : {record['roll']}")
    print(f"  Name        : {record['name']}")
    print(f"  Department  : {record['dept']}")
    print(f"  Phone       : {record['phone']}")
    print(f"  CGPA (Prev Year): {record['cgpa']}")
    print("=" * 40)


# ────────────────────────────────────────────────────────────
# FUNCTION 3 – Search for a student
# ────────────────────────────────────────────────────────────
def search_student():
    print("\n--- Search Student ---")
    print("Search by:  1. Roll Number   2. Name")
    choice = input("Your choice (1/2): ").strip()

    found = []   # list to collect matches

    if choice == "1":
        roll = input("Enter Roll Number: ").strip()
        for s in students:
            if s["roll"] == roll:
                found.append(s)

    elif choice == "2":
        name = input("Enter Name (or part of it): ").strip().lower()
        for s in students:
            if name in s["name"].lower():   # partial match, case-insensitive
                found.append(s)

    else:
        print("Invalid choice!")
        return

    # Show results
    if found:
        print(f"\n{len(found)} record(s) found:")
        for record in found:
            display_student(record)
    else:
        print("\n No student found with that information.")


# ────────────────────────────────────────────────────────────
# FUNCTION 4 – Update a student's record
# ────────────────────────────────────────────────────────────
def update_student():
    print("\n--- Update Student Record ---")
    roll = input("Enter Roll Number of student to update: ").strip()

    # Find the student
    target = None
    for s in students:
        if s["roll"] == roll:
            target = s
            break

    if target is None:
        print("\n Student not found.")
        return

    print(f"\nUpdating record for: {target['name']}")
    print("What do you want to update?")
    print("  1. Name")
    print("  2. Phone Number")
    print("  3. Department")
    print("  4. Previous Year CGPA")

    choice = input("Your choice (1/2/3/4): ").strip()

    if choice == "1":
        target["name"]  = input("New Name : ").strip()
        print(" Name updated!")

    elif choice == "2":
        target["phone"] = input("New Phone Number: ").strip()
        print(" Phone updated!")

    elif choice == "3":
        target["dept"]  = input("New Department  : ").strip()
        print(" Department updated!")

    elif choice == "4":
        while True:
            cgpa_input = input("New CGPA (0.0 to 10.0): ").strip()
            try:
                cgpa = float(cgpa_input)
                if 0.0 <= cgpa <= 10.0:
                    target["cgpa"] = cgpa
                    print(" CGPA updated!")
                    break
                else:
                    print("  Please enter a value between 0.0 and 10.0")
            except ValueError:
                print("  Invalid input! Please enter a number like 7.5")

    else:
        print("Invalid choice!")


# ────────────────────────────────────────────────────────────
# FUNCTION 5 – Show all students
# ────────────────────────────────────────────────────────────
def show_all():
    print("\n--- All Student Records ---")
    if not students:
        print("No records added yet.")
        return
    print(f"Total students: {len(students)}")
    for record in students:
        display_student(record)


# ────────────────────────────────────────────────────────────
# FUNCTION 6 – Delete a student record
# ────────────────────────────────────────────────────────────
def delete_student():
    print("\n--- Delete Student Record ---")
    roll = input("Enter Roll Number to delete: ").strip()

    for i, s in enumerate(students):
        if s["roll"] == roll:
            confirm = input(f"Are you sure you want to delete '{s['name']}'? (yes/no): ")
            if confirm.lower() == "yes":
                students.pop(i)
                print(" Record deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("\n Student not found.")


# ────────────────────────────────────────────────────────────
# MAIN MENU – This is where the program starts
# ────────────────────────────────────────────────────────────
def main():
    print("\n" + "*" * 45)
    print("*          STUDENT RECORD SYSTEM            *")
    print("*          Micro-Project | Python           *")
    print("*" * 45)

    while True:   # keep showing menu until user exits
        print("\n======= MAIN MENU =======")
        print("  1. Add Student")
        print("  2. Search Student")
        print("  3. Update Student")
        print("  4. Show All Students")
        print("  5. Delete Student")
        print("  6. Exit")
        print("=========================")

        choice = input("Choose an option (1-6): ").strip()

        if   choice == "1": add_student()
        elif choice == "2": search_student()
        elif choice == "3": update_student()
        elif choice == "4": show_all()
        elif choice == "5": delete_student()
        elif choice == "6":
            print("\nThank you! Goodbye!\n")
            break
        else:
            print("Please enter a number between 1 and 6.")


# Run the program
main()