# NOTE: I took help from https://kivy.org/docs/api-kivy.uix.scrollview.html
# and https://kivy.org/docs/api-kivy.uix.label.html
# and https://kivy.org/docs/api-kivy.uix.textinput.html
# and https://kivy.org/docs/api-kivy.uix.button.html
# and https://kivy.org/docs/api-kivy.core.text.markup.html
# and http://stackoverflow.com/questions/42820798/how-to-add-background-
# colour-to-a-label-in-kivy
# and https://kivy.org/docs/api-kivy.config.html#kivy.config.ConfigParser.set
# and http://stackoverflow.com/questions/8266529/python-convert-string-to-list
# and http://stackoverflow.com/questions/9542738/python-find-in-list
# and http://stackoverflow.com/questions/9758959/python-how-to-sort-a-list
# -of-numerical-values-in-ascending-order
# and http://stackoverflow.com/questions/402504/how-to-determine-
# a-variables-type
# for this. (-Bhargav)

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from post_message import PostMessageInterface
from globals import GlobalData
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from ErrorPopup import Error
from kivy.uix.label import Label

Builder.load_string("""
<PostScreen>
    BoxLayout:
        padding: 5
        orientation: 'vertical'
        Label:
            text: 'New Post'
            bold: 1
            font_size: 30
            color: 0, 0.2, 0.7, 0.9

        TextInput:
            id: content
            hint_text: 'Double tap to start typing'
            background_color: 0, 0.3, 0.5, 0.5

        Button:
            text:'Post'
            background_color: 0, 0.3, 0.7, 0.65
            on_press:
                root.manager.transition.direction = 'right'
                root.post()
                root.manager.current = 'fscreen'
        Button:
            id: cancel
            text: 'Back to feed'
            background_color: 0, 0.3, 0.7, 0.65
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'fscreen'
<FeedScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        Label:
            text: 'Welcome to your feed'
            size_hint_y: 0.1
            bold: 1
            font_size: 30
            color: 0.5, 0.5, 0.3, 0.9
        ScrollView:
            GridLayout:
                cols: 1
                size_hint: None, None
                height: self.minimum_height
                Label:
                    id: display
                    size_hint: None, None
                    size: self.texture_size
                    font_size: 20
                    color: 0.2,0.2,0.6,0.77
                    bold: 1
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.1
            Label:
                text: 'Enter post IDs to upvote: '
                size_hint_x: 0.3
                color: 0.9, 0.5, 0.1, 1
                bold: 1
                italic: 1
            TextInput:
                id: upvotes_input
                size_hint_x: 0.3
                hint_text: '[MAX 3 ENTRIES] Example: 1 3 20'
                hint_text_color: 0.2, 0.5, 0.7, 0.7
                background_color: 0, 0.3, 0.5, 0.5
            Button:
                size_hint_x: 0.4
                text: 'UPVOTE'
                background_color: 0, 0.3, 0.7, 0.65
                bold: 1
                italic: 1
                on_press: root.upvote_posts()
        BoxLayout:
            orientation: 'horizontal'
            color: 1,0,0,1
            size_hint_y: 0.4
            BoxLayout:
                orientation: 'vertical'
                Label:
                    id: text_label
                    text: 'Filters'
                    font_size: 22
                    italic: 1
                    bold: 1
                    color: 0.9, 0.5, 0.1, 1
                TextInput:
                    id: limit_input
                    hint_text: 'Limit'
                    hint_text_color: 1, 0.2, 0.2, 1
                    font_size: 18
                    background_color: 0.9,0.7,0.5,1
                TextInput:
                    id: uid_input
                    hint_text: 'User ID'
                    hint_text_color: 1, 0.2, 0.2, 1
                    font_size: 18
                    background_color: 0.9,0.7,0.5,1
                TextInput:
                    id: tag_input
                    hint_text: 'Tag'
                    hint_text_color: 1, 0.2, 0.2, 1
                    font_size: 18
                    background_color: 0.9,0.7,0.5,1
            Button:
                text: 'Update feed'
                background_color: 0, 0.3, 0.7, 0.65
                bold: 1
                font_size: 22
                on_release: root.update_posts()
            Button:
                text: 'New post'
                bold: 1
                font_size: 25
                background_color: 0, 0.3, 0.7, 0.65
                on_release: root.manager.current = 'post'

            Button:
                text: 'Home'
                background_color: 0, 0.3, 0.7, 0.65
                bold: 1
                font_size: 22
                on_press: root.manager.current = 'mainsc'

""")


class PostScreen(Screen):
    def post(self):
        content = self.ids.content.text
        uid = GlobalData._user_model.get_id()
        token = GlobalData._user_model.get_token()
        post_getter = PostMessageInterface()
        post_getter.post_status(uid, content, token)


class FeedScreen(Screen):

    _current_ids = []

    def update_posts(self):
        if self.ids.limit_input.text == '' or \
                self.ids.limit_input.text == 'Limit':
            limit = 50
        else:
            limit = self.ids.limit_input.text
        if self.ids.uid_input.text == '' or \
                self.ids.uid_input.text == 'User ID':
            uid = None
        else:
            uid = self.ids.uid_input.text
        if self.ids.tag_input.text == '' or \
                self.ids.tag_input.text == 'Tag':
            tag = None
        else:
            tag = self.ids.tag_input.text

        self.ids.display.text = feed(limit, uid, tag)

    def upvote_posts(self):
        list_upvotes = []
        string_upvotes = ''
        final_list = []
        token = GlobalData._user_model.get_token()
        post_getter = PostMessageInterface()
        uid = GlobalData._user_model.get_id()
        if self.ids.upvotes_input.text == '' or \
                self.ids.upvotes_input.text == \
                '[MAX 3 ENTRIES] Example: 1 3 20':
            list_upvotes = []
        else:
            string_upvotes = self.ids.upvotes_input.text
            list_upvotes = string_upvotes.split()

        for i in range(0, len(list_upvotes)):
            final_list.append(int(list_upvotes[i]))

        final_list.sort(key=int)
        for i in range(0, len(final_list)):
            if final_list[i] in self._current_ids:
                post_getter.rate_post(final_list[i], token, uid)
            else:
                continue

        self.update_posts()


def feed(limit=50, uid=None, tag=None):
    post_getter = PostMessageInterface()
    json_response_info = post_getter.get_posts(limit, uid, tag)
    FeedScreen._current_ids = []
    display_text = ""
    message_number = 0
    for item in json_response_info:
        json_text = json_response_info[message_number]
        display_text += ('-'*500 + "\n")
        display_text += ("Username: " + json_text[u'username'])
        display_text += ("          Time: " + json_text[u'time'])
        display_text += ("          Post ID: " + str(json_text[u'postid']))
        display_text += ("\n\nContent: " + json_text[u'content'])
        display_text += ("\n\nUpvotes: " + ('[*]' * json_text[u'upvotes']))
        display_text += "\n\n"

        FeedScreen._current_ids.append(int(json_text[u'postid']))

        message_number += 1
        if message_number > limit:
            break
    return display_text

if __name__ == '__main__':
    pass
