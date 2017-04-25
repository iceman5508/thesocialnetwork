'''
Created on Apr 22, 2017

@author: isaac
'''
from user_login import UserData
from Screens import Screens

class GlobalData():
    """
    This class makes the transfer of data 
    between different parts of the application
    easier. 
    """

    #keep track of current conversation
    _current_convo = None

    # keep track of current post IDs displayed on the feed
    current_post_ids = []

    _user_model = UserData()
    
    #this should be changed once login screen is done
    #_user_model.login(21, "Parrot", "sguwsicp")
    
    #keep track of screen manager
    _scmanager = Screens._manager
    
    
    """
    Interact with the
    user class to log user in
    :param uid: the id of the user to be logged in
    :param username: the username of the usert to be logged in
    :param token: the token of the user to be logged in
    """
    def login(self, uid, username, token):
        GlobalData._user_model.login(uid, username, token)