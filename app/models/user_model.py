from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

def create_user(email, password):
    users = mongo.db.users
    hashed_password = generate_password_hash(password)

    users.insert_one({
        "email": email,
        "password": hashed_password
    })

def find_user_by_email(email):
    return mongo.db.users.find_one({"email": email})

def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)

def get_all_users():
    return list(mongo.db.users.find())

def delete_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        mongo.db.expenses.delete_many({"user": user["email"]})
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})