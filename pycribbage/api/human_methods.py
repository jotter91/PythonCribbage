from pycribbage.the_play_methods import ThePlayMethod
from pycribbage.discard_methods import Discard
import requests
import urllib.parse
import time 


class HumanThePlay(ThePlayMethod):
    __doc__ = ThePlayMethod.__doc__ + '\n A ThePlayMethod subclass used to allow a human choice of card to play'
    
    def __init__(self):
        ThePlayMethod.__init__(self)
    
    def is_input_ok(self,from_input,valid_index):
        """check that human inputs are correct i.e. an int between 0 and 5 

        Parameters
        -----------
        from_input, int
        valid_index,list
            list (elements are ints) of valid choices 
        Returns
        ----------
        status, bool 
        """
        status=False 
        
        try:
            new_int = int(from_input)
        except ValueError:
            self.print_out('input is not a valid integer,please enter again')
            return status
        
        if new_int not in valid_index:
            self.print_out( ('input is not valid, choices are : '+str(valid_index)) )
            self.print_out('please enter again')
            return status
        else:
            status=True
            return status
        
    def choose_play(self):     
        """human method to choose play""" 
        
        print('Waiting for your choice')
        print('cards on the table:')
        
        for card in self.on_table.cards:
            print('%s '%(card))

        self.get_table_sum()
        print('table sum is %i' %self.table_sum)
        
        valid_index = self.assess_validity()
        print('Your hand:') 
        for i,card in enumerate(self.hand.cards):
            print('%i : %s '%(i,card))
    
        
        if len(valid_index)>1:
            input_valid =False
            while input_valid==False:
                choice = input('Choose index of card to play')
                input_valid = self.is_input_ok(choice,valid_index)
            return int(choice)
        
        elif len(valid_index)==1:
            print('only one valid choice')
            input('you will play %i, press a key to continue '%valid_index[0])
            return valid_index[0]
        
        elif len(valid_index)==0:
            print('no valid choices so you must say go')
            input('Say go, press a key to continue')
            return None
            
class HumanDiscard(Discard):
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
        
        try:
            new_int = int(from_input)
        except ValueError:
            self.print_out('input is not a valid integer,please enter again')
            return status
        
        if new_int<0 or new_int >5:
            self.print_out('input is not in the range of 0 and 5, please enter again')
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
            self.print_out('inputs are not unique, please enter again')
            return status
        else:
            status =True
            return status 
    def choose_discard(self): 
        __doc__ = Discard.__doc__ +'\n this subclass overrides default func to allow a human to choose which cards to discard'
    
        print('Choose cards to discard')
        for i,card in enumerate(self.hand.cards):
            print('%i : %s '%(i,card))
    
        to_discard=[]
        
        input_valid = False
        inputs_unique = False
        
        while inputs_unique ==False: 
        
            while input_valid == False:
                first_index = input('Choose first card to discard :')
                input_valid = self.is_input_ok(first_index)
            
            input_valid=False
            
            while input_valid==False:
                second_index = input('Choose second card to discard :')
                input_valid = self.is_input_ok(second_index)
        
            inputs_unique = self.are_inputs_unique([first_index,second_index])
        
        to_discard =[int(first_index),int(second_index)]
        
        return to_discard            
        
        

#overload human discard 
class HumanDiscardServer(HumanDiscard):
    __doc__ = HumanDiscard.__doc__ + '\n extension via a server'
    
    def __init__(self,home_loc,choice):
        HumanDiscard.__init__(self)
        #self.home_loc = home_loc
        self.choice = choice
        self.url_state = urllib.parse.urljoin(home_loc,'state')
        self.url_info   = urllib.parse.urljoin(home_loc,'info')
        
        self.state = requests.get(self.url_state).json()
    def print_out( self,to_print,clear=True):
        x = requests.post(self.url_info,json=to_print)
        if clear==True:
            self.state[self.choice]=[]
            x = requests.post(self.url_state,json=self.state)   
  
    def choose_discard(self): 

        self.print_out('Choose cards to discard',False)
    
        to_discard=[]
        
        input_valid = False
        inputs_unique = False
        
       
        
        while inputs_unique ==False: 
            x = requests.get(self.url_state,).json()
            p_choice= x[self.choice]
            
            while len(p_choice)==0:
                x = requests.get(self.url_state,).json()
                
                p_choice= x[self.choice]
                time.sleep(1)
                
            first_index=p_choice[0]
            second_index=p_choice[1]
        
        
            while input_valid == False:
                
                input_valid = self.is_input_ok(first_index)
            
            input_valid=False
            
            while input_valid==False:
                
                input_valid = self.is_input_ok(second_index)
        
            inputs_unique = self.are_inputs_unique([first_index,second_index])
        

        to_discard =[int(first_index),int(second_index)]
        self.state[self.choice]=[]
        x = requests.post(self.url_state,json=self.state)
        
        return to_discard
        
class HumanThePlayServer(HumanThePlay):
    __doc__ = HumanThePlay.__doc__ + '\n A ThePlayMethod subclass used to allow a human choice of card to play'
    
    def __init__(self,home_loc,choice):
        HumanThePlay.__init__(self)
        #self.home_loc = home_loc
        self.choice = choice
        self.url_state = urllib.parse.urljoin(home_loc,'state')
        self.url_info   = urllib.parse.urljoin(home_loc,'info')
        
        self.state = requests.get(self.url_state).json()
    def print_out( self,to_print,clear=True):
        x = requests.post(self.url_info,json=to_print)
        if clear==True:
            self.state[self.choice]=[]
            x = requests.post(self.url_state,json=self.state)    
 
    def choose_play(self):     
        """human method to choose play""" 
        
        self.print_out('Waiting for your choice to add to the table',False)

        self.get_table_sum()
                
        valid_index = self.assess_validity()
       
        if len(valid_index)>1:
            input_valid =False
            
            while input_valid==False:
                x = requests.get(self.url_state,).json()
                p_choice= x[self.choice]
                print('got this back ', x)
                while len(p_choice)==0:
                    x = requests.get(self.url_state,).json()
                    p_choice= x[self.choice]
                    print('got this back ', x)
                    time.sleep(1)
                    
                input_valid = self.is_input_ok(p_choice[0],valid_index)
             
            self.state[self.choice]=[]
            _ = requests.post(self.url_state,json=self.state)
            return int(p_choice[0])
        
        elif len(valid_index)==1:
            print('only one valid choice')
            self.print_out('you will play %i, press a key to continue '%valid_index[0])
            _ = requests.post(self.url_state,json=[])
            return valid_index[0]
        
        elif len(valid_index)==0:
            self.print_out('no valid choices so you must say go')
            #input('Say go, press a key to continue')  
            _ = requests.post(self.url_state,json=[])
            return None

                    