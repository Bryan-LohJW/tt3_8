from flask import Flask, request, jsonify, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required, unset_jwt_cookies
from uuid import uuid4
import json
from errors import error_response

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'
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
            'purpose': self.Purpose,
            'project_id': self.ProjectID, 
            'claim_id': self.ClaimID,
            'currency_id': self.CurrencyID,
            'alternative_dept_code': self.AlternativeDeptCode,
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
    data = request.json.get('data')

    #check if claim_id exists
    claim = Projectexpenseclaims.query.get(claim_id)
    if not claim:
        return jsonify({"error": "Expense not found"}), 404


    # # check if charge to default dept is false, if it is, then retrieve the alterntaive dept code
    default_dept = data["chargeDefault"]
    alt_dept = data["altDepCode"]
    
    if default_dept==0 :
        if alt_dept !='':
            return jsonify({"message": "Default department is used"}),401
    
    else:
        if alt_dept == '':
            return jsonify({"message": "Alternative department code required"}), 401


    claim.ChargeToDefaultDept = data["chargeDefault"]
    claim.AlternativeDeptCode = data["altDepCode"]
    claim.CurrencyID = data['currency']

    claim.ExpenseDate = data["date"]
    claim.Amount = data["amount"]
    claim.Purpose = data["purpose"]

    claim.ProjectID = data["projectId"]
    
    
    db.session.commit()

    return jsonify({"message": "Expense updated"}), 200

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

@app.route('/claim/<int:id>', methods=['GET', 'POST'])
def get_claim(id):
    claim = Projectexpenseclaims.query.get(id)
    return claim.serialize()
    

@app.route('/login', methods=['POST'])
def login():
    data = request.json.get('data')
    print(data)
    id = data['id']
    password = data['password']
    
    employee = Employee.query.get(id)

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

@app.route('/claims', methods=['POST'])
# @jwt_required()
def add_expense():
    # cur = db.connection.cursor()
    # claim_id = str(uuid4)

    last_claim = db.session.query(Projectexpenseclaims).order_by(Projectexpenseclaims.ClaimID.desc()).first() 

    claim_id = last_claim.ClaimID +5 
    
    
    employee_id = request.json.get('employeeID')
#     employee_id_exists = db.session.query(
#     db.session.query(Employee).filter_by(EmployeeID=employee_id).exists()
# ).scalar()
#     if not employee_id_exists:
#         return jsonify({"error": "EmployeeID not found"}), 404
    
    project_id = request.json.get('projectId')
#     project_id_exists = db.session.query(
#     db.session.query(Employeeprojects).filter_by(ProjectID=project_id).exists()
# ).scalar()
#     if not project_id_exists:
#         return jsonify({"error": "ProjectID not found"}), 404

    amount = request.json.get('amount')
#     amount_exists = db.session.query(
#     db.session.query(Employee).filter_by(Amount=amount).exists()
# ).scalar()
    if not amount:
        return jsonify({"error": "Amount is null"}), 404

    currency_id = request.json.get('currency')
    currency_id_exists = db.session.query(
    db.session.query(Currency).filter_by(CurrencyID=currency_id).exists()
).scalar()
    if not currency_id_exists:
        return jsonify({"error": "CurrencyID not found"}), 404

    expense_date = request.json.get('date')
#     expense_date_exists = db.session.query(
#     db.session.query(Employee).filter_by(ExpenseDate=expense_date).exists()
# ).scalar()
    if not expense_date:
        return jsonify({"error": "ExpenseDate is null"}), 404

    purpose = request.json.get('purpose')
#     purpose_exists = db.session.query(
#     db.session.query(Employee).filter_by(Purpose=purpose).exists()
# ).scalar()
    if not purpose:
        return jsonify({"error": "Purpose is null"}), 404

    chargeDefault = request.json.get('chargeDefault')
#     chargeDefault_exists = db.session.query(
#     db.session.query(Employee).filter_by(ChargeToDefaultDept=chargeDefault).exists()
# ).scalar()
    if not chargeDefault:
        return jsonify({"error": "Charge To Default Deparment is null"}), 404

    altDepCode = request.json.get('altDepCode')
#     altDepCode_exists = db.session.query(
#     db.session.query(Employee).filter_by(AlternativeDeptCode=altDepCode).exists()
# ).scalar()
    if not altDepCode:
        return jsonify({"error": "Alternate Department Code is null"}), 404

    LastEditedClaimDate = db.Column(db.String(255), nullable=False)

#     status = request.json.get('status')
#     status_exists = db.session.query(
#     db.session.query(Employee).filter_by(Status=status).exists()
# ).scalar()
#     if not status_exists:
#         return jsonify({"error": "Status is null"}), 404

    last_edited_claim_date = request.json.get('last_edit_claim_date')
#     last_edited_claim_date_exists = db.session.query(
#     db.session.query(Employee).filter_by(LastEditedClaimDate).exists()
# ).scalar()
    if not last_edited_claim_date:
        return jsonify({"error": "Last Edited Claim Date not found"}), 404

    if chargeDefault==0 :
        if altDepCode !='':
            return jsonify({"message": "Default department is used"})
    
    else:
        if altDepCode == '':
            return jsonify({"message": "Alternative department code required"})
    
    q = (db.session.query( Employee, Employeeprojects)
        .join(Employee)
        .join(Employeeprojects)
        .filter_by(EmployeeID=employee_id)
        )
    print(q)
    if not q:
        return jsonify({"error": "Employee or Project does not exist "}), 404

    expense = Projectexpenseclaims(claim_id = claim_id,employee_id= employee_id,status='Pending', project_id = project_id, amount=amount, currency_id=currency_id,expense_date=expense_date, purpose=purpose, charge_dept=chargeDefault, alternative_dept_code=altDepCode,last_edit_claim_date= last_edited_claim_date)


    db.session.add(expense)
    db.session.commit()
    return jsonify({'msg': 'Expense created successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)




