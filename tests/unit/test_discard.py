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

def test_human_discard_inputs():
    """behaviour to test : the input should only ints between 0 and 5
    Given : an int
    When : after input 
    then : check if it is an int between 0-5
    """
    bot = discard_methods.HumanDiscard()
    
    assert bot.is_input_ok(0) == True
    assert bot.is_input_ok(-1) == False
    assert bot.is_input_ok(6) == False
    assert bot.is_input_ok('a') == False
    
    """behaviour to test : the dicard indicies should be unique
    Given : a list of  ints
    When : after input 
    then : return False if the are the same, True if unique 
    """
    
    assert bot.are_inputs_unique([0,1])==True
    assert bot.are_inputs_unique([0,0])==False

def test_human_discard(monkeypatch):
    """ behaviour to test : human should be able to choose two cards to discard
    Given : a hand 
    When : two cards are to be discarded
    Then : print the hand with each index, ask user for the integers which correspond to 
           the card indicies, return these as a list 
    
    Parameters
    -----------
    monkeypatch
        monkeypatch object to handle stdin
    """
    def check_to_discard(to_discard): 
        assert len(to_discard)==2
        assert to_discard[0] != to_discard[1]
        for i in [0,1]:
            assert type(to_discard[i])==int


    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(2, 1))
    hand.cards.append(deck_tools.Card(3, 1))
    hand.cards.append(deck_tools.Card(3, 10))
    hand.cards.append(deck_tools.Card(2, 10))

    bot = discard_methods.HumanDiscard()
    bot.update_hand(hand)

    responses = iter(['0','1'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_discard = bot.choose_discard()

    check_to_discard(to_discard)

    #handle case where first input is not correct
    responses = iter(['a','1','2'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_discard = bot.choose_discard()
    
    check_to_discard(to_discard)

    #handle case where inputs are not unique
    responses = iter(['1','1','1','2'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_discard = bot.choose_discard()

    check_to_discard(to_discard)

    #handle case where inputs are not unique an a string is given
    responses = iter(['a','1','1','2','3'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_discard = bot.choose_discard()
    
    check_to_discard(to_discard)

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

