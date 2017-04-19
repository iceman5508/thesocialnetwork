'''
Created on Apr 18, 2017

@author: isaac
'''
from server_interface import ServerInterface
from datetime import datetime

class MessageInterface(ServerInterface):
    '''
    This is the messgaeinterface class
    The job of this class is to manage 
    all services as it relates to personal
    messages.
    '''


    def __init__(self, user_id):
        """
        Like every other interface class in 
        this application, the messageinterface class
        assumes that authentication means have been taken
        prior to the use of this interface. The default
        constructor takes in the user_id and builds the message 
        service around that.          
        """
       
        self.uid = user_id
        self.messages = list()
        self.get_all_messages()
        
        
        
    
    def get_all_messages(self):
        """
        gets all messages for a specific user
        f none found return none
        """
        
        server_response  = {}
        for message in server_response:
            if self.uid in message['owners']:
                self.messages.append(message)
            else:
                return None
        return None
            
    
    def get_message_with(self, uid): 
        """
        returns message with a specific user
        if none found return none
        """
        for message in self.messages:
            if uid in message['owners']:
                return message
            else:
                return None
        return None
    
    
    def get_message(self, id):
        """
        returns message with a specific id
        if none found return none
        """
        for message in self.messages:
            if message['id'] is id:
                return message
        return None
    
    
    def post_message(self, to, subject, body):
        """
        post/send a message towards another user
        the message should take the form:
        {
            owners:
            sender:
            id:
            timestamp:
            subject:
            body          
        }        
        """
        content = {'owners': [self.uid, to], 'id': 1, 
                   'sender' : self.uid, 'timestamp': datetime.now(),
                   'subject': subject, 'body' : [body] }
        return content
        
        #add message to server
    
    def response_message(self,body, id):
        """
        Handles response to messages
        """
        
        message = self.get_message(id)
        content = {'sender' : self.uid, 'timestamp': datetime.now(), 
                   'body' : body }
        message['body'].append(content)
        
        #update message on server
    
    def delete_message(self, id):
        """
        deletes messages
        """
        message = self.get_message(id)
        for m_id in message['owners']:
            if m_id is self.uid:
                del m_id
                #update messgae on server
        del message 
                
        
    
    def edit_message(self, id, content):
        pass
    
    
    def get_id(self):
        pass   
    
    
    def rate_post(self):
        pass
    
    def post_id(self,id):
        pass
        
    
        
if __name__ == "__main__":
    user = MessageInterface(1) 
    print user.post_message(2, "Yo", "hi nice to meet you 2")
             
        
        
        
        
        
        
          
        
        
        
    
    
       
        