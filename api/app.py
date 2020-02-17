#!../venv/bin/python3

# This project is licenced under the MIT licence.

# Imports.
from flask import Flask


# Debug output.
VERBOSE = True

# App declaration.
app = Flask(__name__)


# Request times for a building.
@app.route('/api/v1/times', methods=['POST'])
def times():
    return "Hello, World!"


# Entry point for the API.
if __name__ == '__main__':
    app.run(debug=VERBOSE)