'''
Created on Apr 3, 2017

@author: isaac
@summary: This class helps to create screens a lot easier 
as well as work in conjunction with the scene manager.
'''
from kivy.uix.screenmanager import Screen
from abc import ABCMeta, abstractmethod
from SceneManager import SceneManager
from kivy.graphics import Color,Rectangle
from kivy.core.window import Window


class Screens(Screen):
    '''
    Screens is an abstract class that blueprints
    the creation of kivy screens. This class works 
    closely with the SceneManager to make transition of screens easier.
    Note that the only parent class method that should be called is the on_init
    method
    '''
    __metaclass__ = type('Screens', (type(Screen), ABCMeta), {})
    
    _manager = SceneManager()
   
    '''
    This is the default constructor.
    Here in the constructor 
    '''
    def __init__(self, name):
        '''
        Constructor
        '''
        Screen.__init__(self)        
        self.name = name       
        Screens._manager.add_screen(self)

    '''
    This method changes the background color of
    the screen

    '''
    def background_color(self, r, g, b, alpha):
        with self.canvas:
            Color(r, g, b, alpha)
            Rectangle(pos=self.pos, size=Window.size)

    '''
    This method makes this specific screens class instance as
    the currently viewed screen.
    '''
    def make_active(self):
        Screens._manager.active_screen(self.name)
    
    '''
    This method is used to init all properties 
    for the specific instance of the screens class
    this should be the last class method called
    '''         
    @abstractmethod   
    def on_init(self):
        pass  
    
    '''
    This method will update all objects painted on screen
    '''         
    @abstractmethod   
    def update(self):
        pass  