import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "smartx-secret-key")
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017/smartx_db"
    )
 