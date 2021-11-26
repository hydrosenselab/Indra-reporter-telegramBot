import json

import os
import re
import requests
import telebot

import inline_keys
from dotenv import load_dotenv
from inline_keys import confirm_markup, calamity_markup

load_dotenv()

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)
post_request_data ={}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, """Hello! Welcome to INDRA Reporting Bot.\nThis bot helps report natural events happening around you! 🌧️ ⛈️ ⚡""")
    bot.send_message(message.chat.id, """To report a disaster near you, type in /report to start the process""")

@bot.message_handler(commands=['report'])
def send_message(message):
    bot.send_message(message.chat.id, "Let's start the process!")
    bot.send_message(message.chat.id, "⚠️ Please be aware that the bot will need to collect your current location for accurately reporting the event!")
    bot.reply_to(message, "Click on the upload (📎) and click to share the location\nAnd then select 'Send My Current Location' option in that sub-menu")

@bot.message_handler(content_types=['location'])
def handle_location(message):
    bot.send_message(message.chat.id, "Thank you for sharing your location 📍")
    post_request_data['lat'] = message.location.latitude
    post_request_data['lon'] = message.location.longitude
    bot.send_message(message.chat.id, "Select the type of calamity you want to report", reply_markup=calamity_markup())

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    print(call.data)
    if call.data == "confirm":
        requests.post("https://indrareport.herokuapp.com/api/add/", data=json.dumps(post_request_data))
        bot.send_message(call.message.chat.id, "Thank you for your response!")
    elif "_" in call.data:
        print(call.data)
        post_request_data['description'] = call.data.split("_")[1]
        post_request_data['description_id'] = call.data.split("_")[0]
        post_request_data['obsval'] = 0.0
        bot.send_message(call.message.chat.id, "Tap confirm to submit the request", reply_markup=confirm_markup())
    elif re.match(r"[A-Za-z]+", call.data):
        post_request_data['category'] = str(call.data).capitalize()
        if call.data == "earthquake":
            bot.send_message(call.message.chat.id, "Thank you for submitting the report!")
        else:
            bot.send_message(call.message.chat.id, f"Select the type of {call.data} you want to report", reply_markup=getattr(inline_keys, f"{call.data}_markup")())
    print(post_request_data)
bot.infinity_polling()