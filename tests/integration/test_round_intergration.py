from pycribbage import cribbage_round,player
from pycribbage.cribbage_tools import deal
    

def test_round_full(init_round):
    """behaviour : should be able to run the whole round
    Given : a round object
    when : at the start of the round  
    then : the round is undertaken. It is complete if the players scores 
           have been incremented accordingly 
    
    Parameters: 
    -----------
    init_round initialised CribbageRound Object
    """
    round_1 = init_round

    round_1.deal()
    round_1.discard()
    
    play = round_1.the_play()
    show = round_1.the_show()
    
    assert (play.pone_the_play_score + show.pone_score) == round_1.pone.score
    assert (play.dealer_the_play_score + show.dealer_score) == round_1.dealer.score
