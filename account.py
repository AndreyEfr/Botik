from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pprint import pprint
import json
import datetime
TOKEN = '5189332828:AAFItsEfTsTLycNDcUfDHffpYAtSSCxpdQw'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
print('Bot started.')
def start(update, context):
    chat = update.effective_chat
    a = 'hello, welcome to calculator bot input /c and write an equation with spaces (like /c 1 + 1)' \
        'operators are: +  -  *  /  //(integer division) %(remainder) **(degree)'
    context.bot.send_message(chat_id=chat.id, text=a)

def calc_hist(s, b,action):
    l = str(datetime.datetime.now())
    memory_json =[
    {
        '1 numb':s,
        '2 numb':b,
        'action': action,
        'time': l
    }]
    with open("hist.json","a")as f:
        json.dump(memory_json, f, indent= 3)
    

def ca(s, b, action):
    if action == "+":
        print(s + b)
        f = s + b
    elif action == "-":
        print(s - b)
        f = s - b
    elif action == "*":
        print(s * b)
        f = s * b
    elif action == "/":
        print(s / b)
        f = s / b
    elif action == "//":
        f = s // b
        print(s // b)
    elif action == "%":
        print(s % b)
        f = s % b
    elif action == "**":
        print(s ** b)
        f = s ** b

    else:
        return "error"
    return f

def ma(update, context):
    chat = update.effective_chat
    l = update.message.text
    try:
        a, b, c, d = l.split()
    except ValueError:
        context.bot.send_message(chat_id=chat.id, text='invalid equation')
        return
    if b.isdigit():
        v = float(b)
    else:
        context.bot.send_message(chat_id=chat.id, text='invalid equation')
    if d.isdigit():
        n = float(d)
    else:
        context.bot.send_message(chat_id=chat.id, text='invalid equation')
    f = calc_hist(v, n, c)
    g = ca(v, n, c)
    context.bot.send_message(chat_id=chat.id, text=g)
    context.bot.send_message(chat_id=chat.id, text=f)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('c', ma))
updater.start_polling()
updater.idle()