# Student Database CRUD

A simple PostgreSQL CRUD application that manages student records. Includes database setup scripts and an application demonstrating Create, Read, Update, and Delete operations through direct interaction with the PostgreSQL database.

## Setup and Run Instructions

### 1. Database Setup

- **Prerequisites:** Make sure you have PostgreSQL installed and running.
- **Create Database:** Create a new PostgreSQL database. For example, `students_db`.
- **Run Script:** Execute the `db/setup.sql` script to create the `students` table and insert the initial data. You can do this using `psql` or a GUI tool like pgAdmin:

  ```sh
  psql -U postgres -h localhost -d student_db -f db/setup.sql
  ```

### 2. Application Setup

- **Clone Repository:**

  ```sh
  git clone <your-repo-url>
  cd student-database-crud
  ```

- **Install Dependencies:**

  ```sh
  pip install -r requirements.txt
  ```

- **Configure Database Connection:**

  Open `app/db_config.py` and update the `DATABASE_URL` with your PostgreSQL connection string.

### 3. Run the Application

  ```sh
  python app/main.py
  ```

## Demonstration Video

[Link to your demonstration video here]

## Project Overview

This project demonstrates how to use Python and PostgreSQL together for database operations. It allows adding, viewing, updating, and deleting student records through a simple console interface.

## Requirements

* Python 3.13.2
* PostgreSQL 17
* psycopg[binary]==3.2.12

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the python script
python main.py
```

## Project Structure

```
student-database-crud/
├─ app/
│  ├─ db_config.py      # Database configuration file
│  └─ main.py           # Main app file containing CRUD operations
├─ db/
│  └─ setup.sql         # SQL script for database setup and initial data
├─ README.md            # Documentation file
└─ requirements.txt     # Python dependencies
```

## File Descriptions

### `app/db_config.py`

Here is the database URL that we have locally:

```python
postgresql://postgres:NewPassword123@localhost:5432/student_db
```

### `db/setup.sql`

Defines the database schema and initial data:

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

Contains the core CRUD functions:

* **get_all_students()** — Lists all students
* **add_student()** — Adds a new record
* **update_student_email()** — Updates a student's email using their ID
* **delete_student()** — Deletes a student record

It also includes an interactive menu to test each operation.

## Database Setup

1. Create a database:

   ```bash
   createdb -U postgres -h localhost student_db
   ```
2. Run the setup script:

   ```bash
   psql -U postgres -h localhost -d student_db -f db/setup.sql
   ```
3. Run the code:

   ```bash
   python app/main.py
   ```

Example output:

```
--- Student Database ---
1. Add Nathalie
2. Update Email (by ID)
3. Delete Nathalie
4. View All Students
5. Exit
Choose: 1
Added: {'student_id': 4, 'first_name': 'Nathalie', 'last_name': 'Umuhoza', 'email': 'nathalie.umuhoza@example.com', 'enrollment_date': '2025-11-07'}
```

## Testing CRUD Operations

Retrieve the list of students directly from the database.

```sql
SELECT * FROM students ORDER BY student_id;
```

## Author

**Mamadou Kabore**
COMP 3005B — November 2025
