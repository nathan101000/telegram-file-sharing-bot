from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from .handlers import start, button

async def main():
    """Main bot logic."""
    # Initialize the application with your bot token
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    
    # Start the bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
