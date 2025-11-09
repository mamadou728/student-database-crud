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
