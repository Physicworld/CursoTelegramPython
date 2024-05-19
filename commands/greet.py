import telebot

def register_greet_commands(bot):
    @bot.message_handler(commands=['saludar'])
    def greet_user(message):
        parts = message.text.split()
        if len(parts) > 1:
            name = parts[1]
            response = f'Hola {name}!'
        else:
            response = 'Por favor, proporciona un nombre despues del comando /saludar.'
        bot.send_message(message.chat.id, response)
