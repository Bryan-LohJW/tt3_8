from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({'msg': 'Username and password required'}), 400

    # accessToken: string,
    # firstName: string,
    
    # lastName: string,
    # employeeId: string,
    # accountNumber: string

    # Check if the user exists in the database and the password is correct
    # If successful, create an access token and return it to the client
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200

@app.route('/protected')
@jwt_required()
def protected():
    username = get_jwt_identity()
    return jsonify({'username': username}), 200
