from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "<h1>Hello from Flask!</h1>"

@main.route('/companies')
def view_companies():
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM companies")
    data = cursor.fetchall()
    cursor.close()
    return render_template('companies.html', companies = data)