import os

db_password = os.getenv("DB_PASSWORD")

if db_password:
    print("Secret received successfully!")
else:
    print("No secret found.")
