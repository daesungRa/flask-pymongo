from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    return 'Welcome To This Page!'

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()