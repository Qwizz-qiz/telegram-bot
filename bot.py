from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8532195297:AAFM92ig8QBj_McFR8d-37Pw0HZgor6lxDQ"
GROUP_ID = -1003426813973

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await context.bot.forward_message(
            chat_id=GROUP_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()
