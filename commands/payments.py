from telebot import types

def register_payment_commands(bot):
    @bot.message_handler(commands=['buy'])
    def show_buy_button(message):
        keyboard = types.InlineKeyboardMarkup()
        buy_button = types.InlineKeyboardButton(text="Comprar Producto", callback_data="buy")
        keyboard.add(buy_button)
        bot.send_message(message.chat.id, "¿Deseas comprar el producto?", reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data == "buy")
    def callback_buy(call):
        product_price = types.LabeledPrice(label="Producto", amount=500)  # Precio en centavos (500 = $5.00)
        bot.send_invoice(
            chat_id=call.message.chat.id,
            title="Compra de Producto",
            description="Descripción del producto.",
            invoice_payload="custom-payload-buy-product",
            provider_token='YOUR_PAYMENT_PROVIDER_TOKEN',
            currency="USD",
            prices=[product_price],
            start_parameter="product-purchase"
        )

    @bot.pre_checkout_query_handler(func=lambda query: True)
    def checkout_process(pre_checkout_query):
        bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

    @bot.message_handler(content_types=['successful_payment'])
    def got_payment(message):
        bot.send_message(message.chat.id, "¡Gracias por tu compra! Pronto recibirás tu producto.")
        bot.send_message(message.chat.id, "Si tienes algún problema, por favor contacta a soporte: /ayuda")
        bot.send_message(message.chat.id, "Si deseas comprar otro producto, por favor presiona /start")
