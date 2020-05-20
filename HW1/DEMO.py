import requests
import configparser
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup

from fugle_realtime import intraday
from idea.func import Func

config = configparser.ConfigParser()
config.read('config.ini')

access_token = config['TELEGRAM']['ACCESS_TOKEN']
webhook_url = config['TELEGRAM']['WEBHOOK_URL']

requests.post('https://api.telegram.org/bot'+access_token+'/deleteWebhook').text
requests.post('https://api.telegram.org/bot'+access_token+'/setWebhook?url='+webhook_url+'/hook').text

app = Flask(__name__)

bot = telegram.Bot(token=config['TELEGRAM']['ACCESS_TOKEN'])
func = Func()

morning = '早安~您好！\n'\
         '若要查詢各產業的股票代碼，請輸入【產業查股】\n'\
         '若要查詢股票代碼的相關資訊，請輸入【股票代碼查詢】\n'\


morning_button = ReplyKeyboardMarkup([['產業查股'],['股票代碼查詢']],
                                     one_time_keyboard = True,
                                     selective = True)

@app.route('/hook', methods=['POST'])

def webhook_handler(): 
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'

def morning_handler(bot, update):
    update.message.reply_text(morning, reply_markup = morning_button)

def industry_handler(bot, update): 
    text = update.message.text   
    reply = func.maim(text)
    update.message.reply_text(reply)
    
# This class dispatches all kinds of updates to its registered handlers.
dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(CommandHandler('morning', morning_handler))
dispatcher.add_handler(MessageHandler(Filters.text, industry_handler)) 


if __name__ == '__main__':
    app.run()