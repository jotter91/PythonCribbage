from pycribbage import discard_methods
from pycribbage import deck_tools
from pycribbage.cribbage_tools import deal
#TODO: make this a class?
def test_discard():
    """behaviour to test : a bot should discard two unique cards to crib and leave four in the hand
    given : a hand 
    when : two cards need to discarded
    then : return two indices of the cards to discard
    """
    
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(2, 1))
    hand.cards.append(deck_tools.Card(3, 1))
    hand.cards.append(deck_tools.Card(3, 10))
    hand.cards.append(deck_tools.Card(2, 10))

    bot = discard_methods.Discard()
    bot.update_hand(hand)
    to_discard = bot.choose_discard()

    assert len(to_discard)==2
    assert to_discard[0] != to_discard[1]
    for i in [0,1]:
        assert type(to_discard[i])==int



def test_discard_random():
    """behaviour to test : a bot should discard two unique cards to crib and leave four in the hand.
    this bot should allocate the indices randomly 
    given : a hand 
    when : two cards need to discarded
    then : return two indices of the cards to discard
    """
    
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(2, 1))
    hand.cards.append(deck_tools.Card(3, 1))
    hand.cards.append(deck_tools.Card(3, 10))
    hand.cards.append(deck_tools.Card(2, 10))

    bot = discard_methods.RandomDiscard()
    bot.update_hand(hand)
    to_discard = bot.choose_discard()

    assert len(to_discard)==2
    assert to_discard[0] != to_discard[1]
    for i in [0,1]:
        assert type(to_discard[i])==int

