import telebot
import settings
from commands.greet import register_greet_commands
from commands.weather import register_weather_commands
from commands.payments import register_payment_commands
from commands.media import register_media_commands
from commands.save_message import register_save_message_command
from data.database import init_db

# Inicializar bot
bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

# Inicializar base de datos
conn, c = init_db()

# Registrar comandos
register_greet_commands(bot)
register_weather_commands(bot)
register_payment_commands(bot)
register_media_commands(bot)
register_save_message_command(bot, conn, c)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Iniciar el bot
bot.infinity_polling()
