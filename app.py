import sys
from util.fetch_quote import fetch_quote
from flask import Flask, request, redirect
from util.db import load_result
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms_reply", methods=['GET', 'POST'])
def sms_reply():
    print("SMS Function Is Called")
    resp = MessagingResponse()
    incoming_message = request.form['Body']
    incoming_number = request.form['From']
    print(incoming_number)
    result_quote = fetch_quote(incoming_message)
    load_result(result_quote, incoming_number, incoming_message)
    resp.message(result_quote)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
    