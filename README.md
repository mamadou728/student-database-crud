# Student Database CRUD

A simple PostgreSQL CRUD application built with Python. It demonstrates how to perform **Create, Read, Update, and Delete** operations using PostgreSQL through a lightweight console interface.

![Python + PostgreSQL](https://img.shields.io/badge/Python-3.13.2-blue?logo=python) ![PostgreSQL 17](https://img.shields.io/badge/PostgreSQL-17-blue?logo=postgresql)

---

## Demo Video

[Watch on YouTube](https://youtu.be/LtI9y2oCBd4)

---

## Requirements

* **Python** ≥ 3.10 (tested with 3.13.2)
* **PostgreSQL** ≥ 17
* **Dependencies:**

  ```bash
  psycopg[binary]==3.2.12
  ```

---

## Setup Instructions

### Database Setup

1. Make sure PostgreSQL is installed and running.
2. Create a new database:

   ```bash
   createdb -U postgres -h localhost student_db
   ```
3. Run the setup script to create and populate the table:

   ```bash
   psql -U postgres -h localhost -d student_db -f db/setup.sql
   ```

### Application Setup

1. Clone this repository:

   ```bash
   git clone <your-repo-url>
   cd student-database-crud
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Update your database credentials in `app/db_config.py`:

   ```python
   DATABASE_URL = "postgresql://postgres:NewPassword123@localhost:5432/student_db"
   ```
4. Run the app:

   ```bash
   python app/main.py
   ```

---

## Project Structure

```text
student-database-crud/
├── app/
│   ├── db_config.py      # PostgreSQL connection settings
│   └── main.py           # Core CRUD logic and CLI
├── db/
│   └── setup.sql         # Table schema + seed data
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## Core Files

### `db/setup.sql`

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    email      TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

### `app/main.py`

Implements basic CRUD operations:

* `get_all_students()` → Retrieve all records
* `add_student()` → Insert a new student
* `update_student_email()` → Modify a student’s email
* `delete_student()` → Remove a student by ID

### Example Interaction

```text
--- Student Database ---
1. Add Student
2. Update Email (by ID)
3. Delete Student
4. View All Students
5. Exit
Choose: 1
Added: {"student_id": 4, "first_name": "Nathalie", "last_name": "Umuhoza", "email": "nathalie.umuhoza@example.com", "enrollment_date": "2025-11-07"}
```

SQL check:

```sql
SELECT * FROM students ORDER BY student_id;
```

---

## Author

**Mamadou Kabore**
Carleton University — COMP 3005B
November 2025
