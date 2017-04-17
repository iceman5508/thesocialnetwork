import abc

class ServerInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_message(self):
        pass

    @abc.abstractmethod
    def post_message(self, content):
        pass

    @abc.abstractmethod
    def edit_message(self, content):
        pass

    @abc.abstractmethod
    def post_id(self,id):
        pass

    @abc.abstractmethod
    def get_id(self):
        pass

    @abc.abstractmethod
    def rate_post(self):
        pass