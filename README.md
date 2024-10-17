# Portfolio Project

This is a portfolio project built using Django Rest Framework for the backend, PostgreSQL as the database, Next.js for the frontend, and Material UI for the design components.

## Project Overview

The project aims to showcase my skills in building a full-stack application with a focus on backend API development using Django Rest Framework (DRF), handling data with PostgreSQL, and creating a modern, responsive user interface using Next.js and Material UI.

### Technologies Used:

- **Backend**: Django Rest Framework (Python)
- **Database**: PostgreSQL
- **Frontend**: Next.js (React framework), Material UI (React component library)

## Features

### Backend (Completed)
- Django Rest Framework used to create APIs for portfolio-related data (projects, blogs, contact information, etc.)
- PostgreSQL integrated for persistent data storage
- Token-based authentication using Django's `djoser` for user management (login, registration)
- Secure API endpoints for CRUD operations
- Deployed locally with instructions for replication

### Frontend (In Progress)
- Next.js planned to handle routing and page rendering
- Material UI planned for consistent design components and responsive layout
- Dynamic pages to showcase portfolio items, blogs, and contact forms

## Installation & Setup

### Backend Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/portfolio-project.git
   cd portfolio-project
   ## Installation & Setup

### Backend Setup

Install backend dependencies:

```bash
pip install -r requirements.txt
```
### Set up PostgreSQL database:

# Make sure you have PostgreSQL installed
```bash
createdb portfolio_db
```
### Configure your environment variables for database connection and Django settings:
```bash
DATABASE_NAME=portfolio_db
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
```

### Run migrations and start the backend server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### FRONTEND(YAAR KAISE KARU BOHT CONFUSING LAG RHA HAI)
