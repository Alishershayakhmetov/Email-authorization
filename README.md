# Email-authorization

A Django project with email-based authentication. This project implements both front-end and back-end solutions, including several HTML files for various features.

## Table of Contents

- [Features](#features)
- [Installation](#installation)

## Features

- User authentication with email verification.
- website implemented with multiple HTML templates.
- User-friendly forms and validation.

## Installation

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. install the dependences:
   ```
   pip install django decouple
   ```

3. create .ven file in the project root and set variables

   ```
   SECRET_KEY=
   DEBUG=
   DATABASE_NAME=
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=
   DATABASE_PORT=
   
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   ```

4. set up a database
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. run the server on http://127.0.0.1:8000/
   ```
   python manage.py runserver
   ```
