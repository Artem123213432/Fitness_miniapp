import os
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем токен бота
TOKEN = "8103057357:AAGBjL_XhBBN5m0LTLzd1Jbcgi8uqFQ8XCw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "Привет! Нажмите на кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup={
            "inline_keyboard": [[
                {
                    "text": "Открыть мини-приложение",
                    "web_app": {"url": "https://your-github-username.github.io/Fitness_miniapp/"}
                }
            ]]
        }
    )

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main() 