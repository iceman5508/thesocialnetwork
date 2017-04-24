from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from user_login import UserData


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


class LoginuiApp(App):

    def build(self):
        return scmanager


if __name__ == '__main__':
    LoginuiApp().run()
