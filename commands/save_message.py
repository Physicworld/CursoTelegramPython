import sqlite3
import telebot

def register_save_message_command(bot, db_conn, db_cursor):
    @bot.message_handler(commands=['save'])
    def save_message(message):
        # Create a new connection and cursor in the same thread
        conn = sqlite3.connect('bot.db')
        c = conn.cursor()

        user_id = message.from_user.id
        user_message = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ''
        c.execute('INSERT INTO messages (user_id, message) VALUES (?, ?)', (user_id, user_message))
        conn.commit()
        bot.send_message(message.chat.id, "¡Tu mensaje ha sido guardado!")

        # Close the connection
        conn.close()