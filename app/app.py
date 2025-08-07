from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker + GitHub Actions!"

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db"
        )
        return "DB Connection OK!"
    except Exception as e:
        return f"DB Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
