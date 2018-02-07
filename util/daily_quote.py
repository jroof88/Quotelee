import os
import time
from datetime import datetime
from pytz import timezone
from twilio.rest import Client
from db import get_collection, get_documents

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
authorization_token = os.environ["TWILIO_AUTH_TOKEN"]
twilio_phone_number = os.environ["TWILIO_PHONE_NUMBER"]
client = Client(account_sid, authorization_token)

def send_daily_quote():
    quote = get_random_quote()
    full_quote = quote['quote'] + " - " + quote['author']
    
    users = get_documents("quotelee", "test_user")
    for user in users:
        if(user["status"] == "active"):
            client.messages.create(to=user["phoneNo"], from_=twilio_phone_number, body=full_quote)
    
    currDateTime = datetime.now(timezone('US/Pacific')).strftime('%m-%d-%Y %H:%M')
    numberOfUsers = users.count()
    daily_quotes = get_collection("quotelee", "daily_quotes")
    daily_quotes.insert({
        "quote": quote['quote'],
        "author": quote['author'],
        "datetime": currDateTime,
        "numberOfUsers": numberOfUsers
    })

def get_random_quote():
    quote_collection = get_collection("quotelee", "quotes")
    random_quote = quote_collection.aggregate(
        [{'$sample':{'size':1}}]
    )
    
    for quote in random_quote:
        return quote
    
def check_subscription(phoneNumber):
    user_collection = get_collection("quotelee", "users")
    user = user_collection.find({"phoneNo": phoneNumber})
    if user.count() == 0:
        add_user(phoneNumber)

def add_user(phoneNumber):
    user_collection = get_collection("quotelee", "users")
    user_collection.insert({
        "phoneNo": phoneNumber,
        "status": "active"
    })
    send_welcome_message(phoneNumber)
    
def send_welcome_message(phoneNumber):
    mesg = "Hi I'm Quotelee! You are now subscribed to recieve daily quotes. If one a day isn't enough, text me a topic, person, or anything and I'll reply with a relevant quote to hopefully better your day! Text STOP at any time to unsubscribe."
    client.messages.create(to=phoneNumber, from_=twilio_phone_number, body=mesg)
    
def unsubscribe_user(phoneNumber):
    user_collection = get_collection("quotelee", "users")
    user_collection.update_one(
        {"phoneNo": phoneNumber},
        { "$set": {
            "status": "inactive"
        }
    })
    
def resubscribe_user(phoneNumber):
    user_collection = get_collection("quotelee", "users")
    user_collection.update_one({
        "phoneNo": phoneNumber},
        { "$set": {
            "status": "active"
        }
    })
    send_resubscribe_message(phoneNumber)

def send_resubscribe_message(phoneNumber):
    mesg = "Welcome back! Enjoy your daily quote and remember you can text me a topic or historial figure for a quote!"
    client.messages.create(to=phoneNumber, from_=twilio_phone_number, body=mesg)
        