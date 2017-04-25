'''
Created on Apr 22, 2017
@author: isaac
This class handles all the visual for the new user messages
'''
from Screens import Screens
from WidgetModifier import Modify
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from globals import GlobalData
from ErrorPopup import Error
from message_interface import MessageInterface


class ComposeScreen(Screens):

    """
    Init all ui elements and connects to business and data logic for messages
    :param name: The name of the screen
    """
    def __init__(self, name):
        Screens.__init__(self, name)

        self.sending_clear = False
        self.message_clear = False

        self.layout = BoxLayout(padding=5, orientation='vertical')
        self.info = Modify(Label(text="New Messages"))
        self.info.size(1, 0.1)
        self.layout.add_widget(self.info.get_widget())

        self.input_uname = Modify(TextInput())
        self.input_uname.size(1, 0.1)
        self.input_uname.text("To: ")

        self.input_message = Modify(TextInput())
        self.input_message.size(1, 0.6)
        self.input_message.text("Message: ")

        self.send = Modify(Button(text="Send", on_press=self.send))
        self.send.size(1, 0.3)
        self.send.background_color(0.3, 0.6, 1, 1)

        self.cancel = Modify(Button(text="Cancel", on_press=self.back))
        self.cancel.size(1, 0.3)
        self.cancel.background_color(0.3, 0.6, 1, 1)

        self.layout.add_widget(self.input_uname.get_widget())
        self.layout.add_widget(self.input_message.get_widget())
        self.layout.add_widget(self.send.get_widget())
        self.layout.add_widget(self.cancel.get_widget())

    def on_init(self):
        """
        Final inits that the class
        should make before being ran
        """
        self.add_widget(self.layout)

    def update(self):
        pass

    def send(self, parm):
        """
        Send a new message to
        the user with the valid
        username provided
        """
        to_name = self.filter_logic(
            self.input_uname.get_widget().text,
            "to:", len("to:"))
        if to_name is None:
            Error(title="Username Error",
                  content=Label(text="Please provide a valid username")).open()
        else:
            to_id = GlobalData._user_model.get_user(to_name)
            if to_id is None:
                Error(title="Username Error",
                      content=Label(text="User not found")).open()
            else:
                to_id = to_id['uid']

                message_name = self.filter_logic(self.input_message.
                                                 get_widget().text, "Message:",
                                                 len("Message:"))

                if message_name is None:
                    Error(title="Messgae Error",
                          content=Label(text="Please Proper fill " +
                                        "the message field")).open()
                else:
                    message_interface = MessageInterface(GlobalData.
                                                         _user_model)
                    message_interface.send_message(to_id, message_name)

                    GlobalData._current_convo = to_id
                    self.input_uname.text("to:")
                    self.input_message.text("message:")
                    GlobalData._update_ui = True
                    Screens._manager.active_screen("messages")

    def filter_logic(self, text, holder, width):
        """
        Filter through the information in a specific text field
        and get useful data
        :param text: the text of the text input
        :param holder: the placeholder in the text input
        :param the length of the placeholder
        """
        if len(text) > 0:
            reciever = text.strip()
            if len(reciever) > width:
                if reciever[:width].lower() == holder.lower():
                    reciever = reciever[width:].strip()
                else:
                    reciever = reciever.strip()

                return reciever
            else:
                return None

        else:
            return None

    def back(self, param):
        """
        Return to the
        message ui screen
        """
        GlobalData._current_convo = None
        Screens._manager.active_screen("messages")
