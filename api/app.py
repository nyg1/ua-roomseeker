# This project is licenced under the MIT licence.

# Imports.
from flask import Flask, request, abort


# Debug output.
VERBOSE = True

# App declaration.
app = Flask(__name__)


# Request rooms for a given building, day, and time.
@app.route('/api/v1/rooms', methods=['POST'])
def get_rooms():
    # Verify JSON data to have a building, time, and day.
    if (not request.json) or ('day' not in request.json) or \
       ('building' not in request.json) or ('time' not in request.json):
        abort(400)

    return {"hi": "bye"}, 201


# Entry point for the API.
if __name__ == '__main__':
    app.run(debug=VERBOSE)