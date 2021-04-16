import flask
from flask import request, jsonify

from patient import Patient

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 'hello world'


@app.route('/summary', methods=['GET'])
def api_all():
    patient_id = request.args.get('patient_id')
    date = request.args.get('date')
    p = Patient(patient_id)
    return jsonify(p.get_summary(date))


app.run()
