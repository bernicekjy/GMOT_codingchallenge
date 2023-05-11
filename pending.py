import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import exc

from datetime import datetime
import json
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/pending'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)


class Pending(db.Model):
    __tablename__ = 'pending'

    submissionID = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    clientID = db.Column(db.String(20), nullable=False)
    newCommission = db.Column(db.Float, nullable=False)
    newGrossAmount = db.Column(db.Float, nullable=False)
    submitterID = db.Column(db.String(20), nullable=False)
    submittedTime = db.Column(db.DateTime, nullable=False,
                              default=datetime.now, onupdate=datetime.now)

    def __intit__(self, submissionID, clientID, newCommission, newGrossAmount, submitterID, submittedTime):
        self.submissionID = submissionID
        self.clientID = clientID
        self.newCommission = newCommission
        self.newGrossAmount = newGrossAmount
        self.submitterID = submitterID
        self.submittedTime = submittedTime

    def json(self):
        return {
            "submissionID": self.submissionID,
            "clientID": self.clientID,
            "newCommission": self.newCommission,
            "newGrossAmount": self.newGrossAmount,
            "submitterID": self.submitterID,
            "submittedTime": self.submittedTime
        }


@app.route("/pending")
def get_all():
    requestslist = Pending.query.all()
    if len(requestslist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "records": [record.json() for record in requestslist]
                },
                "message": "All records have been successfully retrieved."
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no records."
        }
    ), 404


@app.route("/pending/new", methods=['POST'])
def create_order():
    data = request.get_json()
    pending = Pending(**data)

    try:
        db.session.add(pending)
        db.session.commit()

    except exc.IntegrityError as e:
        # rollback the transaction to avoid partially committing the changes
        db.session.rollback()
        print(e)
        return jsonify(
            {
                "code": 400,
                "message": "An submission record with this ID already exists.",
                "data": data
            }
        ), 400
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the submission record. " + str(e),
                "data": data
            }
        ), 500

    # convert a JSON object to a string and print
    print(json.dumps(pending.json(), default=str))
    print()

    return jsonify(
        {
            "code": 201,
            "message": "Request submission record created successfully",
            "data": pending.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5123, debug=True)
