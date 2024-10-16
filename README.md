# Student Management System 🏫
# Student Management System 🏫

This project is a **command-line application** to manage student records using **Python** and **MySQL**. It allows users to **add, view, update, and delete student records** easily via a simple interactive menu.

## 🚀 Features

- **Add Student**: Insert new student records with fields such as first name, last name, age, gender, and major.
- **View Students**: Retrieve and display all student records stored in the database.
- **Update Student**: Modify the details of a specific student using their ID.
- **Delete Student**: Remove a student’s record from the database.
- **Simple CLI Menu**: Interactive and user-friendly command-line interface.

## 🛠️ Technologies Used

- **Python** (for backend logic)
- **MySQL** (for database storage)

## 📋 Prerequisites

Make sure you have the following installed:

- **Python 3.x**
- **MySQL** server
- **mysql-connector-python** library  
  Install it via:
  ```bash
  pip install mysql-connector-python
  ```

## ⚙️ Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. **Install the dependencies**:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up the MySQL database**:

   - Create a new MySQL database:
     ```sql
     CREATE DATABASE student_management;
     ```
   - Switch to the newly created database:
     ```sql
     USE student_management;
     ```
   - Create the `students` table:
     ```sql
     CREATE TABLE students (
         id INT AUTO_INCREMENT PRIMARY KEY,
         first_name VARCHAR(50),
         last_name VARCHAR(50),
         age INT,
         gender VARCHAR(10),
         major VARCHAR(100)
     );
     ```

4. **Update the database connection details** in `main.py`:
   ```python
   return mysql.connector.connect(
       host="localhost",
       user="your_username",
       password="your_password",
       database="student_management"
   )
   ```

## 🚀 Usage

1. **Run the program**:
   ```bash
   python main.py
   ```

2. **Follow the menu prompts** to:
   - Add a student
   - View students
   - Update student details
   - Delete a student
   - Exit the program

## 🧑‍💻 Example

```bash
Student Management System
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 1

Enter first name: John
Enter last name: Doe
Enter age: 20
Enter gender: Male
Enter major: Computer Science
Student added successfully!
```

## 🤝 Contributing

Feel free to open issues or submit pull requests if you want to improve this project!
