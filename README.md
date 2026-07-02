# Flask Blog

A full-featured blog web application built with Flask. Users can register, log in, write and manage posts, customize their profile, and reset forgotten passwords over email. Built following the application-factory pattern with modular blueprints.

## Features

- **User authentication** — registration, login, and logout with secure bcrypt-hashed passwords and "remember me" sessions
- **Account management** — update username, email, and upload a profile picture
- **Blog posts** — full CRUD: create, read, update, and delete posts, with a confirmation modal on delete
- **Authorization** — posts can only be edited or deleted by their author
- **Per-user post pages** — view all posts by a given user, with pagination
- **Password reset** — request a reset link by email; time-limited, signed tokens
- **Custom error pages** — dedicated 403, 404, and 500 handlers
- **Flash messaging** — user feedback on actions, styled with Bootstrap alert categories

## Tech Stack

- **Backend:** Flask (application factory + blueprints)
- **Database:** SQLite (development) via Flask-SQLAlchemy ORM
- **Authentication:** Flask-Login, Flask-Bcrypt
- **Forms:** Flask-WTF / WTForms with server-side validation
- **Email:** Flask-Mail (Gmail SMTP)
- **Tokens:** itsdangerous (`URLSafeTimedSerializer`)
- **Frontend:** Jinja2 templates, Bootstrap 4

## Project Structure

```
flask-blog/
├── run.py                  # Entry point — creates and runs the app
├── requirements.txt
├── .env                    # Environment variables (not committed)
├── .gitignore
└── flaskblog/
    ├── __init__.py         # Application factory, extension setup
    ├── config.py           # Config class (reads from environment)
    ├── models.py           # User and Post database models
    ├── main/               # Home and about routes
    │   └── routes.py
    ├── users/              # Auth, account, password reset
    │   ├── routes.py
    │   ├── forms.py
    │   └── utils.py        # save_picture, send_reset_email helpers
    ├── posts/              # Post CRUD
    │   ├── routes.py
    │   └── forms.py
    ├── errors/             # Error handlers
    │   └── handlers.py
    ├── static/
    │   └── profile_pics/   # Uploaded and default profile images
    └── templates/          # Jinja2 templates (incl. errors/ subfolder)
```

## Getting Started

### Prerequisites

- Python 3.12 or 3.13
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IshaanArekar/Python-Flask-Blog.git
   cd Python-Flask-Blog
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate      # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```
   SECRET_KEY=your-secret-key
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASS=your-gmail-app-password
   ```
   Generate a secret key with:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```
   > **Note:** `EMAIL_PASS` must be a Gmail **App Password** (requires 2-Step Verification), not your regular password.

5. Create the database:
   ```bash
   python
   ```
   ```python
   from flaskblog import create_app, db
   app = create_app()
   with app.app_context():
       db.create_all()
   ```

### Running the App

```bash
python run.py
```

Visit `http://127.0.0.1:5001` in your browser.

## Environment Variables

| Variable      | Description                                   |
|---------------|-----------------------------------------------|
| `SECRET_KEY`  | Flask secret key for sessions and CSRF        |
| `EMAIL_USER`  | Gmail address used to send reset emails       |
| `EMAIL_PASS`  | Gmail App Password (16 characters, no spaces) |

All secrets are loaded from the environment and are never committed to the repository.

## Notes

- The database file (`site.db`), the `.env` file, uploaded profile pictures, and `__pycache__` are excluded from version control via `.gitignore`.
- Profile picture uploads are stored on the local filesystem under `static/profile_pics/`.
- Password reset tokens expire after 30 minutes.

## License

This project is available under the MIT License.
