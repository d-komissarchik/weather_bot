import telebot
import requests
import json


bot = telebot.TeleBot('5356962954:AAGpPLeRTCf5ZEknWMeQlv87y8DGR86YdFY')
API = '121d7581fe449714c646b6adc6e855f9'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello. Enter the name of the city: ')