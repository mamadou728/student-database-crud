````markdown
# Student Database CRUD

A simple PostgreSQL CRUD application that manages student records. It includes a database setup script and a Python console app demonstrating Create, Read, Update, and Delete operations.

---

## Demo Video

https://youtu.be/LtI9y2oCBd4

---

## Requirements

- Python **3.13.2** (compatible with 3.10+)
- PostgreSQL **17**
- `psycopg[binary]==3.2.12`

---

## Quick Start

### 1) Database

1. Ensure PostgreSQL is installed and running.
2. Create the database:
   ```bash
   createdb -U postgres -h localhost student_db
````

3. Run the setup script:

   ```bash
   psql -U postgres -h localhost -d student_db -f db/setup.sql
   ```

### 2) Application

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd student-database-crud
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Configure the database URL in `app/db_config.py` (example):

   ```python
   # app/db_config.py
   DATABASE_URL = "postgresql://postgres:NewPassword123@localhost:5432/student_db"
   ```
4. Run the app:

   ```bash
   python app/main.py
   ```

---

## Project Structure

```
student-database-crud/
├─ app/
│  ├─ db_config.py      # Database configuration
│  └─ main.py           # CLI app with CRUD operations
├─ db/
│  └─ setup.sql         # Schema + seed data
├─ README.md            # You are here
└─ requirements.txt     # Python dependencies
```

---

## Files & Schema

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

Contains the core CRUD functions and a simple interactive menu:

* `get_all_students()` — list students
* `add_student()` — insert a record
* `update_student_email()` — update email by ID
* `delete_student()` — delete by ID

### `app/db_config.py`

Holds the `DATABASE_URL` connection string for PostgreSQL.

---

## Example Run

```
--- Student Database ---
1. Add Student
2. Update Email (by ID)
3. Delete Student
4. View All Students
5. Exit
Choose: 1
Added: {"student_id": 4, "first_name": "Nathalie", "last_name": "Umuhoza", "email": "nathalie.umuhoza@example.com", "enrollment_date": "2025-11-07"}
```

To verify directly in SQL:

```sql
SELECT * FROM students ORDER BY student_id;
```

---

## Author

**Mamadou Kabore**
COMP 3005B — November 2025

```
```
