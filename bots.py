from fbchat import log, Client
from fbchat.models import *
import os
import threading


class Bot(Client):

    def setChat(self, thread_id):
        thread = self.fetchThreadInfo(thread_id)[thread_id]
        self.thread_id = thread.uid
        self.thread_type = thread.type


class SpamBot(Bot):

    def setMessage(self, message):
        self.message = message


    def start(self):
        listen_thread = threading.Thread(target=self.listen, args=(), kwargs={})
        listen_thread.start()
        self.send(Message(text=self.message), thread_id=self.thread_id, thread_type=self.thread_type)


    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        
        if thread_id == self.thread_id:

            if author_id == self.uid:
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)
                log.info('{} sent to ID {}'.format(message_object.text, thread_id))
