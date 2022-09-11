"""global behaviours to test : given two hands play out 'ThePlay' part of a cribbage round
tests are ordered in terms of when they should happen in The play phase. """
from pycribbage import the_play,deck_tools
import pytest


@pytest.fixture()
def init_play_ex_1(init_play):
    """initialise two players with a set hand 
    pone   : Ace of Clubs, Ace of Diamonds
    dealer : Ace of Hearts, Ace of Spades
    Returns 
    ----------
    play, ThePlay object 
    """
    play = init_play
    
    pone_hand = deck_tools.Hand()
    pone_hand.cards.append(deck_tools.Card(0, 1))
    pone_hand.cards.append(deck_tools.Card(1, 1))


    dealer_hand = deck_tools.Hand()
    dealer_hand.cards.append(deck_tools.Card(2, 1))
    dealer_hand.cards.append(deck_tools.Card(3, 1))

    play.pone.update_hand(pone_hand)
    play.dealer.update_hand(dealer_hand)
    
    play.play()
    
    return play
    


def test_the_play_pone_lead(init_play):
    """
    behaviour 1 : pone should always lead (play the first card)
    given : each player has been dealt cards, and the dealer is known 
    when : start of the play phase
    then : pone should be the first player to put a card down 
    """
    play = init_play

    assert play.active_player=='pone'


def test_the_play_alternative_plays(init_play_ex_1):
    """"
    behaviour 2: players should add to the table alternatively - unless the sum is greater than 31
    Given: two hands 
    When : during the player 
    Then : if the sum is less than 31 the players should add alternate cards to the table 
    """
    play = init_play_ex_1 
    assert play.on_table.cards[0].__str__() == 'Ace of Clubs' 
    assert play.on_table.cards[1].__str__()== 'Ace of Hearts' 
    assert play.on_table.cards[2].__str__()== 'Ace of Diamonds' 
    assert play.on_table.cards[3].__str__()== 'Ace of Spades' 


def test_the_play_score(init_play_ex_1):
    """behaviour 3 :the scores should be advanced according to the rules
    Given : cards on the table
    When : after each card has been played 
    Then : the player's score should be updated if they have some points
    """
    play = init_play_ex_1 
    pone_hand = deck_tools.Hand()
    pone_hand.cards.append(deck_tools.Card(0, 1))
    pone_hand.cards.append(deck_tools.Card(1, 1))


    dealer_hand = deck_tools.Hand()
    dealer_hand.cards.append(deck_tools.Card(2, 1))
    dealer_hand.cards.append(deck_tools.Card(3, 1))
    #in this case pone has played a three of a kind so should have 6 points 
    assert play.pone.score == 6 
    

def test_the_play_go(init_play):
    """behaviour 4: player must say go if they can't play a card, and a point is awarded to the other player 
    Given : cards on the table 
    When : before each play 
    then : if the player cannot add a card they must say go and the other player is awarded a point 
    """
    #TODO : make this into a function
    play = init_play

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

    play.pone.update_hand(pone_hand)
    play.dealer.update_hand(dealer_hand)
    play.play()
    
    assert play.pone.score == 7 
    assert play.dealer.score == 7 




def test_the_play_return_cards(init_players):
    """behaviour to test : cards should be returned to each player after the play
    Given : cards on the table after the play
    When : the play is over 
    Then : return cards to player's hand 
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

    
    player_1,player_2 = init_players
    player_1.update_hand(pone_hand)
    player_2.update_hand(dealer_hand)
    play =the_play.ThePlay(player_1,player_2)
    

    play.play()
    
    assert len(play.pone.hand.cards) ==4
    assert len(play.dealer.hand.cards) ==4

