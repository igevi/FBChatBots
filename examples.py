from fbchat import log, Client
from fbchat.models import *
from bots.spamBot import SpamBot
import os

user = os.environ.get('fb_user')
passw = os.environ.get('fb_pass')


# Example SpamBot usage ####
bot = SpamBot(user, passw)
bot.setChat(bot.searchForUsers('James Maclachlan')[0].uid)
bot.setMessage('test')
bot.start()
############################