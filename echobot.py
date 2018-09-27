from fbchat import log, Client
from fbchat.models import *
import os

class EchoBot(Client):

    def set_chats(self, chat_names):
        self.chat_IDs = []
        chats = self.fetchThreadList()
        for chat in chats:
            if chat.name in chat_names:
                self.chat_IDs.append(chat.uid)


    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        
        # only echo in Electronics (Gone Gorog)
        if thread_id in self.chat_IDs:

            # mark message as delivered and read
            self.markAsDelivered(thread_id, message_object.uid)
            self.markAsRead(thread_id)

            # log message info
            log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

            # if i'm not the author, echo the message back
            if author_id != self.uid:
                self.send(message_object, thread_id=thread_id, thread_type=thread_type)


if __name__ == '__main__':
    client = EchoBot(os.environ.get('fb_user'), os.environ.get('fb_pass'))
    client.set_chats('Electronics (Gone Gorog)')
    client.listen()

