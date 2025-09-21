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
from flask import request
from flask import Flask, request, redirect, url_for, flash, jsonify
import io
import csv
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import classification_report

from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import nltk
import re
from nltk.corpus import stopwords
nltk.download('stopwords', force=True)

from langchain_community.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib import pyplot as plt
OPENAI_API_KEY="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"

import numpy as np
import pandas as pd

data = pd.read_csv("preprocessed_reviews.csv")

data["Preprocessed Review"] = data["Preprocessed Review"].apply(lambda x : str(x))

preprocessed_text = data["Preprocessed Review"].values
tokenizer = Tokenizer(char_level=False, oov_token = "oov") 
tokenizer.fit_on_texts(preprocessed_text)
vocab_size = len(tokenizer.word_index)+1
max_len = 20

vocab_size = len(tokenizer.word_index)+1 
vocab_size

template1 = """
Context: You are analyzing sentiment in reviews from the Amazon Fine Food Reviews dataset. Your goal is to classify both the sentiment (positive, negative) and the reason label of a given review. Please provide the sentiment and reason labels based on the content of the review.

Note: Consider the language, tone, and context of the review when determining the sentiment and reason labels. If the sentiment or reason is ambiguous or mixed, you may mention that in your response.

---
Task:
    1. Predict the reason for review why its Positive , Negative .
    2. Output should be only Reason in JSON.
---

Instruction:

Base your sentiment and reason analysis solely on the content of the review without inventing any additional information.

Review Content: ```{Review}```
Sentiment Label: ```{Sentiment}```
"""

prompt_template1=PromptTemplate(
    input_variables=['Review', 'Sentiment'],
    template=template1
)


llm1=OpenAI(temperature=0,openai_api_key =OPENAI_API_KEY,model="gpt-3.5-turbo-instruct")
chain=LLMChain(
    llm=llm1,prompt=prompt_template1)


from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense, Dropout, LSTM, Bidirectional

n_lstm=128
embeding_dim =128
drop_lstm =0.2
model = Sequential()
model.add(Embedding(vocab_size, embeding_dim,name='embedding_4'))
model.add(LSTM(n_lstm, dropout=drop_lstm,return_sequences=False))

model.add(Dense(2, activation='softmax'))
# model.summary()

model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])

model.load_weights("lstm_w.h5", by_name=True, skip_mismatch=True)

import re
from bs4 import BeautifulSoup
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def preprocessed(review): 
    sentance = re.sub(r"http\S+", "", review)
    sentance = BeautifulSoup(sentance, 'lxml').get_text()
    sentance = decontracted(sentance)
    sentance = re.sub("\S*\d\S*", "", sentance).strip()
    sentance = re.sub('[^A-Za-z]+', ' ', sentance)
    sentance = ' '.join(e.lower() for e in sentance.split() if e.lower() not in stopwords.words('english'))
    return sentance.strip()


def predict(text,model,tokenizer,chain) : 
    
    review = text
    print("Review : " , review)
    preprocessed_re = preprocessed(review)
    print(preprocessed_re)
    token_sent = tokenizer.texts_to_sequences([preprocessed_re])
    seq = pad_sequences(token_sent, maxlen = 40, padding = "pre", truncating = "post")
    print(seq)
    c = model.predict(seq)

    o = np.argmax(c, axis=1)
    d = {1:"Positive", 0 : "Negative"}
    llm_output = chain.run(Review = review, Sentiment = d[o[0]], verbose = False)
    print("Sentiment Predicted By Deep Learning Model LSTM: ",d[o[0]])
    print("\n")
    print(llm_output)
    
    print("\n")
    print("Sentiment Label & Reason Predicted by LLM")

    llm_output = chain2.run(Review = review,verbose = False)
    print(llm_output)

    return {"Sentiment": d[o[0]],"LLM_REASON":llm_output}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder to store uploaded files
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
        print(query)
        if not query:
            return jsonify({'message': 'Query parameter is required'}), 400
        
        # ml code
        res = {"Sentiment": "Positive","LLM_REASON":"Reason: Good quality and appealing to finicky dogs"}

        # res  = predict(query,tokenizer,model,chain1)
        review = query
        print("Review : " , review)
        preprocessed_re = preprocessed(review)
        print(preprocessed_re)
        token_sent = tokenizer.texts_to_sequences([preprocessed_re])
        seq = pad_sequences(token_sent, maxlen = 40, padding = "pre", truncating = "post")
        print(seq)
        c = model.predict(seq)
        print(c)
        o = np.argmax(c, axis=1)
        d = {1:"Positive", 0 : "Negative"}
        llm_output = chain.run(Review = review, Sentiment = d[o[0]], verbose = False)
        print("Sentiment Predicted By Deep Learning Model LSTM: ",d[o[0]])
        print("\n")
        print(llm_output)

        res = {"Sentiment": d[o[0]],"LLM_REASON":llm_output}
        print(res)
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
    except Exception as e:
        print(e) 
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

        review = row["Text"]
        print("Review : " , review)
        preprocessed_re = preprocessed(review)
        print(preprocessed_re)
        token_sent = tokenizer.texts_to_sequences([preprocessed_re])
        seq = pad_sequences(token_sent, maxlen = 40, padding = "pre", truncating = "post")
        print(seq)
        c = model.predict(seq)
        print(c)
        o = np.argmax(c, axis=1)
        d = {1:"Positive", 0 : "Negative"}
        llm_output = chain.run(Review = review, Sentiment = d[o[0]], verbose = False)
        print("Sentiment Predicted By Deep Learning Model LSTM: ",d[o[0]])
        print("\n")
        print(llm_output)

        # res = {"Sentiment": d[o[0]],"LLM_REASON":llm_output}
        #print(res)
        d1 = {}
        d1["LLM_REASON"] = str(llm_output)
        d1["Sentiment"] = str(d[o[0]])
        d1["query"] = str(row["Text"]) 
        
        l.append(d1)
        res = {"Sentiment": d1["Sentiment"],"LLM_REASON":d1["LLM_REASON"]}
        data = str(res)
        # Store the query in the Search table

        if user:
            new_search = Search(query=row["Text"], result = data,user_id=user.id)
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