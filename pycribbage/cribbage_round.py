from pycribbage.cribbage_tools import deal
from pycribbage import deck_tools,the_play,the_show 
from copy import deepcopy
class CribbageRound():
    """
    A class used to represent a round of Cribbage within a game

    ...

    Attributes
    ----------
    pone : Player
        a Player object to represent the non-dealer (pone)
    dealer : dict
        a Player object to represent the dealer 
    pone_score_start : int
        pone's score at start of the round
    dealer_score_start : int
        dealer's score at start of the round        
    crib : Hand
        the cards stored in the crib

        
    Methods
    -------
    deal()
        Deal out hands and perform cut
    discard()
        collect player's discard and move into crib 
    update_final_scores()
        add the player's final scores to the round class 
        in order to work out the total change in for this round only 
    the_show()
        play the show part of the round and update scores
    the_play()
        play the play part of the round and update scores    
    """
    def __init__(self,pone,dealer):
    
        """
        Parameters
        ----------
        pone : Player
            non-dealer (pone) player object
        dealer : Player
            dealer (pone) player object            
        """
        
        
        self.pone = pone
        self.dealer =dealer
        
        self.pone_score_start = self.pone.score
        self.dealer_score_start = self.dealer.score
        
        self.pone_score_end = 0
        self.dealer_score_end = 0

        self.crib = deck_tools.Hand() 
        self.cut_card = deck_tools.Hand() 
        self.deck = deck_tools.Hand() 
 
    def deal(self,set_game={}):
        """
        Deal out hands and perform cut
        
        Parameters
        ----------
        set_game : dict, optional 
            dict of hands for each player , 
            default is an empty dict in which case new random hands are created
            

        Returns
        ----------
        for_set_game : dict
            dict of hands for each player, this is returned so that the 
            same hands can be replayed 
        """
        
        if len(set_game.keys()) ==0:
           pone_hand,dealer_hand,cut_card,deck  = deal()
        else:
           pone_hand =set_game['pone_hand']
           dealer_hand =set_game['dealer_hand']
           cut_card =set_game['cut_card']
           deck =set_game['deck']
       
        for_set_game ={'pone_hand' : deepcopy(pone_hand),
         'dealer_hand' : deepcopy(dealer_hand),
         'cut_card' : deepcopy(cut_card),
         'deck':deepcopy(deck)}
        
        self.pone.update_hand(pone_hand)
        self.dealer.update_hand(dealer_hand)
        self.cut_card = cut_card
        self.deck = deck
        
        return for_set_game
        
    def discard(self):
        """collect player's discard and move into crib""" 
        
        self.pone.discard_method.update_hand(self.pone.hand)
        pone_to_discard = self.pone.discard_method.choose_discard()
        self.pone.move_to_crib(pone_to_discard,self.crib)

        self.dealer.discard_method.update_hand(self.dealer.hand)
        dealer_to_discard = self.dealer.discard_method.choose_discard()
        self.dealer.move_to_crib(dealer_to_discard,self.crib)

    
    def update_final_scores(self):
       """add the player's final scores to the round class 
           in order to work out the total change in for this round only 
       """
       self.pone_score_end = self.game_score.player_1.score
       self.dealer_score_end = self.game_score.player_2.score

    def the_show(self):
        """play the show part of the round and update scores
        
        Returns 
        ----------
        show, TheShow
            returns the corresponding TheShow object
        """
        show = the_show.TheShow(self.pone.hand,self.dealer.hand,self.crib,self.cut_card)
        self.pone.update_score(show.pone_score)
        self.dealer.update_score(show.dealer_hand_score)
        self.dealer.update_score(show.crib_score)
        return show
        
    def the_play(self):
        """play the play part of the round and update scores
        
        Returns 
        ----------
        temp, ThePlay
            returns the corresponding ThePlay object
        """
        temp = the_play.ThePlay(self.pone,self.dealer)
        temp.play()
        return temp
