from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def drinks():
    return {"drinks":"drink data"}