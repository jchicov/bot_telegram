#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to send timed Telegram messages.

This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import random

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackContext, ConversationHandler
#from Ahorcado import *
import palabras
import random


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

JUGANDO, TYPING_REPLY, TYPING_CHOICE = range(3)


print(JUGANDO)
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola soy Chic0Bot, estoy aqui para servirte.')


imagen = ['\n \n \n| \n| ','\n| \n| \n| \n| ','___\n| |\n| \n| \n| ','___\n| |\n| o\n| \n| ','___\n| |\n| o\n| ^\n| ','___\n| |\n| o\n| ^\n| ^']

numim = 0

Num_le = random.randrange(len(palabras.palabras3))
p = palabras.palabras3[Num_le]
z = list(p)
#cuadro = []

def iniahor():
    print(p)
    cuadro = ['_' for i in range(len(p))]
    return cuadro
 





def include(Letra, cu):
    for i in range(z.count(Letra)):
        y = z.index(Letra)
        cu.pop(y)
        z.pop(y)
        z.insert(y, '')
        cu.insert(y, Letra)
    return cu
    return z







def echo(update: Update, context: CallbackContext) -> None:
    #Vamos a comprobar si la letra esta en la palabra
    update.message.reply_text(update.message.text)
    print(update.message.text)
    if update.message.text in p:
        include(update.message.text, cuadro)
        update.message.reply_text(cuadro)
    else:
        update.message.reply_text(imagen[numim])
        numim += 1






def ahor(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(str(iniahor()))
    return JUGANDO






























def fibo(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

def fiboo(update: Update, context: CallbackContext) -> None:
	user_name = update.message.from_user.first_name
	chat_id = update.message.chat_id
	msg = fibo(int(context.args[0]))
	update.message.reply_text(msg)
	print('El usuario', str(user_name), 'con id', str(chat_id), 'ha usado la función fibo')

def marginal(l):
	li = len(l)
	return l[li-1]

def Marginal(update: Update, context: CallbackContext) -> None:
	user_name = update.message.from_user.first_name
	chat_id = update.message.chat_id
	ms = marginal(context.args)
	update.message.reply_text(ms)
	print('El usuario', str(user_name), 'con el id', str(chat_id), 'ha usado la función marginal')


def Decide(opciones):
	b = []
	c = 0
	for x in opciones:
		if x.startswith(' '):
			print('Has puesto mas de un espacio despues de la coma')
			break
		else:
			b.append(x)
	c = len(b)
	return(b[random.randrange(c)])

def ls2str(ls): # Vamos a recibir una lista en el siguiente formato: ['hola', 'como', 'estas']
	c = ''
	for wrd in ls:
		if wrd == ls[0]:
			c += wrd
		else:
			c = c + ',' + wrd
	return(c)

def decide(update: Update, context: CallbackContext) -> None:
	user_name = update.message.from_user.first_name
	chat_id = update.message.chat_id
	ms = Decide(ls2str(context.args).split(','))
	update.message.reply_text(ms)
	print('El usuario', str(user_name), 'con el ID:', str(chat_id),', ha usado la función decide')


def fin(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "I learned these facts about you" "Until next time!")
    return ConversationHandler.END


def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1417065618:AAEwxjqUtJhpULy8AZrffnTDomVHhNdbX4k", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('ahorcado', ahor)],
        states={
            JUGANDO: [
                MessageHandler(Filters.text & ~Filters.command, echo),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Fin$'), fin)],
    )

    dispatcher.add_handler(conv_handler)
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("fiboo", fiboo, pass_args=True))
    dispatcher.add_handler(CommandHandler("marginal", Marginal))
    dispatcher.add_handler(CommandHandler("decide", decide))
    dispatcher.add_handler(CommandHandler("ahorcado", ahor))
    #dispatcher.add_handler(CommandHandler("help", start))
    #dispatcher.add_handler(CommandHandler("set", set_timer))
    #dispatcher.add_handler(CommandHandler("unset", unset))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
