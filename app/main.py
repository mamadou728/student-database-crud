# main.py — minimal CRUD demo
import psycopg
from psycopg.rows import dict_row
from datetime import date
from db_config import DATABASE_URL


def get_connection():
    """Get a connection to the database."""
    return psycopg.connect(DATABASE_URL, autocommit=True)

# ---------- CRUD ----------
def get_all_students():
   
    """Retrieve the list of students from the database."""
   
    # Connect to the database and create a cursor that returns rows as dictionaries.
    with get_connection() as conn, conn.cursor(row_factory=dict_row) as cur:
   
        # Execute a SQL query to fetch all student records
        cur.execute("""
            SELECT student_id, first_name, last_name, email, enrollment_date
            FROM students
            ORDER BY student_id
        """)
   
        # Retrieve all the rows from the executed query
        return cur.fetchall()



def add_student(first_name, last_name, email, enrollment_date):
   
    """Add a new student to the database."""
   
    # Connect to the database and create a cursor that returns rows as dictionaries.
    with get_connection() as conn, conn.cursor(row_factory=dict_row) as cur:
   
        # Execute a SQL query to check if the student already exists.
        cur.execute("SELECT 1 FROM students WHERE email = %s", (email,))
        if cur.fetchone():
   
            # If the student exists, print a message and return None.
            print(f"Student with email {email} already exists.")
            return None

        # Execute a SQL query to insert the new student.
        cur.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s)
            RETURNING student_id, first_name, last_name, email, enrollment_date
        """, (first_name, last_name, email, enrollment_date))
   
        # Retrieve the newly created student record.
        return cur.fetchone()

def update_student_email(student_id, new_email):
    """Update a student's email by their ID."""
   
    # Connect to the database and create a cursor that returns rows as dictionaries.
    with get_connection() as conn, conn.cursor(row_factory=dict_row) as cur:
   
        # Execute a SQL query to update the student's email.
        cur.execute("""
            UPDATE students
               SET email = %s
             WHERE student_id = %s
         RETURNING student_id, first_name, last_name, email, enrollment_date
        """, (new_email, student_id))
      
        # Retrieve the updated student record.
        return cur.fetchone()  

def delete_student(student_id):
    """Delete a student by their ID."""
  
    # Connect to the database and create a cursor.
    with get_connection() as conn, conn.cursor() as cur:
  
        # Execute a SQL query to delete the student by ID.
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
      
        # Return True if a row was deleted, False otherwise.
        return cur.rowcount > 0


def main():
   
    # Define the interactive menu for the user.
    menu = (
        "\n--- Student Database ---\
"
        "1. Add Nathalie\n"
        "2. Update Email (by ID)\n"
        "3. Delete (by ID)\n"
        "4. View All Students\n"
        "5. Exit\n"
        "Choose: "
    )
    
    nathalie = {
        "first_name": "Nathalie",
        "last_name": "Umuhoza",
        "email": "nathalie.umuhoza@example.com",
        "enrollment_date": date.today().isoformat(),
    }

    # Start the main application loop.
    while True:
        choice = input(menu).strip()

        # Handle the user's choice.
        if choice == "1":
            created = add_student(**nathalie)
            print("Added:", created or "no change (duplicate email)")

        elif choice == "2":
            print("\n--- UPDATE EMAIL BY ID ---")
            try:
                student_id = int(input("Enter student ID: "))
                new_email = input("Enter new email: ").strip()
                updated = update_student_email(student_id, new_email)
                if updated:
                    print("Updated:", updated)
                else:
                    print("No student found with that ID.")
            except ValueError:
                print("Invalid ID format. Please enter a number.")

        elif choice == "3":
            print("\n--- DELETE BY ID ---")
            try:
                student_id = int(input("Enter student ID to delete: "))
                if delete_student(student_id):
                    print(f"Student with ID {student_id} deleted successfully.")
                else:
                    print(f"No student found with ID {student_id}.")
            except ValueError:
                print("Invalid ID format. Please enter a number.")

        elif choice == "4":
            rows = get_all_students()
            if not rows:
                print("(no students)")
            else:
                for s in rows:
                    print(s)

        # Exit the loop if the user chooses to quit.
        elif choice == "5":
            print("Bye.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
