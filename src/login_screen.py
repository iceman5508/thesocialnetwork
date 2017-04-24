from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from globals import GlobalData
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


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
        TextInput:
            id: username
            text: 'Enter username here'
        TextInput:
            id: uid
            text: 'Enter your id here'
        TextInput:
            id: token
            text: 'Enter your token here'
        Button:
            id: login
            text: 'Submit'
            on_release: root.user_login()
        Label:
            text: 'New to the app?'
        Button:
            id: register
            text: 'Register'
            on_release: root.manager.current = 'register'
        Button:
            text: 'Exit'
            on_release: app.stop()

<RegisterScreen>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Register information'
        TextInput:
            id: new_username
            text: 'Write your new username here'
        Button:
            id: register_user
            text: 'Register'
            on_release: root.user_register()
        Button:
            text: 'Return'
            on_release: root.manager.current = 'login'

<MainScreen>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: ''
            id: welcome_text
        Label:
            text: ''
            id: user_info
        Button:
            text: 'Logout'
            on_release: root.manager.current = 'login'

""")

class LoginScreen(Screen):

    def user_login(self):
        user_name = self.ids.username.text
        user_id = self.ids.uid.text
        user_token = self.ids.token.text
        GlobalData._user_model.login(int(user_id), user_name, user_token)
        if GlobalData._user_model.login(int(user_id), user_name, user_token) == 'Error':
            popup_error()
        else:
            self.manager.get_screen('mainsc').update_text_login()
            scmanager.current = 'mainsc'


class RegisterScreen(Screen):

    def user_register(self):
        new_username = self.ids.new_username.text
        user_info = GlobalData._user_model.register(new_username)
        uname = GlobalData._user_model.get_username()
        uid = GlobalData._user_model.get_id()
        utoken = GlobalData._user_model.get_token()
        GlobalData._user_model.login(uid, uname, utoken)
        self.manager.get_screen('mainsc').update_text_register()
        scmanager.current = 'mainsc'


class MainScreen(Screen):

    def update_text_register(self):
        uname = GlobalData._user_model.get_username()
        uid = GlobalData._user_model.get_id()
        utoken = GlobalData._user_model.get_token()
        self.ids.user_info.text = 'Username: ' + uname + '\n' + 'ID: ' \
                                      + str(uid) + '\n' + 'Token: ' + utoken
        self.ids.welcome_text.text = 'Welcome ' + uname

    def update_text_login(self):
        uname = GlobalData._user_model.get_username()
        uid = GlobalData._user_model.get_id()
        self.ids.welcome_text.text = 'Welcome ' + uname
        self.ids.user_info.text = 'Username: ' + uname + '\n' + 'ID: '\
                                      + str(uid)

    def logout(self):
        GlobalData._user_model = {}
        scmanager.current = 'login'


scmanager = ScreenManager()
scmanager.add_widget(LoginScreen(name='login'))
scmanager.add_widget(RegisterScreen(name='register'))
scmanager.add_widget(MainScreen(name='mainsc'))

scmanager.current = 'login'


class LoginuiApp(App):

    def build(self):
        return scmanager


if __name__ == '__main__':
    LoginuiApp().run()
