from app import mongo
from datetime import datetime

def add_expense(user_email, amount, category, description, pay_type, date, place):
    mongo.db.expenses.insert_one({
        "user": user_email,
        "amount": float(amount),
        "category": category,
        "description": description,
        "pay_type": pay_type,
        "date": date or datetime.utcnow().strftime("%Y-%m-%d"),
        "place": place
    })

def get_expenses(user_email):
    return list(mongo.db.expenses.find({"user": user_email}))
 