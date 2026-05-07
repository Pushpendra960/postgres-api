from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="db",
    database="mydb",
    user="sid",
    password="sidpass"
)

@app.route("/")
def home():
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    return f"PostgreSQL Connected 🚀<br>{version}"

app.run(host="0.0.0.0", port=5000)
