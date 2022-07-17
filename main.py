import re

import requests
import telebot

from config import BOT_TOKEN
from funcs import getStories


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "send instagram username to download stories\nexample: `@instagram`", parse_mode="MARKDOWN")


@bot.message_handler(regexp="(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)")
def handle_message(message):
	
    storyList = getStories(message.text.replace('@', ''))
    
    if storyList == 404:
       	bot.reply_to(message, "account not found", parse_mode="MARKDOWN") 
    elif storyList == 400:
        bot.reply_to(message, "there are no stories", parse_mode="MARKDOWN") 
    else:
        for strory in storyList:
            if strory['type'] == 'photo':
                bot.send_photo(message.chat.id, strory['media'])
            elif strory['type'] == 'video':
                bot.send_video(message.chat.id, strory['media'])

bot.polling()