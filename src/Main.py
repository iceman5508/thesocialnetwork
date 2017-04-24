from kivy.app import App
from kivy.clock import Clock
from view.Screens import Screens
from ui.message_ui import MessageScreen
from ui.new_message_ui import ComposeScreen

'''
Social Messaging application
Provide messaging and posting services
to users
'''


class social():

    def __init__(self):

        '''message screen'''
        message = MessageScreen("messages")
        message.on_init()

        '''this is temp and should be removed once first screen is made'''
        message.make_active()

        '''new message screen'''
        new_message = ComposeScreen("new_messages")
        new_message.on_init()


class socialApp(App):

    def build(self):
        social()
        Clock.schedule_interval(Screens._manager.update, 1.0/60.0)
        return Screens._manager

if __name__ == '__main__':
    socialApp().run()
