from pycribbage import player,discard_methods,the_play_methods
from pycribbage import deck_tools 
import pytest


def test_player_init(init_players):
    """behaviour to test : a player should be created 
    Given : player inputs 
    When  : a player is created
    Then  : create player with a score of 0, a discard and the play method and the dealer should not be allocated yet
    """
    player_1 = player.Player('Player 1',
                             discard_methods.Discard(),
                             the_play_methods.ThePlayMethod() )

    assert player_1.name =='Player 1'
    assert player_1.is_dealer ==False
    assert player_1.score ==0
    assert isinstance(player_1.discard_method ,discard_methods.Discard) == True 
    assert isinstance(player_1.the_play_method,the_play_methods.ThePlayMethod) == True 


def test_player_score(init_players):
    """behaviour to test : increment players score
    given : points to be added a player's score
    when : update requested
    then :score should be incremented
    """

    player_1,_ = init_players 

    player_1.update_score(1)

    assert player_1.score ==1


def test_player_add_to_hand(init_players):
    """behaviour to test : update a players hand
    Given : a change to players hand 
    When : before any other moves by the player 
    Then : update the players hand 
    """
    player_1,_=init_players

    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0,1))
    player_1.update_hand(hand)

    assert player_1.hand.cards[0].__str__() =='Ace of Clubs'



def test_player_move_to_card(init_players):
    """behaviour to test : move to the table
    Given : play needs to move  cards
    When : before the end of the players turn 
    Then : move to another hand 
    """
    player_1,_=init_players

    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0,1))
    hand.cards.append(deck_tools.Card(0,2))
    player_1.update_hand(hand)
    
    table = deck_tools.Hand()

    player_1.move_to_table(0,table)

    assert len(table.cards)==1
    assert len(player_1.hand.cards)==1
    
def test_player_move_to_card(init_players):
    """behaviour to test : move to the crib
    Given : play needs to move  cards to the crib
    When : before the play 
    Then : move to crib
    """
    player_1,_=init_players

    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0,1))
    hand.cards.append(deck_tools.Card(0,2))
    player_1.update_hand(hand)
    
    crib = deck_tools.Hand()

    player_1.move_to_crib([0,1],crib)

    assert len(crib.cards)==2
    assert len(player_1.hand.cards)==0


def test_player_raise_game_over(init_players):
    """behaviour to test : game should be stopped if the score is over 121
    Given : a player has updated their score 
    when : each time the score is incremented 
    then : raise execption to say the game is over 
    """
    player_1,_=init_players

    with pytest.raises(Exception) as e_info:
        player_1.update_score(121)

def test_game_score_init_dealer(init_players):
    """ behaviour to test : set dealers after initialising the players
    given : a dealer has been chosen
    when : the game is about to start
    then : the dealer should be assigned to one player only 
    """
    player_1,player_2 = init_players   
    player_1.set_dealer(True) 
    player_2.set_dealer(False) 
    
    assert player_1.is_dealer ==True
    assert player_2.is_dealer ==False
    

