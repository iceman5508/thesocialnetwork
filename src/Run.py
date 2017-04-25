# NOTE: I took help from http://stackoverflow.com/questions/42820798/how-
# to-add-background-colour-to-a-label-in-kivy
# and https://groups.google.com/forum/#!topic/kivy-users/JInL3VyFHS0
# for this.

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from globals import GlobalData
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from message_ui import MessageScreen
from new_message_ui import ComposeScreen
from post_screen import FeedScreen, PostScreen


def popup_error():
    """
    Creates a popup widget if an error is encountered while trying to access
     the url.
    """
    content = BoxLayout(orientation='vertical')
    message_label = Label(text='Wrong information')
    dismiss_button = Button(text='Dismiss')
    content.add_widget(message_label)
    content.add_widget(dismiss_button)
    popup = Popup(title='Error', content=content, size_hint=(0.3, 0.25))
    dismiss_button.bind(on_release=popup.dismiss)
    popup.open()

Builder.load_string("""
<LoginScreen>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Login information'
            font_size: 30
            bold: 1
            italic: 1
            color: 1, 0.2, 0.2, 0.8
            canvas.before:
                Color:
                    rgba: 0, 0.3, 0.5, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
        TextInput:
            id: username
            hint_text: 'Enter username here'
            foreground_color: 1,1,1,1
            hint_text_color: 0.2, 0.5, 0.7, 0.7
            background_color: 0, 0.3, 0.5, 0.4
            write_tab: 0
            cursor_color: 1,1,1,1
        TextInput:
            id: uid
            hint_text: 'Enter your id here'
            foreground_color: 1,1,1,1
            hint_text_color: 0.2, 0.5, 0.7, 0.7
            background_color: 0, 0.3, 0.5, 0.4
            write_tab: 0
            cursor_color: 1,1,1,1
        TextInput:
            id: token
            hint_text: 'Enter your token here'
            foreground_color: 1,1,1,1
            hint_text_color: 0.2, 0.5, 0.7, 0.7
            background_color: 0, 0.3, 0.5, 0.4
            write_tab: 0
            cursor_color: 1,1,1,1
        Button:
            id: login
            text: 'Submit'
            background_color: 0.5,0.5,0.5,0.5
            bold: 1
            on_release: root.user_login()
        Label:
            text: 'New to the app?'
            font_size: 30
            bold: 1
            italic: 1
            color: 1, 0.2, 0.2, 0.8
            canvas.before:
                Color:
                    rgba: 0, 0.3, 0.5, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
        Button:
            id: register
            text: 'Register'
            on_release: root.manager.current = 'register'
            background_color: 0.5,0.5,0.5,0.5
            bold: 1
        Button:
            text: 'Exit'
            background_color: 0.5,0.5,0.5,0.5
            bold: 1
            on_release: app.stop()

<RegisterScreen>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Register information'
            font_size: 30
            bold: 1
            italic: 1
            color: 1, 0.2, 0.2, 0.8
            canvas.before:
                Color:
                    rgba: 0, 0.3, 0.5, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
        TextInput:
            id: new_username
            hint_text: 'Write your new username here'
            foreground_color: 1,1,1,1
            hint_text_color: 0.2, 0.5, 0.7, 0.7
            background_color: 0, 0.3, 0.5, 0.4
            write_tab: 0
            cursor_color: 1,1,1,1
        Button:
            id: register_user
            text: 'Register'
            on_release: root.user_register()
            background_color: 0.5,0.5,0.5,0.5
            bold: 1
        Button:
            text: 'Return'
            on_release: root.manager.current = 'login'
            background_color: 0.5,0.5,0.5,0.5
            bold: 1

<MainScreen>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: ''
            id: welcome_text
            font_size: 30
            bold: 1
            underline: 1
            color: 1, 0.2, 0.2, 0.8
            canvas.before:
                Color:
                    rgba: 0, 0.3, 0.5, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
        Label:
            text: ''
            id: user_info
            font_size: 22
            italic:
            color: 1, 0.2, 0.2, 0.8
            canvas.before:
                Color:
                    rgba: 0, 0.3, 0.5, 0.2
                Rectangle:
                    pos: self.pos
                    size: self.size
        Button:
            text: 'Messages'
            on_release: root.manager.current = 'messages'
            background_color: 0.5,0.5,0.5,0.5
            bold: 1
        Button:
            text: 'Feeds'
            on_release: root.manager.current = 'fscreen'
            background_color: 0.5,0.5,0.5,0.5
            bold: 1
        Button:
            text: 'Logout'
            on_release: root.manager.current = 'login'
            background_color: 0.5,0.5,0.5,0.5
            bold: 1

""")


