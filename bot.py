from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler
from telegram.ext import filters

# Токен бота (замени на свой)
token = "8497922798:AAEG279iUN_Ww365xayiTnVYZYCUuOiaJMA"
# ID администратора (замени на свой ID)
admin_id = "8283258905"

# Пример команды для старта
async def start(update: Update, context):
    await update.message.reply("Привет! Я твой Таро-бот!")

# Пример обработки текста (не команды)
async def handle_text(update: Update, context):
    text = update.message.text
    await update.message.reply(f"Ты написал: {text}")

# Основная функция для запуска бота
def main():
    # Создание приложения (замена Updater на Application)
    application = Application.builder().token(token).build()

    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))

    # Регистрация обработчика текстовых сообщений (не команд)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
