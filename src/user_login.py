from server_interface import ServerInterface
import requests
import json


def get_uname(uinfo):
    return uinfo['username']


def get_uid(uinfo):
    return uinfo['uid']


def get_utoken(uinfo):
    return uinfo['token']

class UserData(ServerInterface):
    """
    This class stores the user data and has functions that let's the user
    interact with the access to his account.
    """
    
    def __init__(self):
        # The data will be stored in a dictionary in the object.

        self.info = {}
        self.base_url = 'http://nsommer.wooster.edu/social'

    def get_id(self):
        return self.info['uid']

    def get_username(self):
        return self.info['username']

    def get_token(self):
        return self.info['token']

    def register(self, new_user):
        """
        Uploads a username and returns the new user information.
        After registering the user is automatically logged in.
        :param new_user: New user name.
        :return: Returns the new user information as a dictionary.
        """
        posts = requests.post(self.base_url + '/users',
                              data={'username': new_user})
        json_info = json.loads(posts.text)
        self.info = json_info
        return self.info

    def login(self, uid, username, token):
        """
        Logs in the user given the id or username input is right.
        Also stores the information in the object parameters.
        Note: If the token is wrong no error will be shown until the user
        tries to edit a post or change username.

        :param uid: User Id.
        :param username: Username.
        :param token: Token.
        :return: Returns the user information as a dictionary.
        """
        response = requests.get(self.base_url + '/users', data={'uid': uid})
        user_info = json.loads(response.text)
        if uid is user_info['uid']:
            if username == user_info['username']:
                self.info = user_info
                self.info['token'] = token
                return self.info
            else:
                return 'Error'
        else:
            return 'Error'

    def change_username(self, uid, new_username, token):
        """
        Changes the username given the input contains ID, username and token
        of the right user. In case one of them is wrong an error message
        will be returned.

        :param uid: User ID.
        :param new_username: New username.
        :param token: Token.
        :return: Returns the new user information.
        """
        response = requests.patch(self.base_url + '/users',
                                  data={'uid': uid, 'username': new_username,
                                        'token': token})
        if response.status_code == 200:
            changed_info = json.loads(response.text)
            user_data = requests.get(self.base_url + '/users',
                                     data={'uid': uid})
            user_info = json.loads(user_data.text)
            if token == changed_info['token']:
                if uid is changed_info['uid']:
                    if new_username == user_info['username']:
                        self.info = changed_info
                        return self.info
                    else:
                        return 'Error'
                else:
                    return 'Error'
            else:
                return 'Error'
        else:
            return 'Error'
    
    def get_user(self, username):
        """
        Grabs a specific user based on the username
        given
        
        :param username: name of the user requested
        :return: returns the user information
        """
        response = requests.get(self.base_url + '/users', data={'username': username})
        if response.status_code is 200:
            return json.loads(response.text)
        else:
            return None
       
        

    def get_message(self, id):
        pass

    def post_message(self, to, subject, body):
        pass

    def edit_message(self, id, content):
        pass

    def post_id(self, id):
        pass

    def rate_post(self):
        pass
    
    def delete_post(self):
        pass
    
    def edit_post(self):
        pass
    def get_posts(self):
        pass
    def post_status(self):
        pass 
    
    def send_message(self):
        pass
