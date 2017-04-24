from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from post_message import PostMessageInterface
from globals import GlobalData


class PostScreen(Screen):
    def post(self):
        content = self.ids.content.text
        uid = GlobalData._user_model.get_id()
        token = GlobalData._user_model.get_token()
        return PostMessageInterface.post_status(uid,token,content)


class NewsFeedScreen():
    def newsfeed(self):
        pass

scmanager = ScreenManager()
scmanager.add_widget(PostScreen(name='post'))


class PostuiApp(App):

    def build(self):
        return scmanager


if __name__ == '__main__':
    PostuiApp().run()
