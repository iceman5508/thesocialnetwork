'''
Created on Apr 4, 2017

@author: isaac
'''


class Modify():
    '''
    This class can be used to modify properties of kivy widgets
    '''

    def __init__(self, widget):
        '''
        Constructor
        '''

        self.widget = widget

    '''
    Modifies the color of widget
    '''
    def text_color(self, r, g, b, alpha):

        self.widget.color = [r, g, b, alpha]

    '''
    Modifies the background color
    '''
    def background_color(self, r, g, b, alpha):
        self.widget.background_color = [r, g, b, alpha]

    '''
     Modifies the size of the widget
     '''
    def size(self, width, height):
        # self.widget.size = [width,height]
        self.widget.size_hint = (width, height)

    '''
    Modifies the position of the widget
    '''
    def position(self, x, y):
        self.widget.pos = [x, y]

    '''
    Modify the size of the text
    '''
    def text_size(self, size):
        self.widget.font_size = size

    '''
    modify the text of a widget
    '''
    def text(self, text):
        self.widget.text = text

    '''
    Returns the modified widget
    '''
    def get_widget(self):
        return self.widget
