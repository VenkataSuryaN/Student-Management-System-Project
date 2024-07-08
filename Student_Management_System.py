import mysql.connector

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="student_management"
    )

# Add a new student
def add_student(first_name, last_name, age, gender, major):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, gender, major)
        VALUES (%s, %s, %s, %s, %s)
    """, (first_name, last_name, age, gender, major))
    conn.commit()
    cursor.close()
    conn.close()
    print("Student added successfully!")

# View all students
def view_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# Update student details
def update_student(student_id, first_name, last_name, age, gender, major):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET first_name = %s, last_name = %s, age = %s, gender = %s, major = %s
        WHERE id = %s
    """, (first_name, last_name, age, gender, major, student_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Student updated successfully!")

# Delete a student record
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Student deleted successfully!")

# Main program loop
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            major = input("Enter major: ")
            add_student(first_name, last_name, age, gender, major)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            age = int(input("Enter new age: "))
            gender = input("Enter new gender: ")
            major = input("Enter new major: ")
            update_student(student_id, first_name, last_name, age, gender, major)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
