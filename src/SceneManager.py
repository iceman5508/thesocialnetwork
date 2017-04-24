'''
Created on Apr 3, 2017

@author: isaac
@summary: This class Manages all screens being used
in order to make the creation and transition between 
screens easier. 

@note: There is no need to call this class directly 
since all the management is done within the screen 
class automatically. 
'''
from kivy.uix.screenmanager import ScreenManager


class SceneManager(ScreenManager):
    
    def __init__(self):
        
        ScreenManager.__init__(self)
    
    '''
    Adds a specific screen to the scene manager
    this method is called whenever a new screen is
    created. 
    '''
    def add_screen(self, screen):
        self.add_widget(screen)

    '''
    Sets a specific screen as the currently viewed screen.
    Note that the argument being asked for is the name of the 
    screen. 
    '''    
    def active_screen(self, screen_name):
        if self.has_screen(screen_name) is True:
            self.current = screen_name

    def update(self, params):
        self.get_screen(self.current).update()
