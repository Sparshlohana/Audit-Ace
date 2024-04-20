from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/')
def hello_world():
    return jsonify({
        "name": "Sparsh",
        "roll Number": "123" # Fixed the typo here
    })

if __name__ == '__main__':
    app.run(debug=True)
