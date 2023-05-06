from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, unset_jwt_cookies
from uuid import uuid4

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/expenseclaimsdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Department(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supervisor_id = db.Column(db.Integer)
    department_code = db.Column(db.Integer, db.ForeignKey('Department.code'))
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    bank_account_no = db.Column(db.String(50), nullable=False)

    def __init__(self, supervisor_id,department_code,firstname, lastname, password,bank_account_no):
        self.supervisor_id = supervisor_id
        self.department_code = department_code
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.bank_account_no = bank_account_no


class EmployeeProjects(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer,  db.ForeignKey('Employee.id'))
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    lead_id = db.Column(db.String(255), nullable=False)

    def __init__(self,employee_id, firstname, lastname, password,bank_account_no):
        self.employee_id = employee_id
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.bank_account_no = bank_account_no

class Expense(db.Model):
    claim_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('EmployeeProjects.project_id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'))
    currency_id = db.Column(db.Integer, db.ForeignKey('Currency.id'))
    expense_date = db.Column(db.String(255), nullable=False)
    amount= db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(255), nullable=False)
    change_dept = db.Column(db.Boolean, nullable=False)
    alternative_dept_code = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    last_edit_claim_date = db.Column(db.String(255), nullable=False)

    def __init__(self,project_id, employee_id, currency_id, expense_date,amount,purpose,change_dept,alternative_dept_code,status,last_edit_claim_date):
        self.project_id = project_id
        self.employee_id = employee_id
        self.currency_id = currency_id
        self.expense_date = expense_date
        self.amount = amount
        self.purpose = purpose
        self.change_dept = change_dept
        self.alternative_dept_code = alternative_dept_code
        self.status = status
        self.last_edit_claim_date = last_edit_claim_date

@app.route('/')
def employee():
    employees = Employee.query.all()
    return employees
# @app.route("/claims/<int:claim_id>")

@app.route('/employee')
def displayEmployeeRecord():
    employees = Employee.query.all()
    return employees

@app.route('/claims', methods=['POST'])
@jwt_required()
def add_expense():
    cur = db.connection.cursor()
    project_id = request.json.get('projectId')
    amount = request.json.get('amount')
    currency_id = request.json.get('currency')
    expense_date = request.json.get('date')
    purpose = request.json.get('purpose')
    chargeDefault = request.json.get('chargeDefault')
    altDepCode = request.json.get('altDepCode')
    if chargeDefault == 0:
        altDepCode = ""
    expense = Expense(employee_id = str(uuid4), project_id = project_id, amount=amount, currency_id=currency_id,expense_date=expense_date, purpose=purpose, chargeDefault=chargeDefault, altDepCode=altDepCode)
    sql = """INSERT INTO ProjectExpenseClaims (age, gender, name, email, accuracy) VALUES (%d, %d, %s, %s, %f);"""
    fields = (p)
    cur.execute(sql % fields)
    
 
    db.session.add(expense)
    db.session.commit()
    return jsonify({'msg': 'Expense created successfully'}), 201

    # claim_id = db.Column(db.Integer, primary_key=True)
    # project_id = db.Column(db.Integer, db.ForeignKey('EmployeeProjects.project_id'))
    
    # employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'))
    
    # currency_id = db.Column(db.Integer, db.ForeignKey('Currency.id'))
    # expense_date = db.Column(db.String(255), nullable=False)
    # amount= db.Column(db.Float, nullable=False)
    # purpose = db.Column(db.String(255), nullable=False)
    # change_dept = db.Column(db.Boolean, nullable=False)
    # alternative_dept_code = db.Column(db.String(20), nullable=False)
    # status = db.Column(db.String(20), nullable=False)
    # last_edit_claim_date = db.Column(db.String(255), nullable=False)


# projectId: string,
# amount: string,
# currency: string
# date: string,
# purpose: string,
# chargeDefault: boolean,
# altDepCode: string,
# }

# Response: 
# {
# message: string,
# }

    # claim_id = db.Column(db.Integer, primary_key=True)
    # project_id = db.Column(db.Integer, db.ForeignKey('EmployeeProjects.project_id'))
    # employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'))
    # currency_id = db.Column(db.Integer, db.ForeignKey('Currency.id'))
    # expense_date = db.Column(db.String(255), nullable=False)
    # amount= db.Column(db.Float, nullable=False)
    # purpose = db.Column(db.String(255), nullable=False)
    # change_dept = db.Column(db.Boolean, nullable=False)
    # alternative_dept_code = db.Column(db.String(20), nullable=False)
    # status = db.Column(db.String(20), nullable=False)
    # last_edit_claim_date = db.Column(db.String(255), nullable=False)

if __name__ == '__main__':
    app.run(debug=True)




