from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, unset_jwt_cookies
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3306/expenseclaimsdata'
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


class EmployeeProjects(db.Model):
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

    def __init__(self,project_id, employee_id, currency_id, expense_date,amount,purpose,change_dept,alternative_dept_code,status,last_edit_claim_date):
        self.ProjectID = project_id
        self.EmployeeID = employee_id
        self.CurrencyID = currency_id
        self.ExpenseDate = expense_date
        self.Amount = amount
        self.Purpose = purpose
        self.ChargeToDefaultDept = change_dept
        self.AlternativeDeptCode = alternative_dept_code
        self.Status = status
        self.LastEditedClaimDate = last_edit_claim_date

class Currency(db.Model):
    CurrencyID = db.Column(db.Integer, primary_key=True)
    ExchangeRate = db.Column(db.Float, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def employee():
    employees = Employee.query.filter_by(EmployeeID=10001).first()
    employees = Employee.query.all()
    for employee in employees:
        print(employee)
     
    return ""

@app.route("/claims/<int:id>", methods=["DELETE"])
def deleteExpense(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({"error": "Expense not found"}), 404
    db.session.delete(Expense)
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

if __name__ == '__main__':
    app.run(debug=True)




