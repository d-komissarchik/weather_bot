import telebot
import requests
import json


bot = telebot.TeleBot('')
API = '121d7581fe449714c646b6adc6e855f9'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello. Enter the name of the city: ')


#декоратором проверяем что пользователь отправил имено текс, если да, то срабатывает ф-ия
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower() #удаляем пробелы и переводим в нижний регистр
    show_city = city.title()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:#проверяем введен ли правильно город
        data = json.loads(res.text)#получаем текст с джейсон и теперь можем добраться до его атрибутов(main, temp)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Now temperature in {show_city}: {temp}°')
        #переменная хранит разное изображение в зависимости от текущей погоды
        image = 'sunny.png' if temp > 5.0 else 'clouds.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Incorrect name of  city - {show_city}')




bot.polling(none_stop=True)