"""Command-line interface for Grade Book."""
from grades import add_grade, average, letter


def main():
    book = {}
    while True:
        print("\n1) Add grade  2) Show average  3) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            student = input("Student name: ").strip()
            grade = input("Grade (0-100): ")
            try:
                add_grade(book, student, grade)
            except ValueError as error:
                print(f"Not saved: {error}")
            else:
                print("Saved.")
        elif choice == "2":
            student = input("Student name: ").strip()
            avg = average(book, student)
            print(f"{student}: {avg:.1f} ({letter(avg)})")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
