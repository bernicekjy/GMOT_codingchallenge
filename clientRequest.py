from flask import Flask, request, jsonify, render_template
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

@app.route('/')
def my_route():
    my_value = ""
    return render_template('clientRequest.html', value=my_value)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # if request.method == 'POST':
    # clientID = request.form['clientID']
    # commissionDiff = request.form['commissionDifference']
    # grossAmountDiff = request.form['grossAmountDifference']

    clientID = request.form.get('clientID')
    commissionDiff = request.form.get('commissionDifference')
    grossAmountDiff = request.form.get('grossAmountDifference')
    clientFound = Client.query.filter_by(clientID=clientID).first()

    if not len(clientFound):
        ans='ClientID not found.'

    if commissionDiff>clientFound.commission: #commission difference out of tolerance
        ans='Commission difference is out of tolerance.'
    elif grossAmountDiff>clientFound.grossAmount:
        ans='Gross amount is out of tolerance.'
    else:
        ans='Successful: Commission difference and gross amount are within setup tolerance'

    return render_template('clientRequest.html', value=ans)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
