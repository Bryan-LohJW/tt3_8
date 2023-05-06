from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from errors import error_response
from flask_sqlalchemy import SQLAlchemy
from app import Employee

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost:3306/expenseclaimsdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/login', methods=['POST'])
def login():
    
    id = request.json.get('id')
    password = request.json.get('password')
    employee = db.get_user_by_id(id)
    employee = Employee.query.filter_by(EmployeeID=id)
    if not id or not password:
        return error_response(400, 'Employee ID and password required')
    
    if not id or employee.password != password:
        return error_response(401, "Employee ID or password invalid.")

    firstName = employee.firstname
    lastName = employee.lastName
    accountNumber = employee.bank_account_no
    
    # Check if the user exists in the database and the password is correct
    # If successful, create an access token and return it to the client
    access_token = create_access_token(identity=id)
    return jsonify({'access_token': access_token, 'firstName': firstName, 'lastName': lastName, 'accountNumber' : accountNumber}), 200

@app.route('/protected')
@jwt_required()
def protected():
    id = get_jwt_identity()
    return jsonify({'employeeId': id}), 200
