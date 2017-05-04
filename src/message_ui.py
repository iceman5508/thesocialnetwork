'''
Created on Apr 22, 2017
@author: isaac
This class handles all the visual for the user messages
'''
from Screens import Screens
from globals import GlobalData
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from WidgetModifier import Modify
from message_interface import MessageInterface
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from Convo_item import ConvoItem
from kivy.uix.button import Button
from ErrorPopup import Error
from _ast import If


class MessageScreen(Screens):
    """
    Init all ui elements and connects to business and data
    logic for messages
    :param name: The name of the screen
    """
    def __init__(self, name):
        Screens.__init__(self, name)
        self.main_layout = BoxLayout(padding=10)
        self.mi = MessageInterface(GlobalData._user_model)

        self.left_layout = BoxLayout(padding=10, orientation='vertical')
        convo_label = Modify(Label(text=GlobalData._user_model.get_username() +
                             "'s Conversations"))
        convo_label.size(1, 0.2)

        self.new_convo = Modify(Button(text="Compose New Message",
                                on_press=self.start_new))
        self.new_convo.size(1, 0.2)
        self.new_convo.background_color(0.4, 1, 1, 1)
        self.new_convo.text_color(1, 1, 1, 1)
        
        self.homee = Modify(Button(text="Return Home",
                            on_press=self.home))
        self.homee.size(1, 0.2)
        self.homee.background_color(0.4, 1, 1, 1)
        self.homee.text_color(1, 1, 1, 1)

        self.left_layout.add_widget(convo_label.get_widget())
        self.left_layout.add_widget(self.new_convo.get_widget())
        self.left_layout.add_widget(self.homee.get_widget())

        self.right_layout = BoxLayout(padding=10, orientation='vertical')

        self.message_list = list()
        self.get_conversations()

        self.display_message = TextInput(text="No Message Selected")
        self.display_message_func()

        display_layout = GridLayout(rows=1)
        display_layout.add_widget(self.display_message.get_widget())
        self.right_layout.add_widget(display_layout)

        self.send_message = TextInput()
        self.send_message.disabled = True
        self.send_message = Modify(self.send_message)
        self.send_message.size(1, 0.4)
        self.right_layout.add_widget(self.send_message.get_widget())

        self.send_button = Modify(Button(text="Send", on_press=self.send))
        self.send_button.size(1, 0.2)
        self.send_button.background_color(0.3, 0.6, 1, 0.8)
        self.send_button.get_widget().disabled = True

        self.right_layout.add_widget(self.send_button.get_widget())

    def on_init(self):
        """
        Final inits that the class
        should make before being ran
        """

        '''list of all conversations'''
        self.main_layout.add_widget(self.left_layout, 1)
        '''display specific messages'''
        self.main_layout.add_widget(self.right_layout, 0)
        self.add_widget(self.main_layout)

    def get_conversations(self):
        """
        Get all conversation
        of the user from the business logic
        and display it in the ui
        """
        self.message_list = self.mi.get_conversations()
        for item in self.message_list:
            item_button = Modify(ConvoItem(item))
            item_button.size(1, 0.3)
            item_button.background_color(0.3, 0.6, 1, 1)
            self.left_layout.add_widget(item_button.get_widget())

    def display_message_func(self):
        """
        Provide Ui rules for displaying messages
        """
        self.display_message.multiline = True
        self.display_message.disabled = True
        self.display_message = Modify(self.display_message)
        self.display_message.size(1, 0.7)

    def update(self):
        """
        Update the message by checking across the business logic
        and update the ui upon getting a new message.
        """

        if GlobalData._update_ui is True:
            self.message_list = self.mi.get_conversations()
            add_to = GlobalData._user_model.get_user_by_id(
                     GlobalData._current_convo )
            item_button = Modify(ConvoItem(add_to))
            item_button.size(1, 0.3)
            item_button.background_color(0.3, 0.6, 1, 1)
            self.left_layout.add_widget(item_button.get_widget())
            GlobalData._update_ui = False          

        try:
            if GlobalData._current_convo is not None:
                message = self.mi.get_message(GlobalData._current_convo)
                if self.send_message.get_widget().disabled is True:
                    self.send_message.get_widget().disabled = False
                    self.send_button.get_widget().disabled = False
                text = ""
                for talk in message:
                    text = text+"___________________________________________\n"
                    text = text+"Sender: "+talk['sender']+"\n"
                    text = text+"Message: "+talk['content']+" \n"
                    text = text+"Time Sent: "+talk['time']+" \n"

                self.display_message.get_widget().text = text
        except ValueError:
            pass

    def send(self, param):
        """
        Send a new message to a the user currently in coversation
        with the logged in user.
        """
        if GlobalData._current_convo is not None:
            if len(self.send_message.get_widget().text) > 0:
                self.mi.send_message(
                   GlobalData._current_convo,
                   self.send_message.get_widget().text)

                self.send_message.get_widget().text = ""
            else:
                Error(title="Message Error",
                      content=Label(text="No blank messages")) .open()

    def start_new(self, param):
        """
        Switch to the compose screen
        for starting a new message string
        to a new user
        """
        self.display_message.text("No Message Selected")
        self.send_message.get_widget().disabled = True
        self.send_button.get_widget().disabled = True
        Screens._manager.active_screen("new_messages")
    
    def home(self, param):
        """
        Switch to the home screen
        """
        self.display_message.text("No Message Selected")
        self.send_message.get_widget().disabled = True
        self.send_button.get_widget().disabled = True
        Screens._manager.active_screen("mainsc")
