import abc


class ServerInterface:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_message(self, id):
        pass

    @abc.abstractmethod
    def get_posts(self, limit, tag):
        pass

    @abc.abstractmethod
    def send_message(self, to, subject, body):
        pass

    @abc.abstractmethod
    def post_status(self, uid, content, token):
        pass

    @abc.abstractmethod
    def edit_post(self, uid, token, postid, content):
        pass

    @abc.abstractmethod
    def delete_post(self, uid, token, postid):
        pass

    @abc.abstractmethod
    def post_id(self,id):
        pass

    @abc.abstractmethod
    def get_id(self):
        pass

    @abc.abstractmethod
    def rate_post(self, postid, token, uid):
        pass