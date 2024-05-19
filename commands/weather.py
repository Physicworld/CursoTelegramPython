import requests
import telebot

def register_weather_commands(bot):
    @bot.message_handler(commands=['clima'])
    def clima(message):
        city = 'Mexico'
        latitude = 19.4326
        longitude = -99.1332
        response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true')
        data = response.json()
        print(data)
        current_weather = data['current_weather']
        temperature = current_weather['temperature']
        wind_direction = current_weather['winddirection']
        wind_speed = current_weather['windspeed']
        response = f'El clima en {city} es de {temperature}°C con direccion {wind_direction} y una velocidad del viento de {wind_speed} km/h.'
        bot.send_message(message.chat.id, response)