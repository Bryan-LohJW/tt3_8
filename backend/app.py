from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, unset_jwt_cookies


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3306/expenseclaimsdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # supervisor_id = db.Column(db.Integer)
    # department_code = db.Column(db.Integer)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    bank_account_no = db.Column(db.String(50), nullable=False)

    def __init__(self, firstname, lastname, password,bank_account_no):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.bank_account_no = bank_account_no


class EmployeeProjects(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.foreign_key='Employee.id')
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.float, nullable=False)
    lead_id = db.Column(db.String(255), nullable=False)

    def __init__(self, firstname, lastname, password,bank_account_no):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.bank_account_no = bank_account_no






if __name__ == '__main__':
    app.run(debug=True)




