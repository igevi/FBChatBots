from fbchat import log, Client
from fbchat.models import *
import threading


class Bot(Client):

    def setChat(self, thread_id):
        thread = self.fetchThreadInfo(thread_id)[thread_id]
        self.thread_id = thread.uid
        self.thread_type = thread.type
