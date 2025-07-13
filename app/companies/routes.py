from flask import Blueprint, render_template, request, redirect, url_for
from .. import db 

companies = Blueprint('companies', __name__, url_prefix='/companies')

@companies.route('/')
def list_companies():
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM companies")
    data = cursor.fetchall()
    cursor.close()
    return render_template('list.html', companies = data)
