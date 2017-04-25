from server_interface import ServerInterface
import json
import requests
from globals import GlobalData

base_url = 'http://nsommer.wooster.edu/social'


class PostMessageInterface(ServerInterface):
    """
    This class uses the ServerInterface class
    to deal with all services that are related
    to posting messages.
    """
    def __init__(self):
        pass

    def post_status(self, uid, content, token):
        """
        This method posts a status that the user has
        :param uid: the integer id of the user
        :param content: the content a user will post
        :param token: unique authentication for the user
        :return: the post id
        """
        response = requests.post(base_url+ '/posts', data={'uid': uid,
                                                'token': token,
                                                'parentid': -1,
                                                'content': content,
                                                })
        return response.status_code

    def get_posts(self, limit=50, uid=None, tag=None):
        """
        A method to get posts.

        :param limit: OPTIONAL. If passed, gets posts equal to the limit.
        :param uid: OPTIONAL. If passed, gets posts with only passed uid.
        :param tag: OPTIONAL. If passed, gets posts with only passed tag.
        :return: Posts. According to the parameters if provided. If not, 50
        posts having any or no tags and any uids.
        """
        data = {}
        data["limit"] = limit
        if uid is not None:
            data["uid"] = uid
        if tag is not None:
            data["tag"] = tag

        response = requests.get(base_url + '/posts', data)
        return json.loads(response.text)

    def edit_post(self, uid, token, post_id, content):
        """
        This method is used to edit a post
        that the user makes.
        :param uid: the integer id of the user
        :param token:  unique authentication for the user
        :param post_id: the integer id of the post
        :param content: the content a user will edit
        :return: ID of the edited post
        """
        response = requests.patch(base_url+ '/posts',data={'uid': uid,
                                                           'token': token,
                                                           'postid': post_id,
                                                           'content': content})
        return json.loads(response.text)

    def delete_post(self, uid, token, postid):
        """
        This method is used to delete posts
        :param uid: the integer id of the user
        :param token:  unique authentication for the user
        :param postid: the integer id of the post
        :return: ID of the deleted post
        """
        response = requests.delete(base_url+ '/posts', data={'uid': uid,
                                                             'token': token,
                                                             'postid': postid})
        return json.loads(response.text)

    def send_message(self, to, subject, body):
        pass

    def rate_post(self, postid, token, uid):
        get_response = requests.get(base_url + '/posts')
        posts_data = json.loads(get_response.text)
        data = {}
        data['uid'] = uid
        data['token'] = token
        for item in posts_data:
            if postid == item[u'postid']:
                data['postid'] = item[u'postid']
            else:
                continue
        requests.post(base_url + '/upvotes', data)

    def get_message(self, id):
        pass

    def get_id(self):
        pass

    def post_id(self, id):
        pass

if __name__ == "__main__":
    pass
