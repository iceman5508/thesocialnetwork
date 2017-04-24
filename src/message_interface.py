'''
Created on Apr 18, 2017

@author: isaac
'''
import requests
import json
from server_interface import ServerInterface


class MessageInterface(ServerInterface):
    '''
 This is the messgaeinterface class The job of this class is to manage
 all services as it relates to personal messages.
    '''

    def __init__(self, user):
        """
 Like every other interface class in this application, the
messageinterface class assumes that authentication means have been taken
prior to the use of this interface.
 """
        self.base_url = 'http://nsommer.wooster.edu/social'
        self.user = user
        self.messages = list()

    def get_conversations(self):
        """
        gets all messages for the user
        if none found return none
        """
        data = {'uid': self.user.get_id(), 'token': self.user.get_token()}
        get = requests.get(self.base_url + '/conversations', data)
        return json.loads(get.text)

    def get_message(self, uid):
        """
        returns message with a specific user
        if none found return none
        :param uid: the user id to send message to
        """
        data = {'uid': self.user.get_id(), 'otherid': uid,
                'token': self.user.get_token(), 'limit': 50}

        get = requests.get(self.base_url + '/messages', data)
        message = json.loads(get.text)
        return message

    def send_message(self, to, body):
        """
        post/send a message towards another user
        :param to: The user the message is being sent to
        :param body: The content of the message
        """
        convo = list()
        convo.append(body)
        content = {'senderid': self.user.get_id(), 'recipientid': to,
                   'token': self.user.get_token(), 'content': convo}
        posts = requests.post(self.base_url + '/messages', content)
        message = json.loads(posts.text)
        return message

    def get_id(self):
        pass

    def rate_post(self):
        pass

    def post_id(self, id):
        pass

    def delete_post(self):
        pass

    def edit_post(self):
        pass

    def get_posts(self):
        pass

    def post_status(self):
        pass
