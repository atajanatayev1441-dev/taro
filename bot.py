from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

# Токен бота и ID администратора
API_TOKEN = 'your_bot_token'  # Замените на ваш токен
ADMIN_ID = 'your_admin_id'    # Замените на ваш ID

# Начальная команда
def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Любовь", callback_data='love')],
        [InlineKeyboardButton("Карьера", callback_data='career')],
        [InlineKeyboardButton("Финансы", callback_data='finances')],
        [InlineKeyboardButton("Здоровье", callback_data='health')],
        [InlineKeyboardButton("Связаться с администратором", callback_data='contact_admin')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Привет! О чем вы хотите узнать?", reply_markup=reply_markup)

# Обработка нажатий на кнопки
def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'love':
        query.edit_message_text(text="Вы выбрали тему: Любовь. Какие вопросы у вас по любви?")
    elif query.data == 'career':
        query.edit_message_text(text="Вы выбрали тему: Карьера. Какие вопросы у вас по карьере?")
    elif query.data == 'finances':
        query.edit_message_text(text="Вы выбрали тему: Финансы. Какие вопросы вас интересуют?")
    elif query.data == 'health':
        query.edit_message_text(text="Вы выбрали тему: Здоровье. О чем вы хотите узнать?")
    elif query.data == 'contact_admin':
        send_to_admin("Пользователь хочет связаться с вами.")
        query.edit_message_text(text="Сообщение отправлено администратору. Ожидайте ответа.")

# Отправка сообщений админу
def send_to_admin(message):
    context.bot.send_message(chat_id=ADMIN_ID, text=message)

# Обработка загрузки архива
def handle_zip_file(update: Update, context):
    file = update.message.document
    file_name = file.file_name
    file_path = f'./downloads/{file_name}'
    file.download(file_path)
    send_to_admin(f"Пользователь отправил архив: {file_name}")
    update.message.reply_text(f"Файл {file_name} успешно загружен и отправлен админу.")

# Главная функция
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.document.mime_type("application/zip"), handle_zip_file))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
