from flask import Flask, url_for, render_template, request, Response, redirect, jsonify
from flask_static_compress import FlaskStaticCompress
from typing import Dict, List
import json
import datetime

app = Flask(__name__)
app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
app.config['COMPRESSOR_OUTPUT_DIR'] = 'build'
app.static_folder = 'static'
compress = FlaskStaticCompress(app)


@app.route('/', methods=['GET'])
def home():
    """Landing page."""
    print("Reached base redirect")
    return redirect(url_for('static', filename='index.html'))


@app.route('/launchDivi', methods=['GET'])
def launchDivi():
    return redirect(url_for('static', filename='chatbot.html'))


def readTransactionData(fileName: str) -> List[Dict]:
    """Given the complete name of a JSON file such as johnsTransactions.json, this function finds the file and reads it
    in to a list of dictionary objecst and returns it, e.g.
    [{'time': '2020-01-31T23:48:36.969Z', 'value': 99.73, 'cardNum': 234567890, 'bank': 'RBC', 'merchant': 'No Frills',
     'description': 'Food'}]"""
    try:
        with open("./static/data/" + fileName, 'r') as f:
            json_text = f.read()
    except:
        print("There was an invalid file name provided.")
        return []
    transactions = json.loads(json_text)
    #print(transactions)
    #print(type(transactions))
    return transactions


def writeTransactionData(fileName: str, data: List ) -> None:
    """Given the completes"""
    jsonfied = json.dumps(data)
    print(jsonfied)

    try:
        with open("./static/data/" + fileName, 'w') as f:
            print("Open success")
            f.write(jsonfied)
    except:
        print("There was an invalid file name provided.")
        return

def analyzeTransactionData(clientData: List[Dict], similarClients: List[List[Dict]]) -> Dict:
    """Given an object representing the client's transactions, and an list containing elements representing transactions
     of similar clients, this function outputs an object representing predictions for the client's future spending."""

    #Part 1: Analyze the client's own behavior
    #x = datetime.datetime("2020-01-31T23:48:36.969Z")
    #print(x)


if __name__ == "__main__":
    existingTransactions = readTransactionData("johnsTransactions.json")
    writeTransactionData("junweisTransactions.json", existingTransactions)
    analyzeTransactionData([], [])
    app.run(debug=True)
