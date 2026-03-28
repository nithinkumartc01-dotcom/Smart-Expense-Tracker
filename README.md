# Smart Expense Tracker

A Flask-based expense tracker application with user authentication, expense logging, filtering, and admin user management.

## Features

- User registration and login
- Expense entry with amount, category, description, payment type, date, and place
- Expense tracker dashboard with filtered views
- Category and trend charts via dashboard
- Admin page to view all registered users and delete users
- MongoDB backend support
- Contact page

## Project Structure

- `app.py` - application starter and default admin creation
- `config.py` - environment-based Flask config
- `app/__init__.py` - Flask app factory
- `app/routes/` - route blueprints for auth, dashboard, expenses, and contact
- `app/models/` - MongoDB models for users and expenses
- `templates/` - HTML templates for auth, dashboard, and expenses
- `static/` - static assets (CSS, JS, images)
- `docker/mongo/docker-compose.yml` - MongoDB service definition

## Requirements

- Python 3.11+ or compatible
- MongoDB running locally or remote
- `pip` packages from `requirements.txt`

## Setup

1. Clone or copy the repository.
2. Create and activate a Python virtual environment.
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies.
   ```powershell
   pip install -r requirements.txt
   ```
4. Start MongoDB.
   - Local MongoDB: ensure `mongodb://localhost:27017/` is available
   - Or use Docker compose:
     ```powershell
     docker compose -f docker\mongo\docker-compose.yml up -d
     ```
5. Configure environment variables (optional).
   - `SECRET_KEY` (defaults to `smartx-secret-key`)
   - `MONGO_URI` (defaults to `mongodb://localhost:27017/smartx_db`)

## Run the App

From the project root:

```powershell
python app.py
```

Then open `http://127.0.0.1:5000/login` in your browser.

## Default Admin

When the app first runs, it creates a default admin user if one does not already exist:

- Email: `SmartX@gmail.com`
- Password: `be.smaxtX`

Use this account to access admin user management at `/admin/users`.

## Notes

- The app stores users and expenses in MongoDB collections.
- User passwords are hashed using Werkzeug.
- The admin route is restricted to the default admin email.

## License

This project has no license specified. Add a license file if you want to publish under an open-source license.
