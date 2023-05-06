from flask import Flask, request, jsonify, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, unset_jwt_cookies
from uuid import uuid4
import json
from errors import error_response

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/expenseclaimsdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Department(db.Model):
    DepartmentCode = db.Column(db.Integer, primary_key=True)
    DepartmentName = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.DepartmentName = name

class Employee(db.Model):
    EmployeeID = db.Column(db.Integer, primary_key=True)
    SupervisorID = db.Column(db.Integer)
    DepartmentCode = db.Column(db.Integer, db.ForeignKey('department.code'))
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    BankAccountNumber = db.Column(db.String(50), nullable=False)

    def __init__(self, supervisor_id,department_code,firstname, lastname, password,bank_account_no):
        self.SupervisorID = supervisor_id
        self.DepartmentCode = department_code
        self.FirstName = firstname
        self.LastName = lastname
        self.Password = password
        self.BankAccountNumber = bank_account_no


class Employeeprojects(db.Model):
    ProjectID = db.Column(db.Integer, primary_key=True)
    EmployeeID = db.Column(db.Integer,  db.ForeignKey('employee.EmployeeID'))
    ProjectName = db.Column(db.String(100), nullable=False)
    ProjectStatus = db.Column(db.String(255), nullable=False)
    ProjectBudget = db.Column(db.Float, nullable=False)
    ProjectLeadID = db.Column(db.String(255), nullable=False)

    def __init__(self,employee_id, projectname, projectstatus, projectbudget, projectleadid):
        self.EmployeeID = employee_id
        self.ProjectName = projectname
        self.ProjectStatus = projectstatus
        self.ProjectBudget = projectbudget
        self.ProjectLeadID = projectleadid

class Projectexpenseclaims(db.Model):
    ClaimID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('employeeprojects.ProjectID'))
    EmployeeID = db.Column(db.Integer, db.ForeignKey('employee.EmployeeID'))
    CurrencyID = db.Column(db.Integer, db.ForeignKey('currency.CurrencyID'))
    ExpenseDate = db.Column(db.String(255), nullable=False)
    Amount = db.Column(db.Float, nullable=False)
    Purpose = db.Column(db.String(255), nullable=False)
    ChargeToDefaultDept = db.Column(db.Boolean, nullable=False)
    AlternativeDeptCode = db.Column(db.String(20), nullable=False)
    Status = db.Column(db.String(20), nullable=False)
    LastEditedClaimDate = db.Column(db.String(255), nullable=False)

    def __init__(self, claim_id, project_id, employee_id, currency_id, expense_date,amount,purpose,change_dept,alternative_dept_code,status,last_edit_claim_date):
        self.ClaimID = claim_id
        self.ProjectID = project_id
        self.EmployeeID = employee_id
        self.CurrencyID = currency_id
        self.ExpenseDate = expense_date
        self.Amount = amount
        self.Purpose = purpose
        self.ChangeToDefaultDept = change_dept
        self.AlternativeDeptCode = alternative_dept_code
        self.Status = status
        self.LastEditedClaimDate = last_edit_claim_date
        
    def serialize(self):
        return {
            'employee_id': self.EmployeeID,
            'status': self.Status,
            'project_id': self.ProjectID, 
            'claim_id': self.ClaimID,
            'currency_id': self.CurrencyID,
            'amount': self.Amount,
        }
        
class Currency(db.Model):
    CurrencyID = db.Column(db.Integer, primary_key=True)
    ExchangeRate = db.Column(db.Float, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def employee():
    employee = Employee.query.filter_by(EmployeeID=10001).first()
    #employees = Employee.query.all()
    
     
    return jsonify({"message": "Expense deleted"})


@app.route("/claims/<int:id>", methods=["DELETE"])
def deleteExpense(id):
    expense = Projectexpenseclaims.query.get(id)
    print(expense)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Expense deleted"})

@app.route("/claims/<int:claim_id>", methods=['PUT'])
def update_claim(claim_id):

    #check if claim_id exists
    claim = Projectexpenseclaims.query.get(claim_id)
    if not claim:
        return jsonify({"error": "Expense not found"}), 404


    # # check if charge to default dept is false, if it is, then retrieve the alterntaive dept code
    default_dept =request.json.get("chargeDefault")
    alt_dept = request.json.get("altDepCode")
    if default_dept==1 :
        if alt_dept !='':
            return jsonify({"message": "Default department is used"})
    
    else:
        if alt_dept == '':
            return jsonify({"message": "Alternative department code required"})


    Projectexpenseclaims.ChargeToDefaultDept = request.json.get("chargeDefault")
    Projectexpenseclaims.AlternativeDeptCode = request.json.get("altDepCode")

    Projectexpenseclaims.ExpenseDate = request.json.get("date")
    Projectexpenseclaims.Amount = request.json.get("amount")
    Projectexpenseclaims.Purpose = request.json.get("purpose")

    Projectexpenseclaims.ProjectID = request.json.get("projectId")
    Projectexpenseclaims.LastEditedClaimDate= request.json.get("updateDate")
    
    db.session.commit()

    return jsonify({"message": "Expense updated"})

@app.route('/claims/<int:id>', methods=['GET'])
def claims(id):
    claims = Projectexpenseclaims.query.filter_by(EmployeeID=id)
    claimList = []
    for claim in claims:
        claimList.append(claim.serialize())
    #claim_response = jsonify([e.serialize() for e in claims])
    claim_response = {}
    claim_response['claims'] = claimList
    
    return claim_response

@app.route('/login', methods=['POST'])
def login():
    
    id = request.json.get('id')
    password = request.json.get('password')
    
    employee = Employee.query.get(id)
    print(employee)
    if not id or not password:
        return error_response(400, 'Employee ID and password required')
    
    if not id or employee.Password != password:
        return error_response(401, "Employee ID or password invalid.")

    firstName = employee.FirstName
    lastName = employee.LastName
    accountNumber = employee.BankAccountNumber
    
    # Check if the user exists in the database and the password is correct
    # If successful, create an access token and return it to the client
    access_token = create_access_token(identity=id)
    return jsonify({'access_token': access_token, 'firstName': firstName, 'lastName': lastName, 'accountNumber' : accountNumber}), 200

@app.route('/protected')
@jwt_required()
def protected():
    id = get_jwt_identity()
    return jsonify({'employeeId': id}), 200

'''
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
    expense = Projectexpenseclaims(employee_id = str(uuid4), project_id = project_id, amount=amount, currency_id=currency_id,expense_date=expense_date, purpose=purpose, chargeDefault=chargeDefault, altDepCode=altDepCode)
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
'''

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




