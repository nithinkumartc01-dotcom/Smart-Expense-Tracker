from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.expense_model import add_expense, get_expenses
from bson.objectid import ObjectId
from .. import mongo

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/tracker", methods=["GET", "POST"])
def tracker():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        add_expense(
            session["user"],
            request.form["amount"],
            request.form["category"],
            request.form["description"],
            request.form["type"], 
            request.form["date"],
            request.form.get("place")
        )
        return redirect(url_for("expenses.tracker"))

    month = request.args.get("month")
    category = request.args.get("filter_category")

    query = {"user": session["user"]}

    if month:
        query["date"] = {"$regex": f"^{month}"}
    if category:
        query["category"] = category

    expenses = list(mongo.db.expenses.find(query))

    # Prepare data for charts
    category_totals = {}
    date_totals = {}

    for expense in expenses:
        cat = expense.get("category", "Uncategorized")
        category_totals[cat] = category_totals.get(cat, 0) + float(expense["amount"])
        
        d = expense.get("date", "")
        if d:
            date_totals[d] = date_totals.get(d, 0) + float(expense["amount"])

    # Sort dates for the trend chart
    sorted_dates = sorted(date_totals.keys())
    trend_data = [date_totals[d] for d in sorted_dates]

    return render_template("dashboard/tracker.html", 
                           expenses=expenses,
                           category_labels=list(category_totals.keys()),
                           category_data=list(category_totals.values()),
                           trend_labels=sorted_dates,
                           trend_data=trend_data)

@expenses_bp.route("/delete/<expense_id>", methods=["POST"])
def delete_expense(expense_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    mongo.db.expenses.delete_one({"_id": ObjectId(expense_id)})
    return redirect(url_for("expenses.tracker"))
