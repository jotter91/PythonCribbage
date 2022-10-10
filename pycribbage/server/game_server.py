import sys
sys.path.append('C:\\JohnData\\software\\misc\\cr\\PyCribbage\\PyCribbage\\')
from pycribbage.cribbage_game import CribbageGame

import requests
import urllib.parse


class CribbageGameServer(CribbageGame):
    __doc__ = CribbageGame.__doc__ + '\n add server functions'
    
    def __init__(self,players,set_game={},cut_player=None,batch_mode=False,home_loc=None):
        CribbageGame.__init__(self,players,set_game,cut_player,batch_mode)
        self.home_loc = home_loc 
        
    def save_state(self):
        url = urllib.parse.urljoin(self.home_loc,'state')
        state = self.get_state()
        x = requests.post(url, json = state)
        
#function to create game     
def start_game(players):
    game = CribbageGameServer(players,home_loc ='http://127.0.0.1:5000/')
    
    game.play_game()
#create a database for game? - probably another function 

#delete game     
