from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from user_login import UserData

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
            on_release: root.user_login(). root.manager.current = 'mainsc'
        Label:
            text: 'New to the app?'
        Button:
            id: register
            text: 'Register'
            on_release: root.manager.current = 'register'
        Button:
            text: 'Exit'

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
            on_release: root.user_register(), root.manager.current = 'mainsc'
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
            id: new_user_info
        Button:
            text: 'Logout'
            on_release: root.manager.current = 'login'

""")


class LoginScreen(Screen):

    def user_login(self):
        user_name = self.ids.username.text
        user_id = self.ids.uid.text
        user_token = self.ids.token.text
        self.User_object.login(self, user_id, user_name, user_token)


class RegisterScreen(Screen):

    def user_register(self):
        new_username = self.ids.new_username.text
        UserData.register(new_username)


class MainScreen(Screen):

    def update_text(self):
        info = self.manager.get_screen('login').User_object
        self.ids.welcome_text.text = info.get_username()


scmanager = ScreenManager()
scmanager.add_widget(LoginScreen(name='login'))
scmanager.add_widget(RegisterScreen(name='register'))
scmanager.add_widget(MainScreen(name='mainsc'))

scmanager.current = 'login'


class SocialApp(App):

    def build(self):
        return scmanager


if __name__ == '__main__':
    SocialApp().run()
