"""global behaviours to test : given two hands play out 'ThePlay' part of a cribbage round
tests are ordered in terms of when they should happen in The play phase. """
from pycribbage import deck_tools
import pytest


@pytest.fixture()
def init_play_ex_1(init_game):
    """initialise two players with a set hand 
     
    pone   : Ace of Clubs, Ace of Diamonds
    dealer : Ace of Hearts, Ace of Spades
    
    Parameters
    ------------
    init_game : CribbageGame object
        initialised game object

    Returns 
    ----------
    game, CribbageGame object 
    """
    
    pone_hand = deck_tools.Hand()
    pone_hand.cards.append(deck_tools.Card(0, 1))
    pone_hand.cards.append(deck_tools.Card(1, 1))


    dealer_hand = deck_tools.Hand()
    dealer_hand.cards.append(deck_tools.Card(2, 1))
    dealer_hand.cards.append(deck_tools.Card(3, 1))

    game=init_game
    game.player_1.update_hand(pone_hand)
    game.player_2.update_hand(dealer_hand)
    game.set_pone_dealer()

    
    return game
    
@pytest.fixture()
def init_play_ex_2(init_game):
    """initialise two players with a set hand 
     
    pone   : 10 of Clubs, 10 of Diamonds, Jack of Diamonds, Jack of Hearts 
    dealer : 10 of Hearts, 10 of Spades, Queen of Spades, King of Spades 

    
    Parameters
    ------------
    init_game : CribbageGame object
        initialised game object

    Returns 
    ----------
    game, CribbageGame object 
    """
    
    pone_hand = deck_tools.Hand()
    pone_hand.cards.append(deck_tools.Card(0, 10))
    pone_hand.cards.append(deck_tools.Card(1, 10))
    pone_hand.cards.append(deck_tools.Card(1, 11))
    pone_hand.cards.append(deck_tools.Card(2, 11))


    dealer_hand = deck_tools.Hand()
    dealer_hand.cards.append(deck_tools.Card(2, 10))
    dealer_hand.cards.append(deck_tools.Card(3, 10))
    dealer_hand.cards.append(deck_tools.Card(3, 12))
    dealer_hand.cards.append(deck_tools.Card(3, 13))

    game=init_game
    game.player_1.update_hand(pone_hand)
    game.player_2.update_hand(dealer_hand)
    game.set_pone_dealer()

    
    return game


def test_the_play_pone_lead(init_play_ex_1):
    """
    behaviour 1 : pone should always lead (play the first card)
    given : each player has been dealt cards, and the dealer is known 
    when : start of the play phase
    then : pone should be the first player to put a card down 
    """

    assert init_play_ex_1.active_player_str =='pone'


def test_the_play_alternative_plays(init_play_ex_1):
    """"
    behaviour 2: players should add to the table alternatively - unless the sum is greater than 31
    Given: two hands 
    When : during the player 
    Then : if the sum is less than 31 the players should add alternate cards to the table 
    """
    game = init_play_ex_1 
    game.the_play()
    assert game.on_table.cards[0].__str__() == 'Ace of Clubs' 
    assert game.on_table.cards[1].__str__()== 'Ace of Hearts' 
    assert game.on_table.cards[2].__str__()== 'Ace of Diamonds' 
    assert game.on_table.cards[3].__str__()== 'Ace of Spades' 


def test_the_play_score(init_play_ex_1):
    """behaviour 3 :the scores should be advanced according to the rules
    Given : cards on the table
    When : after each card has been played 
    Then : the player's score should be updated if they have some points
    """
    game = init_play_ex_1 
    game.the_play()
    assert game.pone.score == 6 
    

def test_the_play_go(init_play_ex_2):
    """behaviour 4: player must say go if they can't play a card, and a point is awarded to the other player 
    Given : cards on the table 
    When : before each play 
    then : if the player cannot add a card they must say go and the other player is awarded a point 
    """
    game= init_play_ex_2
    game.the_play() 
    assert game.pone.score == 7 
    assert game.dealer.score == 7 




def test_the_play_return_cards(init_play_ex_2):
    """behaviour to test : cards should be returned to each player after the play
    Given : cards on the table after the play
    When : the play is over 
    Then : return cards to player's hand 
    """
    game = init_play_ex_2
    game.the_play()
    assert len(game.pone.hand.cards) ==4
    assert len(game.dealer.hand.cards) ==4

