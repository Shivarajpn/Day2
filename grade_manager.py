"""
Student Grade Manager
Week 1, Day 2 assignment.

Storage choice:
    Students are kept in a LIST of DICTIONARIES, e.g.
        [{"id": 1, "name": "Priya", "mark": 92}, ...]
    - A list keeps the order students were added.
    - Each student gets a unique ID, so two students both called "Priya"
      are stored separately and never overwrite each other.
      (A dict keyed by name would silently replace the first Priya.)

Input handling:
    - Marks must be whole numbers from 0 to 100.
      "abc", "105", "-5", "" are rejected with a message and re-asked.
    - Names cannot be blank.
    - Menu choices other than 1/2/3 are rejected.
    - Ctrl+C or Ctrl+D quits cleanly instead of crashing.
"""


def get_grade(mark):
    """Return the letter grade for a mark (boundaries inclusive)."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def ask_name():
    """Keep asking until a non-empty name is entered."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("  Name cannot be empty. Please try again.")


def ask_mark():
    """Keep asking until a whole number between 0 and 100 is entered."""
    while True:
        text = input("Enter mark (0-100): ").strip()
        try:
            mark = int(text)
        except ValueError:
            print(f"  '{text}' is not a whole number. Please try again.")
            continue
        if 0 <= mark <= 100:
            return mark
        print(f"  {mark} is out of range. Marks must be between 0 and 100.")


def add_student(students):
    """Add one student to the list, giving them a unique ID."""
    name = ask_name()
    mark = ask_mark()

    # Warn (but still allow) when the name already exists.
    same_name = [s for s in students if s["name"].lower() == name.lower()]
    if same_name:
        print(f"  Note: {len(same_name)} student(s) named '{name}' already exist. "
              "Adding as a separate student.")

    new_id = len(students) + 1
    students.append({"id": new_id, "name": name, "mark": mark})
    print(f"  Added {name} (ID {new_id}) with mark {mark}, grade {get_grade(mark)}.")


def show_results(students):
    """Print an aligned table plus class average, highest and lowest."""
    if not students:
        print("  No students added yet. Choose option 1 to add one.")
        return

    name_width = max(len("Name"), max(len(s["name"]) for s in students))

    print()
    header = f"{'ID':<4}{'Name':<{name_width + 2}}{'Mark':>5}  {'Grade':<5}"
    print(header)
    print("-" * len(header))
    for s in students:
        print(f"{s['id']:<4}{s['name']:<{name_width + 2}}{s['mark']:>5}  {get_grade(s['mark']):<5}")
    print("-" * len(header))

    marks = [s["mark"] for s in students]
    average = sum(marks) / len(marks)
    highest = max(students, key=lambda s: s["mark"])
    lowest = min(students, key=lambda s: s["mark"])

    print(f"Class average : {average:.2f} ({get_grade(round(average))})")
    print(f"Highest mark  : {highest['mark']} ({highest['name']})")
    print(f"Lowest mark   : {lowest['mark']} ({lowest['name']})")
    print()


def main():
    students = []

    print("=== Student Grade Manager ===")
    while True:
        print("\nMenu:")
        print("  1. Add student")
        print("  2. Show results")
        print("  3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_results(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(f"  '{choice}' is not a valid option. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Goodbye!")