import sqlite3

DB_NAME = "students.db"


def init_db() -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            major TEXT NOT NULL,
            gpa REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def add_student(name: str, major: str, gpa: float) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, major, gpa) VALUES (?, ?, ?)",
        (name, major, gpa),
    )
    conn.commit()
    conn.close()


def view_students() -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    print("\nStudent Records:")
    for row in rows:
        print(row)


def search_student(name: str) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))
    rows = cursor.fetchall()
    conn.close()

    print("\nSearch Results:")
    for row in rows:
        print(row)


def update_student(student_id: int, major: str, gpa: float) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET major = ?, gpa = ? WHERE id = ?",
        (major, gpa, student_id),
    )
    conn.commit()
    conn.close()


def delete_student(student_id: int) -> None:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()


def main() -> None:
    init_db()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            major = input("Major: ").strip()
            gpa = float(input("GPA: ").strip())
            add_student(name, major, gpa)
            print("Student added successfully.")

        elif choice == "2":
            view_students()

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            search_student(name)

        elif choice == "4":
            student_id = int(input("Student ID: ").strip())
            major = input("New major: ").strip()
            gpa = float(input("New GPA: ").strip())
            update_student(student_id, major, gpa)
            print("Student updated successfully.")

        elif choice == "5":
            student_id = int(input("Student ID to delete: ").strip())
            delete_student(student_id)
            print("Student deleted successfully.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()