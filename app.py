import sys
from util.fetch_quote import fetch_quote
from util.db import get_mongo_conn
from flask import Flask, request, redirect
from util.db import load_result
from util.daily_quote import check_subscription, unsubscribe_user, resubscribe_user 
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms_reply", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    
    incoming_message = request.form['Body']
    incoming_number = request.form['From']
    
    check_subscription(incoming_number)
    
    if incoming_message.upper() == "STOP":
        unsubscribe_user(incoming_number)
        return ''
    elif incoming_message.upper() == "START":
        resubscribe_user(incoming_number)
        return ''
    else:
        result_quote = fetch_quote(incoming_message)
        load_result(result_quote, incoming_number, incoming_message)
        resp.message(result_quote)
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
    