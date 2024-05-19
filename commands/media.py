import telebot

def register_media_commands(bot):
    @bot.message_handler(commands=['foto'])
    def send_photo(message):
        photo = open('resources/test_image.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    @bot.message_handler(commands=['video'])
    def send_video(message):
        video = open('resources/test_video.mp4', 'rb')
        bot.send_video(message.chat.id, video)
