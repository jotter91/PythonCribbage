from copy import deepcopy
from pycribbage import deck_tools
import random


class Discard():
    """
    A class used to choose which cards to discarding to the crib in a 
    game of Cribbage

    ...

    Attributes
    ----------
    to_discard : list
        the indices of the cards from the hand to discard
    hand : Hand object
        a Hand of cards from which to discard from
    sets : list ,
        a list of the possible discard sets
    Methods
    -------
    update_hand()
        Copy of the player's hand 
    choose_discard()
        choose which cards to discard to the crib    
    create_discard_sets()
        Function to create discard combinations        
    """
    
    def __init__(self):
        self.to_discard=[]
        self.hand =deck_tools.Hand()
        self.sets = self.create_discard_sets()
    def update_hand(self,hand):
        """Copy the player's hand for processing """
        
        #deepcopy as don't want to alter the original
        self.hand=deepcopy(hand)
    def choose_discard(self):
        """choose which cards to discard to the crib
        Returns
        ----------
        to_discard : list
            the indices of the cards from the hand to discard
        """
        
        #this is default class so it discards the first two cards in deck 
        to_discard=[0,1]
        
        return to_discard
    #TODO: move to a static method of discard_methods
    def create_discard_sets(self): 
        """Function to create discard combinations
        Returns
        --------
        sets, list 
            a list of multiple 2 element lists which correspond to the 
            possible cards to discard from a 6 card hand 
        """
        sets = []
        sets.append([0, 1])
        sets.append([0, 2])
        sets.append([0, 3])
        sets.append([0, 4])
        sets.append([0, 5])
        sets.append([1, 2])
        sets.append([1, 3])
        sets.append([1, 4])
        sets.append([1, 5])
        sets.append([2, 3])
        sets.append([2, 4])
        sets.append([2, 5])
        sets.append([3, 4])
        sets.append([3, 5])
        sets.append([4, 5])

        return sets
    def print_out(self,to_print):
        print(to_print)
    

        

class RandomDiscard(Discard):
    __doc__ = Discard.__doc__ + '\n A Discard subclass used randomly choose which cards to discard\n'
    
    
    
    def __init__(self):
        
        Discard.__init__(self)
        
    def choose_discard(self): 
        __doc__ = Discard.__doc__ +'\n this subclass overrides default func to randomly choose which cards to discard'
        
        
        return self.sets[random.randrange(14)]

