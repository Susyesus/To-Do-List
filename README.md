# To-Do-List

📝 Django To-Do List App

A simple To-Do List web application built with Django. Users can create an account, add tasks, mark them as complete, and manage their daily activities.

🚀 Features

User authentication (signup, login, logout)

Create, edit, delete tasks

Mark tasks as complete/incomplete

Task due dates and priority (optional)

Personal task lists (each user sees only their own tasks)

🛠 Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap (or Tailwind, if you prefer)

Database: SQLite (default, can be swapped for PostgreSQL/MySQL)

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/Susyesus/To-Do-List.git
cd django-todo-list


Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Create a superuser (admin account)

python manage.py createsuperuser


Run the server

python manage.py runserver


Visit http://127.0.0.1:8000/ in your browser.


