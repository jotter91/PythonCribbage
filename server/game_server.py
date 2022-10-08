from pycribbage.cribbage_game import CribbageGame,
from pycribbage.discard_methods import Discard

import requests
import urllib.parse
class CribbageGameServer(CribbageGame):
    __doc__ = CribbageGame.__doc__ + '\n add server functions'
    
    def __init__(self,home_loc):
        CribbageGame.__init__(self)
        self.home_loc = home_loc 
        
    def save_state(self):
        url = urllib.parse.urljoin(home_loc,'state')
        state = self.save_state()
        x = requests.post(url, json = state)
        
#function to create game     

#create a database for game? - probably another function 

#delete game     
#home_loc='http://127.0.0.1:5000'        

#overload human discard 
class HumanDiscardServer(Discard):
    __doc__ = Discard.__doc__ + '\n A Discard subclass used to allow a human player to choose which cards to discard'
 
    def __init__(self):
        Discard.__init__(self)
    
    #static
    def is_input_ok(self,from_input):
        """check that human inputs are correct i.e. an int between 0 and 5 

        Parameters
        -----------
        from_input, int

        Returns
        ----------
        status, bool 
        """
        status=False 
        url = urllib.parse.urljoin(home_loc,'info')
        try:
            new_int = int(from_input)
        except ValueError:
            print('input is not a valid integer,please enter again')
            
        
            x = requests.post(url,json='input is not a valid integer,please enter again')
            url = urllib.parse.urljoin(home_loc,'p1_choice')
            x = requests.post(url,json=[])
            return status
        
        if new_int<0 or new_int >5:
            print('input is not in the range of 0 and 5, please enter again')
            x = requests.post(url,json='input is not in the range of 0 and 5, please enter again')
            url = urllib.parse.urljoin(home_loc,'p1_choice')
            x = requests.post(url,json=[])
            return status
        else:
            status=True
            return status
    #static
    def are_inputs_unique(self,to_move):
        """check that human inputs are unique 

        Parameters
        -----------
        to_move, list
            two element list of ints

        Returns
        ----------
        status, bool 
        """
        status=False 
        if to_move[0] ==to_move[1]:
            print('inputs are not unique, please enter again')
            url = urllib.parse.urljoin(home_loc,'info')
        
            x = requests.post(url,json='inputs are not unique, please enter again')
            url = urllib.parse.urljoin(home_loc,'p1_choice')
            x = requests.post(url,json=[])
            return status
        else:
            status =True
            return status 
    def choose_discard(self): 
        __doc__ = Discard.__doc__ +'\n this subclass overrides default func to allow a human to choose which cards to discard'
    
        print('Choose cards to discard')
        url = urllib.parse.urljoin(home_loc,'info')
        
        x = requests.post(url,json='choose cards')
        for i,card in enumerate(self.hand.cards):
            print('%i : %s '%(i,card))
    
        to_discard=[]
        
        input_valid = False
        inputs_unique = False
        
        #check p1_choice
        url = urllib.parse.urljoin(home_loc,'p1_choice')
        
        while inputs_unique ==False: 
            x = requests.get(url,).json()
            print('got this back ', x)
            while len(x)==0:
                x = requests.get(url,).json()
                #print('got this back ', x)
                time.sleep(1)
                
            first_index=x[0]
            second_index=x[1]
        
        
            while input_valid == False:
                
                input_valid = self.is_input_ok(first_index)
            
            input_valid=False
            
            while input_valid==False:
                
                input_valid = self.is_input_ok(second_index)
        
            inputs_unique = self.are_inputs_unique([first_index,second_index])
        
        #first_index=x[0]
        #second_index=x[1]
        to_discard =[int(first_index),int(second_index)]
        x = requests.post(url,json=to_discard)
        return to_discard