#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/demo', methods=['POST'])
def predict():
  # file input
  f = request.files['file']
  f.save('./uploads/' + secure_filename(f.filename))

  result = 'hello';
  return jsonify({ 'result': result }), 201

if __name__ == '__main__':
  app.run(debug=True)
