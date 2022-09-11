"""global behaviour to test : for a set of cards during 'The Play'/pegging return the score"""

from pycribbage import deck_tools,scorer



def test_ScoreThePlay_pairs_etc():
    """behaviour to test : scoring  pairs,threes and,fours in the play
    Given : cards 'on the table' during the play 
    when : a score is needed
    then : add two points for a pair, six for a three-of-a-kind and 12 for a four-of-a-kind
    """

    #pair
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 1))
    on_table.cards.append(deck_tools.Card(1, 1))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 2

    #threes
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 1))
    on_table.cards.append(deck_tools.Card(1, 1))
    on_table.cards.append(deck_tools.Card(2, 1))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 6

    #fours
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 1))
    on_table.cards.append(deck_tools.Card(1, 1))
    on_table.cards.append(deck_tools.Card(2, 1))
    on_table.cards.append(deck_tools.Card(3, 1))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 12

def test_ScoreThePlay_sums():
    """behaviour to test : score 15s and 31s in the play 
    Given : cards 'on the table' during the play 
    when : a score is needed
    then : add two points for a 15 and one a 31, return -1 if the sum is over 31
    """
    
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 10))
    on_table.cards.append(deck_tools.Card(1, 5))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 2

    
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 10))
    on_table.cards.append(deck_tools.Card(1, 11))
    on_table.cards.append(deck_tools.Card(1, 13))
    on_table.cards.append(deck_tools.Card(1, 1))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 1

    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 10))
    on_table.cards.append(deck_tools.Card(1, 11))
    on_table.cards.append(deck_tools.Card(1, 13))
    on_table.cards.append(deck_tools.Card(2, 13))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == -1

def test_ScoreThePlay_runs():
    """behaviour to test scoring  runs in the play
    Given : cards 'on the table' during the play 
    when : a score is needed
    then : return score for the number of consecutive cards
    """
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 3))
    on_table.cards.append(deck_tools.Card(1, 6))
    on_table.cards.append(deck_tools.Card(1, 7))
    on_table.cards.append(deck_tools.Card(1, 8))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 3
    
    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 1))
    on_table.cards.append(deck_tools.Card(1, 2))
    on_table.cards.append(deck_tools.Card(1, 3))
    on_table.cards.append(deck_tools.Card(1, 4))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 4


    on_table = deck_tools.Hand()
    on_table.cards.append(deck_tools.Card(0, 1))
    on_table.cards.append(deck_tools.Card(1, 9))
    on_table.cards.append(deck_tools.Card(1, 3))
    on_table.cards.append(deck_tools.Card(1, 4))

    s = scorer.ScoreThePlay(on_table)
    assert s.score == 0


