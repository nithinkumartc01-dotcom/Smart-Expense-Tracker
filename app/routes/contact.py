from flask import Blueprint, render_template

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("dashboard/contact.html")
 