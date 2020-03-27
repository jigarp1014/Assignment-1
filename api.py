import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
sdb = [
    {'id': 0,
     'f_name': 'Jigar',
     'l_name': 'Patel',
     'dob': '011197',
     'amt_due': '1000'},
    {'id': 1,
     'f_name': 'Koi',
     'l_name': 'Patel',
     'dob': '052394',
     'amt_due': '2000'},
    {'id': 2,
     'f_name': 'Krupali',
     'l_name': 'Patel',
     'dob': '073197',
     'amt_due': '3000'},
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Student sdb</h1>
<p>This is a sdb that includes information related to students</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/sdb', methods=['GET'])
def api_all():
    return jsonify(sdb)

@app.route('/api/v1/resources/sdb', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if sdb['id'] == id:
            results.append(sdb)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()