# Student Management API

## Description

This is a RESTful API for managing student records, featuring secure user authentication and CRUD operations. It allows for the registration, login, and management of student data through a secure and efficient interface.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) system for Python.
- **SQLite**: A self-contained, serverless, zero-configuration SQL database engine.
- **JWT (JSON Web Tokens)**: Used for secure user authentication.
- **OAuth2**: An authorization framework that allows third-party services to exchange user data without exposing passwords.

## Features

- User registration and authentication
- CRUD operations for managing student records
- Secure password hashing and token-based authentication

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Incognitol07/student-management-api
   ```

2. Navigate to the project directory:

    ```bash
    cd student-management-api
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Usage Instructions
Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

6. Access the API: Open your browser or a tool like Postman and navigate to <http://127.0.0.1:8000/>.

7. API Endpoints
   User Registration: POST /auth/register \
   User Login: POST /auth/login \
   Create Student: POST /students/create-student \
   Get Student: GET /students/get-student \
   Get All Students: GET /students/get-students \
   Update Student: PUT /students/update-student/{student_id} \
   Delete Student: DELETE /students/delete-student/{student_id} \

## License

This project is licensed under the MIT License.
