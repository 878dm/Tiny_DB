from tinydb import TinyDB 
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update
from tinydb.database import Document
import telegram
import json
db = TinyDB('db.json')

TOKEN = '5549407151:AAGVaQx5L2bvwBYnZE3a50yycdBQfPvl1fo'
updater = Updater(TOKEN)

def start(update:Update,context:CallbackContext):
    chat_id = update.message.chat.id
    bot = context.bot 
    bot.sendMessage(chat_id,"Welcome")

def main(update:Update, context:CallbackContext):
    text = update.message.text
    chat_id = update.message.chat.id
    first_name = update.message.chat.first_name
    with open('db.json','r') as f:
        data = f.read() 
        if data == "":
            data = "{}"
        data_users = json.loads(data)
    
    ids1 = data_users.get('_default')
    if ids1 !=None:
        ids = list(ids1.keys())[-1]
        doc = Document(value={'name':f'{first_name}','text':f'{text}'},doc_id=int(ids)+1)
        db.insert(doc)
    else:
        ids=0
        doc = Document(value={'name':f'{first_name}','text':f'{text}'},doc_id=ids)
        db.insert(doc)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,main))

updater.start_polling()
updater.idle()

# db.insert({'user_id':5,'username':'User1'})
