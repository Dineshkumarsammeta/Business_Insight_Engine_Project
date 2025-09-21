from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
import ast
import json
from flask import Flask, request, redirect, url_for, flash, jsonify
import io
import csv
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and all origins

app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
swagger = Swagger(app)

# SQLAlchemy User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    searches = db.relationship('Search', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# SQLAlchemy Search Model
class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.Text, nullable=False)
    result = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Search('{self.query}', '{self.timestamp}')"

# Decorator to check JWT token validity
def authorized(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Missing authorization token'}), 401

        try:
            decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            username = decoded_token['username']
            # Add any additional checks here, such as checking if the user exists in the database
            return func(username, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

    return wrapper


@app.route('/hello', methods=['GET'])
def hello():
    """
    Hello Endpoint
    ---
    responses:
      200:
        description: A simple hello message
        content:
          text/plain:
            schema:
              type: string
    """
    return jsonify({'message': 'Hello, World!'})


# Signup Endpoint
@app.route('/signup', methods=['POST'])
def signup():
    """
    User Signup
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    responses:
      201:
        description: User created successfully
      400:
        description: Bad request
    """
    data = request.form
    username = data.get('username')
    
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Please provide username, email, and password'}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists. Please choose a different one.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Email already exists. Please use a different email.'}), 400

# Signin Endpoint
@app.route('/signin', methods=['POST'])
def signin():
    """
    User Signin
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    responses:
      200:
        description: Token generated successfully
      400:
        description: Bad request
      401:
        description: Unauthorized
    """
    data = request.form
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Please provide username and password'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    token = jwt.encode({'username': username, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return jsonify({'token': token}), 200


# Predict Endpoint
@app.route('/predict', methods=['POST'])
@authorized
def predict(username):
    """
    Predict Endpoint
    ---
    parameters:
      - name: query
        in: formData
        type: string
        required: true
        description: The prediction query
    responses:
      200:
        description: Query stored successfully
    """
    try : 
        
        query = request.form.get('query')

        if not query:
            return jsonify({'message': 'Query parameter is required'}), 400
        
        # ml code
        res = {"Sentiment": "Positive","LLM_REASON":"Reason: Good quality and appealing to finicky dogs"}
        data = str(res)
        # Store the query in the Search table
        user = User.query.filter_by(username=username).first()
        if user:
            new_search = Search(query=query, result = data,user_id=user.id)
            db.session.add(new_search)
            db.session.commit()
            return jsonify(res), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except: 
        return jsonify({'message': 'Server Error'}), 500


@app.route('/fetch_searches', methods=['GET'])
@authorized
def fetch_searches(username):
    """
    Fetch Searches Endpoint
    ---
    responses:
      200:
        description: Searches fetched successfully
      404:
        description: User not found
    """
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404
    print(user.id)
    searches = User.query.get(user.id)
    print(searches)

    print(searches.searches)
    
    search_list = [{'query': search.query, 'result': ast.literal_eval(search.result), 'timestamp': search.timestamp} for search in searches.searches]
    # for x in search_list : 
    #     print(x["result"])
    #     print(type(x["result"]))
    #     print(ast.literal_eval(x["result"]))
    return jsonify({'searches':search_list}), 200

@app.route('/upload', methods=['POST'])
@authorized
def upload(username):
    print(username)
    if 'csvfile' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['csvfile']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Check if the file is a CSV
    if not file.filename.lower().endswith('.csv'):
        return jsonify({"error": "File is not a CSV"}), 400

    # Read the CSV content in memory
    stream = io.StringIO(file.stream.read().decode("UTF-8"), newline=None)
    csv_reader = csv.DictReader(stream)  # DictReader to get rows as dictionaries
    
    # Convert the CSV content into a list of dictionaries
    csv_content = [row for row in csv_reader]
    l = []
    user = User.query.filter_by(username=username).first()
    for row in csv_content :
        row["LLM_REASON"] = "LLM_REASON" *100
        row["Sentiment"] = "Positive"
        row["query"] = str(row["Text"]) *1090
        del row["Text"]
        l.append(row)
        res = {"Sentiment": row["Sentiment"],"LLM_REASON":row["LLM_REASON"]}
        data = str(res)
        # Store the query in the Search table

        if user:
            new_search = Search(query=row["query"], result = data,user_id=user.id)
            db.session.add(new_search)
            db.session.commit()
        else:
            return jsonify({'message': 'User not found'}), 404

    # Return the JSON representation of the CSV content
    return jsonify({"csv_content": l})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)