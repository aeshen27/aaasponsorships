from flask import Blueprint, render_template
import mysql.connector
import config

main = Blueprint('main', __name__)

conn = mysql.connector.connect(
    host="localhost",
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

@main.route('/')
def home():
    return "<h1>Hello from Flask!</h1>"

@main.route('/companies')
def view_companies():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM companies")
    data = cursor.fetchall()
    cursor.close()
    return render_template('companies.html', companies = data)