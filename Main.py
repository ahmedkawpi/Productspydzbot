import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "مرحبا بيك! 🇩🇿\n\n"
        "بوت اكتشاف المنتجات الرائجة في الجزائر.\n\n"
        "الأوامر المتاحة:\n"
        "/trending - المنتجات الرائجة\n"
        "/help - المساعدة\n\n"
        "البوت ما زال في مرحلة الإعداد."
    )

async def trending(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "قائمة المنتجات الرائجة قيد الإعداد.\n"
        "سنضيف مصادر البيانات في الخطوات القادمة."
    )

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "هذا البوت مخصص لاكتشاف الإعلانات "
        "والمنتجات الرائجة في السوق الجزائري."
    )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is not configured."
        )

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trending", trending))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
