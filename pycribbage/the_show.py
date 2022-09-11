from pycribbage import deck_tools,scorer
from copy import deepcopy

class TheShow():
    """
    A class used to represent a the show phase of cribbage

    ...

    Attributes
    ----------
    pone_hand : Hand
        a hand object to represent the non-dealer's (pone) hand
    dealer_hand : Hand
        a hand object to represent the dealer's  hand 
    crib : Hand
        a hand object to represent the crib
    cut_card : Hand
        a hand object to represent cut card   
    pone_score : int
        pone's accrued score through the show
    dealer_score_init : int
        dealer'saccrued score through the show  
    crib_score : int
        pone's accrued score through the show
    dealer_hand_score : int
        dealer's accrued score from hand only 
            
    Methods
    -------
    __str__()
        output the results in human readable form
        
    """
    def __init__(self,pone_hand,dealer_hand,crib,cut_card):
        """
        
        Parameters
        -----------
        pone_hand : Hand
            a hand object to represent the non-dealer's (pone) hand
        dealer_hand : Hand
            a hand object to represent the dealer's  hand 
        crib : Hand
            a hand object to represent the crib
        cut_card : Hand
            a hand object to represent cut card    
        
        """
        
        self.pone_score=0
        self.dealer_score=0
        self.crib_score=0
        self.dealer_hand_score=0

        #deepcopy to avoid altering the original
        self.pone_hand = deepcopy(pone_hand)
        self.dealer_hand = deepcopy(dealer_hand)
        self.crib = deepcopy(crib)
        self.cut_card = deepcopy(cut_card)

        #add the cut card to each hand for scoring - this is OK as it is a deepcopy 
        self.pone_hand.add_card(self.cut_card.cards[0])
        self.dealer_hand.add_card(self.cut_card.cards[0])
        self.crib.add_card(self.cut_card.cards[0])


        self.pone_score         = scorer.ScoreTheShow(self.pone_hand).score 
        self.dealer_hand_score  = scorer.ScoreTheShow(self.dealer_hand).score 
        self.crib_score         = scorer.ScoreTheShow(self.crib,is_crib=True).score 
        self.dealer_score       = self.dealer_hand_score + self.crib_score
    
    def __str__(self):
        """output the results in human readable form
        
        Returns
        --------
        out_string,str
            output string ... need I say more?
        """
        out_string='='*30 + "\n"
        
        out_string=out_string +'Pone Hand, Score : %i\n'%self.pone_score
        out_string=out_string +'='*30 + "\n"
        out_string=out_string + self.pone_hand.__str__() +'\n'
        out_string=out_string +'='*30 + "\n"
        
        out_string=out_string +'Dealer Hand, Score %i\n'%self.dealer_hand_score
        out_string=out_string +'='*30 + "\n"
        out_string=out_string + self.dealer_hand.__str__() +'\n'
        out_string=out_string +'='*30 + "\n"

        out_string=out_string +'Crib, Score : %i\n' %self.crib_score
        out_string=out_string +'='*30 + "\n"
        out_string=out_string + self.crib.__str__() +'\n'
        out_string=out_string +'='*30 + "\n"

        out_string = out_string +'Final Scores\n'
        out_string=out_string +'='*30 + "\n"
        out_string = out_string +'Pone : %i  Dealer : %i' %(self.pone_score,self.dealer_score)
    
        return out_string
