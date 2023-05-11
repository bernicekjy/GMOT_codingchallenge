from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/client'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)


class Client(db.Model):
    __tablename__ = 'client'

    clientID = db.Column(db.String(20), primary_key=True)
    commission = db.Column(db.Float, nullable=False)
    grossAmount = db.Column(db.Float, nullable=False)
    lastUpdateTime = db.Column(db.DateTime, nullable=False,
                               default=datetime.now, onupdate=datetime.now)

    def __intit__(self, clientID, commission, grossAmount, lastUpdateTime):
        self.clientID = clientID
        self.commission = commission
        self.grossAmount = grossAmount
        self.lastUpdateTime = lastUpdateTime

    def json(self):
        return {
            "clientID": self.clientID,
            "commission": self.commission,
            "grossAmount": self.grossAmount,
            "lastUpdateTime": self.lastUpdateTime
        }

# get all posts - filter based on date


@app.route("/clients/<clientID>")
def get_all(clientID):
    clientlist = Client.query.filter_by(clientID=clientID).all()
    if len(clientlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "records": [record.json() for record in clientlist]
                },
                "message": "All client records have been successfully retrieved."
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no records."
        }
    ), 404

@app.route('/submit-form', methods=['POST'])
def submit_form():
    clientID = request.form.get('clientID')
    commissionDiff = request.form.get('commissionDifference')
    grossAmountDiff = request.form.get('grossAmountDifference')
   
    clientFound = Client.query.filter_by(clientID=clientID).first()

    if not len(clientFound):
        return 'ClientID not found.'

    if commissionDiff>clientFound.commission: #commission difference out of tolerance
        return 'Commission difference is out of tolerance.'
    elif grossAmountDiff>clientFound.grossAmount:
        return 'Gross amount is out of tolerance.'
    else:
        return 'Successful: Commission difference and gross amount are within setup tolerance'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
