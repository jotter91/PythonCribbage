from pycribbage import deck_tools,scorer
from copy import deepcopy

class ThePlay():
    """
    A class used to represent a the play phase of cribbage

    ...

    Attributes
    ----------
    active_player : str
        string to denote who's turn it is 
    on_table : Hand 
        a Hand object that represents the cards on the table to be scored
    pone : Player
        a Player object to represent the non-dealer (pone)
    dealer : dict
        a Player object to represent the dealer     
    dealer_go : bool
        bool to represent if the dealer is able to play a card_to_play
        True means that the play has said 'go' and cannot go
    pone_go : bool
        bool to represent if pone is able to play a card_to_play
        True means that the play has said 'go' and cannot go
    go_added : bool
        bool to keep track is the point for a go has been added to the player's score  
    play_end : bool
        bool to represent if the play has finished 
    pone_hand_init : Hand 
        a Hand object that represents the cards dealt to pone player . 
        This is required as cards will be moved to the table and they need to be returned
        before the show 
    dealer_hand_init : Hand 
        a Hand object that represents the cards dealt to the dealer. 
        This is required as cards will be moved to the table and they need to be returned
        before the show  
    pone_score_init : int
        pone's score at start of the play
    dealer_score_init : int
        dealer's score at start of the play  
    pone_score_init : int
        pone's accrued score  in the play 
    dealer_score_init : int
        dealer's accrued score in the play 
    table_sum : int
        sum of face values of the cards on the table 
    out_string : str
       string to store updates of the play 
            
            
    Methods
    -------
    play()
        Plays out the play
        
    """
    def __init__(self,pone,dealer):
        """
        Parameters
        ----------
        pone : Player
            a Player object to represent the non-dealer (pone)
        dealer : dict
            a Player object to represent the dealer 
        """
        
        self.active_player='pone'
        self.on_table = deck_tools.Hand()

        self.pone = pone
        self.dealer = dealer

        self.dealer_go=False
        self.pone_go=False

        self.go_added = False
        self.play_end=False

        self.pone_hand_init = deepcopy(pone.hand)
        self.dealer_hand_init = deepcopy(dealer.hand)
   
        self.pone_score_init= pone.score
        self.dealer_score_init= dealer.score

        self.pone_the_play_score =0
        self.dealer_the_play_score =0
        
        self.table_sum=0
        self.out_string=''
    def play(self):
        """  Plays out the play """
        
        while self.play_end ==False: 
           
            if len(self.pone.hand.cards)==0 and len(self.dealer.hand.cards)==0:
                self.play_end=True 
            
            # when both go reset and carry on
            if self.dealer_go is True and self.pone_go is True:
                self.table_sum = 0
                self.on_table = deck_tools.Hand()
                self.pone_go = False
                self.dealer_go = False
                self.go_added = False

            active_player  = getattr(self, self.active_player)
           
            if len(active_player.hand.cards)>0:
            
                active_player.the_play_method.update_hand(active_player.hand)
                active_player.the_play_method.update_on_table(self.on_table)
                
                index_to_play = active_player.the_play_method.choose_play() 
                
                if index_to_play== None: 
                    self.go()
                else:
                    
                    card_to_play= active_player.hand.cards[index_to_play]
                    active_player.hand.remove_card(card_to_play)
                    self.on_table.add_card(card_to_play)
                    self.table_sum = self.table_sum + card_to_play.face_value
                    to_add = scorer.ScoreThePlay(self.on_table).score
                    active_player.update_score(to_add)
                    
                    self.out_string += '%s plays %s  Sum : %i.\nAdd %i for %s.\n%s score : %i %s  score :%i\n'%\
                            (active_player.name,
                             card_to_play,
                             self.table_sum,
                             to_add,
                             active_player.name,
                             self.pone.name,
                             self.pone.score,
                             self.dealer.name,
                             self.dealer.score)
                    self.out_string += 'On table :\n%s\n'%(self.on_table.__str__())
                    
                    self.switch_player() 
                    
            else:
                self.go()
                
        self.return_cards()            
        self.get_the_play_score()
        
    #TODO: private?    
    def go(self):
        """ simulate the fact that active player can't play so says go"""
        active_player  = getattr(self, self.active_player)
        self.out_string+='%s said go\n'%active_player.name
        setattr(self,self.active_player +'_go',True)
       
        self.switch_player()
        active_player  = getattr(self, self.active_player)
        
        if self.go_added == False:
            active_player.update_score(1)
            self.go_added = True
            
    #TODO: private?            
    def switch_player(self):
        """ switch active player after a cards has been played or player says go"""
        if self.active_player == 'pone':
            self.active_player = 'dealer'
        else:
            self.active_player = 'pone'
    #TODO: private?            
    def get_the_play_score(self):
        """ calculate the scores accured in the play"""
        self.pone_the_play_score = self.pone.score - self.pone_score_init
        self.dealer_the_play_score = self.dealer.score - self.dealer_score_init
    #TODO: private?        
    def return_cards(self):
        """ move cards from the table back to player's hands"""
        self.pone.update_hand(self.pone_hand_init)
        self.dealer.update_hand(self.dealer_hand_init)
    
    def __str__(self):
        """ print the summary of the round"""
        return self.out_string

