from flask import Flask, url_for, render_template, request, Response, redirect, jsonify
from flask_static_compress import FlaskStaticCompress
from typing import Dict, List
import json
import datetime

divi_message_pos = 0
num_divi_messages = 0

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

@app.route('/reset', methods=["GET"])
def resetDIVI():
    global divi_message_pos
    divi_message_pos = 0
    return jsonify("Successful reset of DIVI", 200)


@app.route('/message', methods=['GET'])
def replyToMessage():
    global divi_message_pos
    global num_divi_messages
    try:
        divi_messages = readTransactionData("divisScript.json")
    except:
        print("There was an issue reading the message data")
        return jsonify(""), 500
    num_divi_messages = len(divi_messages) # Update the number of messages
    if num_divi_messages <= divi_message_pos:
        divi_message_pos = 0
        return jsonify("Divi is your financial companion!"), 200
    cur_message = divi_messages[divi_message_pos]
    divi_message_pos += 1
    return jsonify(cur_message), 200


def readTransactionData(fileName: str) -> List[Dict]:
    """Given the complete name of a JSON file such as johnsTransactions.json, this function finds the file and reads it
    in to a list of dictionary objecst and returns it, e.g.
    [{'time': '2020-01-31T23:48:36.969Z', 'value': 99.73, 'cardNum': 234567890, 'bank': 'RBC', 'merchant': 'No Frills',
     'description': 'Food'}]"""
    print("The filename is: ", fileName)
    try:
        with open("./static/data/" + fileName, 'r') as f:
            print("File successfully opened to read")
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


if __name__ == "__main__":
    # for i in range(20):
    #     reply = replyToMessage()
    #     print(reply)
    #existingTransactions = readTransactionData("ourScript.json")
    #writeTransactionData("junweisTransactions.json", existingTransactions)
    app.run(debug=True)
