'''
Created on Apr 22, 2017

@author: isaac
'''
from kivy.uix.button import Button
from globals import GlobalData


class ConvoItem(Button):
    '''
    classdocs
    '''

    def __init__(self, convo, **kwargs):
        '''
        Constructor
        '''
        Button.__init__(self, **kwargs)

        self.speaker_id = convo['uid']
        self.text = convo['username']

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 0.3, 0.6, 1]
            GlobalData._current_convo = self.speaker_id
        else:
            self.background_color = [0.3, 0.6, 1, 1]
