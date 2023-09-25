from pycribbage.cribbage_tools import deal,cut_for_crib,switch_dealer,create_set_game,save_set_game,load_set_game
from pycribbage import deck_tools
import os 

def test_deal():
    """behaviour to test : From a shuffled deck deal two 6 hands to the pone and dealer. Also create a cut card
    given : no prerequisites
    when  : cards are to be dealt
    then  : deal 6 cards to each hand, and one to a cut card 
    """

    pone_hand,dealer_hand,cut_card,deck = deal()

    assert len(pone_hand.cards)==6
    assert len(dealer_hand.cards)==6
    assert len(cut_card.cards)==1
    assert len(deck.cards)==(52-13)

    #TODO also check they are unique? should be ok as other tests have verified that cards leave the deck 
    

def test_cut_cards():
    """behaviour to test : choose dealer based on cut cards. 
                            this should a random process
    given : a game is about to start 
    when : a dealer is to be choosen 
    then : allocate dealer based on the cutting of a deck, this should be 50-50
    
    """
    
    dealer,out_string= cut_for_crib()

    assert dealer=='player_1' or dealer =='player_2'
    assert 'dealer' in out_string
    
    #do 1000 tests and see what the number for each is 
    n_player_1=0
    n_player_2=0

    for i in range(1000):
        dealer,out_string = cut_for_crib()
        if dealer=='player_1':
            n_player_1 = n_player_1 +1
        if dealer=='player_2':
            n_player_2 = n_player_2 +1
            
    #give some leeway  - not very precise
    #not the best test tbh, not very rigorous! 
    
    assert n_player_1 >450
    assert n_player_2 <550

def test_switch_dealer(init_players):
    """behaviour to test : should be able to switch which player is dealer
    given : two players
    when : end of round and dealers is to be switched
    then : switch dealer from 1 to 2, or vice versa. Only one dealer allowed 
    
    Parameters
    ------------
    init_players, tuple 
        tuple of Player objects
    
    """
    player_1,player_2 = init_players   
    
    switch_dealer(player_1,player_2)
    
    assert player_1.is_dealer ==True
    assert player_2.is_dealer ==False

def test_create_set_game():
    """behaviour to test : should be able to create a set game for a given number of rounds
    given : number of rounds 
    when : need set game
    then : create set game dictionary
   
    
    """
    set_game = create_set_game(20)

    assert len(set_game.keys()) ==20
    for key in set_game.keys():
        for name in ['pone_hand','dealer_hand','cut_card','deck']:
            assert isinstance(set_game[key][name],deck_tools.Deck)==True

def test_save_and_read_set_game(tmp_path):
    """behaviour to test : should be able to save and load a set game
    given : number of rounds 
    when : need set game
    then : create set game dictionary, save and then load 
   
    Parameters
    -----------
    tmp_path, str 
        location of temporary path 
    """    
    set_game = create_set_game(20)
    fname = os.path.join(tmp_path,'set_game.pickle')
   
    save_set_game(set_game,fname)
    
    set_game_load = load_set_game(fname)
    
    for i in range(20):
        for name in ['pone_hand','dealer_hand','cut_card','deck']:
            for card_load,card in zip( set_game_load[i][name].cards,set_game[i][name].cards):
                assert card_load.__str__() ==card.__str__()


