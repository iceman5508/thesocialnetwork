'''
Created on Apr 2, 2017

@author: isaac
'''
from kivy.uix.popup import Popup


class Error(Popup):
    '''
    This class handeles popup errors
    '''


    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        Popup.__init__(self,**kwargs)
        '''
        Constructor
        '''
        self.size_hint= (0.4,0.4)
        
        self.auto_dismiss=True
        
    
    

