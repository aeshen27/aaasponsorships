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
    return render_template('companies/list.html', companies = data)

@companies.route('/add', methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT ()")
        
        return redirect(url_for('companies.list_companies'))
    
    return render_template('companies/add.html')
