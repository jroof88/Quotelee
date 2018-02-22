from flask import Flask, request, redirect, render_template
from util.db import load_result, get_mongo_conn
from util.fetch_quote import fetch_quote
from util.daily_quote import check_subscription, unsubscribe_user, resubscribe_user 
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms_reply", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    
    incoming_message = request.form['Body']
    incoming_number = request.form['From']
    
    check_subscription(incoming_number)
    
    blacklist_words = ["STOP", "STOPALL", "UNSUBSCRIBE", "CANCEL", "END", "QUIT"]
    start_words = ["START", "YES"]
     
    if incoming_message.upper() in blacklist_words:
        unsubscribe_user(incoming_number)
        return ''
    elif incoming_message.upper() in start_words:
        resubscribe_user(incoming_number)
        return ''
    else:
        result_quote_object = fetch_quote(incoming_message)
        load_result(result_quote_object, incoming_number, incoming_message)
        if(result_quote_object['author'] == "No Match"):
            resp.message(result_quote_object['quote'])
        else:
            resp.message(result_quote_object['quote'] + " - " + result_quote_object['author'])
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
    