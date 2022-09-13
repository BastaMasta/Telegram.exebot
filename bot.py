#Sum randum telegram bot

#==============================================================================================#
# just a disclaimer: if you want any changes to be made, like having the bot reply and get the
# username of th eppl who start the bot the ill have to re-structure the bot, cuz this is just
# some sub-stadard and a bit messy stuff i pulled off in a bit of a hurry
#
#   That's it.
# 																				-BastaMasta
#==============================================================================================#

# token = "5732142359:AAGmfjObY-0gvbw-zXFgARuhJjx83sInJgU"

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os

updater = Updater("5732142359:AAGmfjObY-0gvbw-zXFgARuhJjx83sInJgU", use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Weclom. (/help for help)")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("/run_out to run the [.exe] file")

def run_out(update: Update, context: CallbackContext):
	update.message.reply_text("executing command")
	os.startfile("shell.exe")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('run_out', run_out))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

print("The Bot is up and running!")

updater.start_polling()
