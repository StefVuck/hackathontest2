from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Signup Endpoint
@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username')
    password = request.json.get('password')
    # Logic to save user in DB
    return jsonify(message='User created'), 201

# Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # Logic to verify user
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Token Verification Endpoint
@app.route('/verify', methods=['GET'])
@jwt_required()
def verify():
    return jsonify(message='Token is valid'), 200

if __name__ == '__main__':
    app.run(debug=True)