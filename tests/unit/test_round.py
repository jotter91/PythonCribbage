from pycribbage import cribbage_round,player
from pycribbage.cribbage_tools import deal
    

def test_round_init(init_round):
    """behaviour : round should store players in pone (non-dealer) and dealer 
    Given : a game of cribbage is in progress
    WHen : start of next round 
    then : initialise the round with two players
    
    Parameters: 
    -----------
    init_round initialised CribbageRound Object
    """
    round_1 = init_round
   
    assert isinstance(round_1.pone,player.Player) == True
    assert isinstance(round_1.dealer,player.Player) == True


def test_round_deal(init_round):    
    """behaviour : round should be able to deal two hands to the two players
    Given : a round object 
    when : ast the start of a round 
    then : deal 6 cards to each player and choose 1 cut card 
    
    Parameters: 
    -----------
    init_round initialised CribbageRound Object    
    """
    round_1 = init_round

    round_1.deal()

    assert len(round_1.pone.hand.cards)==6 
    assert len(round_1.dealer.hand.cards)==6 
    assert len(round_1.cut_card.cards)==1 


def test_round_set_game(init_round):
    """behaviour : each set of cards should be stored in a dict, and it should be possible to 
                   replay a set of cards for a round 
                   
    Given : a round object and a set of pre determined hands 
    when : at the start of the round 
    then : deal the specified cards to each player
    
    Parameters: 
    -----------
    init_round initialised CribbageRound Object
    """
    round_1 = init_round
    
    pone_hand,dealer_hand,cut_card,deck=deal()
    
    set_game = {'pone_hand':pone_hand,
                'dealer_hand' : dealer_hand,
                'cut_card' : cut_card,
                'deck' : deck}
    
    #first check that the right cards were dealt, 
    #i.e. for_set_game is the same as set_game 
    for_set_game = round_1.deal(set_game)
    for key in for_set_game.keys():
        for card1,card2 in zip(for_set_game[key].cards,set_game[key].cards):
            assert card1.__str__() == card2.__str__() 
    
    #then check that the set_game hands end up in the player's hands 
    for hand in ['pone','dealer','cut_card']:
        obj  = getattr(round_1,hand)
        if 'card' in hand:
            extra=''
            obj2=obj
        else:
            extra='_hand'
            obj2 = getattr(obj,'hand')
        for card1,card2 in zip(set_game[hand+extra].cards,obj2.cards):
            assert card1.__str__() == card2.__str__() 
 

def test_round_discard(init_round):    
    """#behaviour : round should be able to discard to the crib
    Given : a round object
    when : after the deal 
    then : each player moves 2 cards to the crib   
    
    Parameters: 
    -----------
    init_round initialised CribbageRound Object
    """
    round_1= init_round

    round_1.deal()
    round_1.discard()
    
    assert len(round_1.crib.cards)==4 
    assert len(round_1.pone.hand.cards)==4 
    assert len(round_1.dealer.hand.cards)==4 


def test_round_the_play(init_round):
    """
    #behaviour :round should be able to execute the play
    Given : a round object
    when : after the discard 
    then : 'the play' phase should happen. The dealer always gets at least one point
    
    Parameters: 
    -----------
    init_round initialised CribbageRound Object
    """
    round_1=init_round


    round_1.deal()
    round_1.discard()
    
    round_1.the_play()

    assert round_1.dealer.score >0
    

def test_round_the_show(init_round):
    """
    #behaviour :round should be able to execute the show
    Given : a round object
    when : after the play 
    then : 'the show' phase should happen.The players scores should be incremented 
    based on how many points they get in the show
    
    Parameters: 
    -----------
    init_round initialised CribbageRound Object
    """
    round_1=init_round


    round_1.deal()
    round_1.discard()
    
    show = round_1.the_show()

    assert show.pone_score == round_1.pone.score 
    assert show.dealer_score == round_1.dealer.score 


