# secure_login_system

1️⃣ Project Overview
🔹 Project Name:

Secure Authentication System
🔹 Description:

This is a Flask-based authentication system with user registration, login, JWT authentication, role-based access control, and reCAPTCHA verification. It also includes CORS for frontend integration and bcrypt for password hashing.
🔹 Features:

✅ User Registration & Login with Role-Based Access
✅ JWT Authentication for Secure API Requests
✅ reCAPTCHA Verification to Prevent Bots
✅ API Key Permissions & Rate Limiting
✅ Secure Password Hashing with Bcrypt
✅ Admin Panel for User Management
2️⃣ Setup Instructions
🔹 Prerequisites:

Before running the project, ensure you have:

    Python 3.x installed
    Flask and required dependencies

🔹 Installation Steps:
1. Clone the Repository

git clone https://github.com/yourusername/yourproject.git
cd yourproject

2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Environment Variables

Create a .env file and add:

SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///users.db
RECAPTCHA_PRIVATE_KEY=your_private_key

5. Run Database Migrations

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

6. Start the Flask App

python app.py

The app will run at: http://127.0.0.1:5000/
3️⃣ API Endpoints
🔹 Authentication Routes
Endpoint	Method	Description
/register	POST	Register a new user
/login	POST	User login with JWT authentication
/profile	GET	Get user profile (Requires JWT)
/logout	POST	Logout the user
4️⃣ Screenshots of the System

Include screenshots of:

    Registration Page
    Login Page
    Admin Dashboard
    Postman API Testing

5️⃣ Challenges Faced & Solutions
🔹 Challenge 1: Implementing reCAPTCHA Verification

Issue: The API was rejecting reCAPTCHA requests.
Solution: Used Flask requests to verify reCAPTCHA with Google’s API.
🔹 Challenge 2: Storing Passwords Securely

Issue: Plaintext passwords were a security risk.
Solution: Implemented bcrypt for password hashing.
🔹 Challenge 3: Handling CORS Issues in Frontend

Issue: The frontend was unable to make requests due to CORS restrictions.
Solution: Enabled Flask-CORS to allow cross-origin requests.
