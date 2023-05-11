from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date

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
    lastUpdateTime = db.Column(db.Date, nullable=False)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