class LoginScreen(Screen):
    """
    This class helps in building the Login Screen.
    """

    def user_login(self):
        """
        The function for logging in users.
        :return: nothing
        """
        user_name = self.ids.username.text
        user_id = self.ids.uid.text
        user_token = self.ids.token.text
        GlobalData._user_model.login(int(user_id), user_name, user_token)
        if GlobalData._user_model.login(int(user_id), user_name, user_token) \
                == 'Error':
            popup_error()
        else:
            self.manager.get_screen('mainsc').update_text_login()
            
            '''message screen'''
            message = MessageScreen("messages")
            message.on_init()

            '''new message screen'''
            new_message = ComposeScreen("new_messages")
            new_message.on_init()
            
            '''feeds'''
            scmanager.add_widget(FeedScreen(name='fscreen'))
            scmanager.add_widget(PostScreen(name='post'))
        
            scmanager.current = 'mainsc'


class RegisterScreen(Screen):
    """
    This class helps in building the Register Screen.
    """

    def user_register(self):
        """
        The function to register new users.
        :return: nothing
        """
        new_username = self.ids.new_username.text
        user_info = GlobalData._user_model.register(new_username)
        uname = GlobalData._user_model.get_username()
        uid = GlobalData._user_model.get_id()
        utoken = GlobalData._user_model.get_token()
        GlobalData._user_model.login(uid, uname, utoken)
        self.manager.get_screen('mainsc').update_text_register()
        
        '''message screen'''
        message = MessageScreen("messages")
        message.on_init()

        '''new message screen'''
        new_message = ComposeScreen("new_messages")
        new_message.on_init()
        
        '''feeds'''
        scmanager.add_widget(FeedScreen(name='fscreen'))
        scmanager.add_widget(PostScreen(name='post'))
        scmanager.current = 'mainsc'


class MainScreen(Screen):
    """
    This class helps in building the Main Screen.
    """

    def update_text_register(self):
        """
        The function to update the text on the Main Screen after registering
        new users.
        :return: nothing
        """
        uname = GlobalData._user_model.get_username()
        uid = GlobalData._user_model.get_id()
        utoken = GlobalData._user_model.get_token()
        self.ids.user_info.text = 'Username: ' + uname + '\n' + 'ID: ' \
                                      + str(uid) + '\n' + 'Token: ' + utoken
        self.ids.welcome_text.text = 'Welcome ' + uname

    def update_text_login(self):
        """
        The function to update the text on the Main Screen after an user logs
        in.
        :return: nothing
        """
        uname = GlobalData._user_model.get_username()
        uid = GlobalData._user_model.get_id()
        self.ids.welcome_text.text = 'Welcome ' + uname
        self.ids.user_info.text = 'Username: ' + uname + '\n' + 'ID: '\
                                      + str(uid)

    def logout(self):
        """
        The function to log an user out.
        :return: nothing
        """
        GlobalData._user_model = {}
        scmanager.current = 'login'


scmanager = GlobalData._scmanager
scmanager.add_widget(LoginScreen(name='login'))
scmanager.add_widget(RegisterScreen(name='register'))
scmanager.add_widget(MainScreen(name='mainsc'))


scmanager.current = 'login'


class socialApp(App):

    def build(self):
        Clock.schedule_interval(scmanager.update, 1.0/60.0)
        return scmanager


if __name__ == '__main__':
    socialApp().run()
