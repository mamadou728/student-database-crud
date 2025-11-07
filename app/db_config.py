import os
from dotenv import load_dotenv

# Database configuration
DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'postgresql://postgres:NewPassword123@localhost:5432/student_db'
)

