from telegram import Update

from telegram.ext import Application,CommandHandler,ContextTypes

async def hello(update:Update,context:ContextTypes.DEFAULT_TYPE):
  await Update.massage.reply_text('hi madi')


app = ApplicationBuilder().token("telegram bot token").build()

app.add_handler(commandHandler('hello' , hello))

app.ran_polling()
