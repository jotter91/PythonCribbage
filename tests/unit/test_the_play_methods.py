from pycribbage import the_play_methods, deck_tools

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
def test_the_play_method_choose():
    """behaviour - the play method should choose a legit card to play - or return None
    given : a hand and cards on the table 
    when : it is the players turn 
    then : an index of the card to be played should be returned.
           if no card can be played (as it would make the sum > than31) 
           then None should be returned
    """
    
    #first example where the player can only play the 3  of clubs 
    player_hand,on_table = example_hand_1_play()

    method = the_play_methods.ThePlayMethod()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    assert method.table_sum ==26
    assert method.assess_validity() ==[1]
    assert method.choose_play() == 1

    #second example where no card can be played as it would make the sum >31 
    player_hand,on_table = example_hand_no_play()


    method = the_play_methods.ThePlayMethod()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    assert method.table_sum ==26
    assert method.choose_play() == None






def test_main_the_play_random_method():

    """behaviour - the play random method should only let the player choose a legit card (sum <31) to play
                    if no cards to be played it should return -1 
    given : a hand and cards on the table 
    when : it is the players turn 
    then : an index of the card to be played should be returned.
           if no card can be played (as it would make the sum > than31) 
           then None should be returned
    """
    
    #first example where the player can only play the 3  of clubs 
    player_hand,on_table = example_hand_1_play()

    method = the_play_methods.RandomThePlay()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    to_play = method.choose_play() 

    assert method.table_sum ==26
    assert method.assess_validity() ==[1]
    assert to_play == 1
    
    #second example where the player can only two cards 
    player_hand,on_table = example_hand_2_plays()

    method = the_play_methods.RandomThePlay()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    to_play =method.choose_play() 

    assert method.table_sum ==26
    assert method.assess_validity() ==[1,2]
    assert to_play == 2 or to_play ==1
    
    #third example where no card can be played as it would make the sum >31 
    player_hand,on_table = example_hand_no_play()

    method = the_play_methods.RandomThePlay()
    method.update_hand(player_hand)
    method.update_on_table(on_table)
    
    to_play =method.choose_play() 
    assert method.table_sum ==26
    assert to_play == None


def test_main_the_play_human_method(monkeypatch):
    """behaviour - the play human method should only let the player choose a legit card (sum <31) to play
                    if no cards to be played it should return -1
    given : a hand and cards on the table
    when : it is the players turn
    then : an index of the card to be played should be returned.
           if no card can be played (as it would make the sum > than31)
           then None should be returned
    """

    # first example where the player can only play the 3  of clubs
    player_hand, on_table = example_hand_1_play()

    method = the_play_methods.HumanThePlay()
    method.update_hand(player_hand)
    method.update_on_table(on_table)

    responses = iter(['\n'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_play = method.choose_play()

    assert method.table_sum == 26
    assert method.assess_validity() == [1]
    assert to_play == 1

    # second example where the player can only two cards
    player_hand, on_table = example_hand_2_plays()

    method = the_play_methods.HumanThePlay()
    method.update_hand(player_hand)
    method.update_on_table(on_table)

    responses = iter(['a', '0', '-1', '2'])  # add in some junk
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_play = method.choose_play()

    assert method.table_sum == 26
    assert method.assess_validity() == [1, 2]
    assert to_play == 2

    # third example where no card can be played as it would make the sum >31
    player_hand, on_table = example_hand_no_play()

    method = the_play_methods.ThePlayMethod()
    method.update_hand(player_hand)
    method.update_on_table(on_table)

    responses = iter(['\n'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    to_play = method.choose_play()
    assert method.table_sum == 26
    assert to_play == None


def test_human_play_inputs():
    """behaviour to test : the input should only be ints in the valid list
    Given : an int
    When : after input
    then : check if it is in the supplied list, should also only be an int
    """
    bot = the_play_methods.HumanThePlay()

    assert bot.is_input_ok(0, [0, 1]) == True
    assert bot.is_input_ok(-1, [0, 1]) == False
    assert bot.is_input_ok(6, [0, 2]) == False
    assert bot.is_input_ok('a', [0, 2]) == False