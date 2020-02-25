# This project is licenced under the MIT licence.

# Imports.
from flask import Flask, request, abort
import db


# Debug output.
VERBOSE = True

# App declaration.
app = Flask(__name__)


# Request rooms for a given building, day, and time.
@app.route('/api/v1/rooms', methods=['POST'])
def get_rooms():
    print(request.json)

    # Verify JSON data to have a building, time, and day.
    if (not request.json) or ('day' not in request.json) or \
       ('building' not in request.json) or ('time' not in request.json):
        abort(400)

    res = db.query(request.json['building'], request.json['day'], request.json['time'])

    return {"hi": "bye"}, 201


# Entry point for the API.
if __name__ == '__main__':
    app.run(debug=VERBOSE)