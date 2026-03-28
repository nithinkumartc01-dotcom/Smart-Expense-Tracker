from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.user_model import create_user, find_user_by_email, verify_password

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if find_user_by_email(email):
            return "User already exists"

        create_user(email, password)
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

 
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = find_user_by_email(email)

        if user and verify_password(user["password"], password):
            session["user"] = email
            return redirect(url_for("dashboard.home"))

        if not user:
            error = "User not found"
        else:
            error = "Invalid credentials"

    return render_template("auth/login.html", error=error)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
