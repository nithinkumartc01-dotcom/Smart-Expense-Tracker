from flask import Blueprint, render_template, session, redirect, url_for
from app.models.user_model import get_all_users, delete_user

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    return render_template("dashboard/home.html")

@dashboard_bp.route("/admin/users")
def admin_users():
    if "user" not in session or session["user"] != "SmartX@gmail.com":
        return redirect(url_for("dashboard.home"))
    
    users = get_all_users()
    return render_template("dashboard/admin_users.html", users=users)

@dashboard_bp.route("/admin/delete_user/<user_id>", methods=["POST"])
def delete_user_route(user_id):
    if "user" not in session or session["user"] != "SmartX@gmail.com":
        return redirect(url_for("auth.login"))
        
    delete_user(user_id)
    return redirect(url_for("dashboard.admin_users"))
