# Junior Developer Applicant Dashboard

This project is a Django web application designed to serve as a Job Applicant Dashboard specifically for the Junior Developer position. It allows for the management and viewing of applicant information and their portfolios through a web interface, with data managed via the Django Admin.

## Table of Contents

1.  [Requirements Fulfilled](#1-requirements-fulfilled)
2.  [Project Structure Overview](#2-project-structure-overview)
3.  [Setup and Running the Project](#3-setup-and-running-the-project)
    * [1. Clone the Repository](#1-clone-the-repository)
    * [2. Create and Activate Virtual Environment](#2-create-and-activate-virtual-environment)
    * [3. Install Required Packages](#3-install-required-packages)
    * [4. Apply Database Migrations](#4-apply-database-migrations)
    * [5. Create a Superuser (Admin Account)](#5-create-a-superuser-admin-account)
    * [6. Populate Initial Data](#6-populate-initial-data)
    * [7. Run the Development Server](#7-run-the-development-server)
    * [8. Access the Application](#8-access-the-application)
4.  [Git Commit Message Conventions](#4-git-commit-message-conventions)

---

## 1. Requirements Fulfilled

This application implements the following features as per the project requirements:

* **Core Functionality**: A web application serving as a Job Applicant Dashboard for the Junior Developer position.
* **Data Management**: All data can be created, viewed, and managed directly inside the Django Admin.
* **User Model**: Utilizes Django's built-in `User` model for basic user information.
* **Custom Models**:
    * `Portfolio`: Links a `User` to a portfolio object (One-to-One relationship).
    * `Project`: Can be assigned to a single `Portfolio` (One-to-One relationship, ensuring a `Project` is unique to a `Portfolio`).
    * **Fields**:
        * `class Project`: `project_name`, `project_description`, `created_at`, `updated_at`.
        * `class Portfolio`: `user`, `portfolio_title`, `portfolio_description`, `project`.
    * **Admin Display (`__str__`)**:
        * `Portfolio`: Displays as "User First Name - Portfolio".
        * `Project`: Displays as "project_name".
* **Dashboard Pages**:
    * Dedicated page for Listing of Applicants.
    * Dedicated page for the detailed portfolio of an applicant.
* **Static Files**: Bootstrap is hosted as a self-contained Static CDN (served locally via Django's static files system), avoiding external stylesheets for now.
* **Template Tags**: Extensive use of `{% extends %}`, `{% include %}`, `{% url %}`.

### Page Specifics:

* **Applicant List View (`/`)**:
    * Uses Bootstrap to create a table.
    * Lists applicant information: First Name, Last Name, Email, Actions (Go, Delete).
    * "Junior Developer Position Applicants" hardcoded above the table in `list.html`.
    * **"Go" CTA**: Redirects to the applicant's detail page.
    * **"Delete" CTA**: Deletes the `User` along with their associated `Portfolio` (and sets the linked `Project` to NULL) from the database. No in-browser confirmation prompt is explicitly implemented beyond Django's default deletion confirmation page.

### Views & URLs:

* **`PortfolioApp`**: A separate Django app named `PortfolioApp` handles all core applicant dashboard logic.
* **View Types**:
    * List View (`/`): Function-Based View (`applicant_list_view`).
    * Detail View (`/portfolio/<username>/`): Class-Based View (`ApplicantDetailView`).
    * Delete View (`/portfolio/<username>/delete/`): Class-Based View (`ApplicantDeleteView`).
* **URL Patterns**:
    * List View route: `/` (root route).
    * Detail View route: `/portfolio/<username>/` (utilizes user's username for lookup).
    * Delete View route: `/portfolio/<username>/delete/` (utilizes user's username for lookup).
* **URL Inclusion**: The `PortfolioApp`'s URL patterns are included in the main project's `urls.py`.

### Project Management:

* Includes a `.gitignore` file to exclude virtual environment (`.venv/`) and the SQLite database (`db.sqlite3`) from version control.

---

## 2. Project Structure Overview

Quiz2_AbellaNicholasBenedictE._CPE202/
├── .venv/                      # Python virtual environment (ignored by Git)
├── Dashboard/                  # Main Django Project Configuration
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL dispatcher (includes PortfolioApp.urls)
│   └── ... (other config files)
├── DashboardApp/               # An existing Django app (not central to applicant dashboard logic)
│   └── ...
├── PortfolioApp/               # The core application for the Job Applicant Dashboard
│   ├── migrations/             # Database migration files
│   ├── admin.py                # Admin site registration for models
│   ├── models.py               # Defines Portfolio and Project models
│   ├── urls.py                 # URL patterns for PortfolioApp
│   └── views.py                # Contains applicant_list_view (FBV), ApplicantDetailView (CBV), ApplicantDeleteView (CBV)
├── static/                     # Directory for collecting all static files (e.g., Bootstrap CSS/JS)
│   ├── css/
│   │   └── bootstrap.min.css
│   └── js/
│       └── bootstrap.bundle.min.js
├── templates/                  # Top-level directory for project-wide HTML templates
│   ├── base.html               # Base layout template extending Bootstrap
│   ├── navbar.html             # Reusable navigation bar included in base.html
│   ├── list.html               # Applicant list page template
│   ├── portfolio.html          # Applicant detail page template
│   └── portfolio_confirm_delete.html # Deletion confirmation template
├── .gitignore                  # Specifies files/directories to be ignored by Git
└── db.sqlite3                  # SQLite database file (ignored by Git)
└── manage.py                   # Django's command-line utility

---

## 3. Setup and Running the Project

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

First, clone the project from GitHub to your local machine:

```bash
git clone <YOUR_GITHUB_REPO_URL_HERE>
cd Quiz2_AbellaNicholasBenedictE._CPE202
2. Create and Activate Virtual Environment
It is highly recommended to use a virtual environment to isolate project dependencies.

Bash

python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
3. Install Required Packages
Install Django (and any other dependencies if specified in a requirements.txt).
(If you haven't created a requirements.txt yet, you can do so by running pip freeze > requirements.txt after installing Django).

Bash

pip install Django
# Or if you have a requirements.txt:
# pip install -r requirements.txt
4. Apply Database Migrations
This step creates the necessary database tables for your Portfolio and Project models, along with Django's built-in models.

Bash

python manage.py makemigrations PortfolioApp
python manage.py migrate
5. Create a Superuser (Admin Account)
This allows you to access the Django administration site (/admin) to manage users, portfolios, and projects.

Bash

python manage.py createsuperuser
Follow the prompts in the terminal to set up your username, email, and password for the admin account.

6. Populate Initial Data (Crucial for Dashboard Display)
For applicants to appear on your dashboard, you need to create them in the Django Admin:

Start the development server (if not already running): python manage.py runserver

Access Django Admin: Open your browser and go to http://127.0.0.1:8000/admin/. Log in with your superuser credentials.

Create Users:

Under AUTHENTICATION AND AUTHORIZATION, click on Users.

Click "+ Add user".

Provide a Username, First name, Last name, and Email address. (First, Last, and Email are important for the dashboard display).

Click "Save". Repeat for multiple applicants if desired.

Create Projects (Optional but Recommended):

Under PORTFOLIOAPP, click on Projects.

Click "+ Add project".

Enter a Project name and Project description.

Click "Save". Create a few different projects.

Create Portfolios and Link them: This is the most critical step for dashboard population.

Under PORTFOLIOAPP, click on Portfolios.

Click "+ Add portfolio".

User: Select one of the User accounts you just created from the dropdown.

Portfolio title and Portfolio description: Fill these in.

Project: Optionally, select one of the Project objects you created.

Click "Save". Ensure you create a Portfolio object for each User you want to appear as an applicant.

7. Run the Development Server
Start the Django development server to access your web application:

Bash

python manage.py runserver
8. Access the Application
Django Admin: http://127.0.0.1:8000/admin/

Login with your superuser account to manage Users, Portfolios, and Projects.

Applicant Dashboard: http://127.0.0.1:8000/

This is the main dashboard page, displaying the list of applicants.

Applicant Detail: Click the "Go" button next to an applicant on the list page (e.g., http://127.0.0.1:8000/portfolio/<username>/).

Applicant Delete: Click the "Delete" button next to an applicant on the list page (e.g., http://127.0.0.1:8000/portfolio/<username>/delete/).

4. Git Commit Message Conventions
When making commits, please use the following formats:

feat: <description> - For new features added.

wip: <description> - For work in progress.

bug: <description> - For a feature that has a known bug.

fix: <description> - For a fix related to a bug or previous issue.
