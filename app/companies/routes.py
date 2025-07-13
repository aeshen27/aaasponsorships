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
        type = request.form.get('type')
        email = request.form.get('email')
        contact = request.form.get('contact')
        notes = request.form.get('notes')

        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
        INSERT INTO companies (name, contacted, type, email, contact, notes) VALUES (%s, 'no', %s, %s, %s, %s);
        """
        values = (name, type, email, contact, notes)
        try:
            cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            print("DB Error:", e)
            raise
        
        return redirect(url_for('companies.list_companies'))
    
    return render_template('companies/add.html')
