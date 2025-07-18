# Junior Developer Applicant Dashboard

This Django web application serves as a dashboard to manage and view junior developer applicants and their portfolios. Data is handled via the Django Admin interface.

## 1. Features

* **Applicant Listing**: Displays a table of applicants with First Name, Last Name, Email, and action buttons ("Go" to detail, "Delete" to remove).
* **Applicant Detail**: Shows comprehensive portfolio information for a selected applicant, including assigned project details.
* **Applicant Deletion**: Removes a user and their associated portfolio from the database.
* **Custom Models**: `Portfolio` (One-to-One with Django's `User` model) and `Project` (One-to-One with `Portfolio`).
* **Views**: Function-Based View for the list, Class-Based Views for detail and delete.
* **URLs**: Uses clean URLs like `/` (list), `/portfolio/<username>/` (detail), and `/portfolio/<username>/delete/` (delete).
* **Frontend**: Uses Bootstrap 5 for responsive design, served as local static files.
* **Admin Integration**: All `User`, `Portfolio`, and `Project` data is manageable via Django Admin.

## 2. Project Structure

Quiz2_AbellaNicholasBenedictE._CPE202/
├── .venv/                   # Virtual environment (ignored by Git)
├── Dashboard/               # Main Django project settings (settings.py, urls.py)
├── PortfolioApp/            # Core application for applicant dashboard logic
│   ├── migrations/          # Database migrations
│   ├── admin.py             # Model registration for admin
│   ├── models.py            # Portfolio & Project models
│   ├── urls.py              # App-specific URL patterns
│   └── views.py             # View functions and classes
├── static/                  # Bootstrap CSS/JS files
├── templates/               # HTML templates (base.html, list.html, portfolio.html, etc.)
├── .gitignore               # Excludes .venv/ and db.sqlite3
├── db.sqlite3               # SQLite database (ignored by Git)
└── manage.py                # Django management script

## 3. Setup and Running the Project

Follow these steps to get the project running locally:

### Prerequisites

* Python 3.x
* Git

### Steps

1.  **Clone the Repository**:
    ```bash
    git clone <YOUR_GITHUB_REPO_URL_HERE>
    cd Quiz2_AbellaNicholasBenedictE._CPE202
    ```

2.  **Create & Activate Virtual Environment**:
    ```bash
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # macOS/Linux: source .venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install Django # Or pip install -r requirements.txt if you've created one
    ```

4.  **Apply Migrations**:
    ```bash
    python manage.py makemigrations PortfolioApp
    python manage.py migrate
    ```

5.  **Create Superuser**:
    ```bash
    python manage.py createsuperuser
    ```
    Follow prompts to create an admin account.

6.  **Populate Data (via Admin)**:
    * Run `python manage.py runserver`.
    * Go to `http://127.0.0.1:8000/admin/`.
    * Log in and create `Users` (filling First/Last Name, Email), `Projects`, and `Portfolios` (linking a `Portfolio` to a `User` and optionally a `Project`). **An applicant will only appear on the dashboard if they have a linked `Portfolio` object.**

7.  **Run Development Server**:
    ```bash
    python manage.py runserver
    ```

8.  **Access Application**:
    * **Dashboard**: `http://127.0.0.1:8000/`
    * **Admin**: `http://127.0.0.1:8000/admin/`

## 4. Git Commit Message Conventions

* `feat: <description>` (New feature)
* `wip: <description>` (Work in progress)
* `bug: <description>` (Feature has a known bug)
* `fix: <description>` (Fix for a bug/issue)
