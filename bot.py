import os
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext import filters

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Получаем токен из переменной окружения
token = os.getenv("BOT_TOKEN")
if not token:
    logger.error("Токен не задан. Убедись, что переменная окружения BOT_TOKEN установлена.")
    exit(1)  # Выход с кодом ошибки, если токен не найден

# ID администратора (замени на свой ID)
admin_id = "YOUR_ADMIN_ID"  # Замените на ваш ID

# Карты Таро
tarot_deck = [
    "0. Шут", "I. Маг", "II. Верховная Жрица", "III. Императрица", "IV. Император", "V. Иерофант",
    "VI. Влюбленные", "VII. Колесница", "VIII. Сила", "IX. Отшельник", "X. Колесо Фортуны",
    "XI. Справедливость", "XII. Повешенный", "XIII. Смерть", "XIV. Умеренность", "XV. Дьявол",
    "XVI. Башня", "XVII. Звезда", "XVIII. Луна", "XIX. Солнце", "XX. Суд", "XXI. Мир"
]

# Функция для получения случайного расклада
def tarot_reading():
    # Выбираем три случайные карты из колоды для расклада
    shuffled_deck = random.sample(tarot_deck, 3)
    return shuffled_deck

# Обработчик команды /start
async def start(update: Update, context):
    logger.info("Получена команда /start")
    await update.message.reply("Привет! Я твой Таро-бот. Пожалуйста, задай тему для расклада!")

# Обработчик команды /read
async def read_tarot(update: Update, context):
    logger.info("Запрашиваем расклад Таро")
    
    # Задаем тему для расклада (если пользователь указал текст)
    if context.args:
        topic = "Тема: " + " ".join(context.args)
    else:
        topic = "Тема не указана."
    
    # Получаем расклад
    cards = tarot_reading()
    
    # Формируем ответ
    reading_message = f"Ваш расклад Таро по теме: {topic}\n\n"
    for idx, card in enumerate(cards, 1):
        reading_message += f"Карта {idx}: {card}\n"

    # Отправляем расклад
    await update.message.reply(reading_message)

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
    application.add_handler(CommandHandler("start", start))  # Обработка команды /start
    application.add_handler(CommandHandler("read", read_tarot))  # Обработка команды /read для расклада Таро
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))  # Обработка текстовых сообщений

    logger.info("Бот запущен!")
    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
