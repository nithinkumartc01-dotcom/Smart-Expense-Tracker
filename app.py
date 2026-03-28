from app import create_app
from app.models.user_model import create_user, find_user_by_email

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        # Create default admin user if it doesn't exist
        if not find_user_by_email("SmartX@gmail.com"):
            create_user("SmartX@gmail.com", "be.smaxtX")
            print("Admin user 'SmartX@gmail.com' created successfully.")

    app.run(debug=True)
 