from pycribbage.api import human_methods
from pycribbage import  deck_tools
from pycribbage import deck_tools

#TODO : replace these 
def example_hand_1_play():
    """return an example hand for testing the play methods 
    on the table the sum is 26 and the player only has one legal play, the 3 of clubs
    
    Returns
    ----------
    player_hand, Hand
        object representing the players hand 
    on_table, Hand 
        object representing the cards on the table 
    """
    
    player_hand = deck_tools.Hand()
    player_hand.cards.append(deck_tools.Card(0, 10))
    player_hand.cards.append(deck_tools.Card(0, 3))
    
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(1, 10))
    on_table.cards.append(deck_tools.Card(2, 10))
    on_table.cards.append(deck_tools.Card(3, 6))
    
    return player_hand,on_table
    
def example_hand_no_play():
    """return an example hand for testing the play methods 
    on the table the sum is 26 and the player has now legal play, the 3 of clubs
    
    Returns
    ----------
    player_hand, Hand
        object representing the players hand 
    on_table, Hand 
        object representing the cards on the table 
    """
    
    player_hand = deck_tools.Hand()
    player_hand.cards.append(deck_tools.Card(0, 10))
    player_hand.cards.append(deck_tools.Card(0, 10))
    
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(1, 10))
    on_table.cards.append(deck_tools.Card(2, 10))
    on_table.cards.append(deck_tools.Card(3, 6))
    
    return player_hand,on_table
    
def example_hand_2_plays():
    """return an example hand for testing the play methods 
    on the table the sum is 26 and the player only has two legal plays, 
    the 3 of clubs or 3 of Diamonds
    
    Returns
    ----------
    player_hand, Hand
        object representing the players hand 
    on_table, Hand 
        object representing the cards on the table 
    """
    
    player_hand = deck_tools.Hand()
    player_hand.cards.append(deck_tools.Card(0, 10))
    player_hand.cards.append(deck_tools.Card(0, 3))
    player_hand.cards.append(deck_tools.Card(1, 3))
    
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(1, 10))
    on_table.cards.append(deck_tools.Card(2, 10))
    on_table.cards.append(deck_tools.Card(3, 6))
    
    return player_hand,on_table   

def test_main_the_play_human_method(monkeypatch):

    """behaviour - the play human method should only let the player choose a legit card (sum <31) to play
                    if no cards to be played it should return -1 
    given : a hand and cards on the table 
    when : it is the players turn 
    then : an index of the card to be played should be returned.
           if no card can be played (as it would make the sum > than31) 
           then None should be returned
    """
    
    #first example where the player can only play the 3  of clubs 
    player_hand,on_table = example_hand_1_play()

    method = human_methods.HumanThePlay()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    responses = iter(['\n'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_play = method.choose_play() 

    assert method.table_sum ==26
    assert method.assess_validity() ==[1]
    assert to_play == 1
    
    #second example where the player can only two cards 
    player_hand,on_table = example_hand_2_plays()

    method = human_methods.HumanThePlay()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    responses = iter(['a','0','-1','2']) #add in some junk
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_play =method.choose_play() 

    assert method.table_sum ==26
    assert method.assess_validity() ==[1,2]
    assert to_play == 2
    
    #third example where no card can be played as it would make the sum >31 
    player_hand,on_table = example_hand_no_play()

    method = human_methods.ThePlayMethod()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    responses = iter(['\n'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_play =method.choose_play() 
    assert method.table_sum ==26
    assert to_play == None
    
def test_human_play_inputs():
    """behaviour to test : the input should only be ints in the valid list
    Given : an int
    When : after input 
    then : check if it is in the supplied list, should also only be an int
    """
    bot = human_methods.HumanThePlay()
    
    assert bot.is_input_ok(0,[0,1]) == True
    assert bot.is_input_ok(-1,[0,1]) == False
    assert bot.is_input_ok(6,[0,2]) == False
    assert bot.is_input_ok('a',[0,2]) == False
        
    
def test_human_discard_inputs():
    """behaviour to test : the input should only ints between 0 and 5
    Given : an int
    When : after input 
    then : check if it is an int between 0-5
    """
    bot = human_methods.HumanDiscard()
    
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

    bot = human_methods.HumanDiscard()
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