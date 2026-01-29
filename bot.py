import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext import filters

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Получаем токен из переменной окружения
token = os.getenv("BOT_TOKEN")  # Токен будет подтягиваться из переменной окружения на Railway
if not token:
    logger.error("Токен не задан. Убедись, что переменная окружения BOT_TOKEN установлена.")
    exit(1)

# ID администратора (замени на свой ID)
admin_id = "YOUR_ADMIN_ID"

# Обработчик команды /start
async def start(update: Update, context):
    logger.info("Получена команда /start")
    await update.message.reply("Привет! Я твой Таро-бот!")

# Обработчик текстовых сообщений
async def handle_text(update: Update, context):
    text = update.message.text
    logger.info(f"Получено текстовое сообщение: {text}")
    await update.message.reply(f"Ты написал: {text}")

# Основная функция для запуска бота
def main():
    # Создание приложения
    application = Application.builder().token(token).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    logger.info("Бот запущен!")
    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
