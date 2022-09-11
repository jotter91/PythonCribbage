"""these tests test the scores for the show part of cribbage """
from pycribbage import deck_tools,scorer

def test_scorer_pairs_etc():
    """
    behaviour for test 1a : check that pairs, three-of-a-kind and four-of-akind are scored correctly
    given : hand with a pair, three-of-a-kind or a four-of-a-kind
    when : a score of the hand is needed
    then : return 2 for a pair, 6 for a three-of-a-kind and 12 for a four-of-a-kind
    """
    
    #pair
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 8))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 2
    
    #three-of-a-kind
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(2, 1))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 8))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 6

    #four-of-a-kind
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(2, 1))
    hand.cards.append(deck_tools.Card(3, 1))
    hand.cards.append(deck_tools.Card(0, 8))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 12



def test_scorer_runs():
    """behaviour for test 1b score runs from a hand 
    given : hand which features a multi card run 
    when : a score is required 
    then : return the score for the runs in the hand
    There are several scenarios for this
    a run of 5
    a run of 4
    a run of 3
    multiple runs of 4
    multiple runs of 3
    """
    
    #5 card run - no flush so make sure not all the same suit and no 15s
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 13))
    hand.cards.append(deck_tools.Card(1, 12))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 9))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 5

    #4 card run - no flush so make sure not all the same suit and no 15s
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 12))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 9))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 4
    
    #3 card run - no flush so make sure not all the same suit and no 15s
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 2))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 9))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 3
    
    #2x3 card run - no flush so make sure not all the same suit and no 15s
    #but this has to have a pair so add an extra two points 
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(1, 9))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 9))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 8
    
    #2x4 card run - no flush so make sure not all the same suit and no 15s
    #but this has to have a pair
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 12))
    hand.cards.append(deck_tools.Card(1, 9))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 9))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 10

    #3x3 card run - no flush so make sure not all the same suit and no 15s
    #but this has to have a three-of-a-kind
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 9))
    hand.cards.append(deck_tools.Card(1, 9))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(0, 9))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 15


def tests_score_15s():
    """behaviour for test 1c : check 15s  from 5 cards,4, 3, 2,2x3,2x2
    given : hand which features cards that sum to 15 
    when : a score is required 
    then : return the score for the 15s in the hand
    There are several scenarios for this
    15 from 2 cards, 
    15 from 3 cards,
    15 from 4 cards,
    15s from 2 cards 3 times, and a 5 card 15
    """

    #2 cards
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(1, 5))
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(0, 3))
    hand.cards.append(deck_tools.Card(0, 8))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 2

    #3 cards
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 11))
    hand.cards.append(deck_tools.Card(1, 3))
    hand.cards.append(deck_tools.Card(1, 2))
    hand.cards.append(deck_tools.Card(0, 9))
    hand.cards.append(deck_tools.Card(3, 8))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 2
    
    #4 cards (plus a two card pair)
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 8))
    hand.cards.append(deck_tools.Card(1, 2))
    hand.cards.append(deck_tools.Card(1, 4))
    hand.cards.append(deck_tools.Card(0, 1))
    hand.cards.append(deck_tools.Card(0, 6))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 4
    
    #3x2 cards, 1x3 plus a three of a kind 
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(0, 10))
    hand.cards.append(deck_tools.Card(1, 5))
    hand.cards.append(deck_tools.Card(2, 5))
    hand.cards.append(deck_tools.Card(3, 5))
    hand.cards.append(deck_tools.Card(0, 6))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 14

def test_score_flush():
    """behaviour for test : scorer should be able to score a flush 
    given : hand which features a flush 
    when : a score is required 
    then : return the score for the flush 
    
    If the hand not the crib, then 4 cards of the same suit are needed
    If the hand is a crib then 5 cards of the same suit are need
    """
    #two cases not crib then only need 4
    
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(1, 3))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(1, 12))
    hand.cards.append(deck_tools.Card(0, 6))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 4

    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(1, 3))
    hand.cards.append(deck_tools.Card(1, 13))
    hand.cards.append(deck_tools.Card(1, 12))
    hand.cards.append(deck_tools.Card(1, 6))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 5
    
    #if it is crib then need 5
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(1, 3))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(1, 12))
    hand.cards.append(deck_tools.Card(0, 6))

    s = scorer.ScoreTheShow(hand,is_crib=True)
    assert s.score == 0

    #if it is crib then need 5
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(1, 3))
    hand.cards.append(deck_tools.Card(1, 13))
    hand.cards.append(deck_tools.Card(1, 12))
    hand.cards.append(deck_tools.Card(1, 6))

    s = scorer.ScoreTheShow(hand,is_crib=True)
    assert s.score == 5

def test_score_nobs():
    """behaviour for test : scorer should be able to score 'hob's
    given : hand which features a jack of the same suit as the cut card
    when : a score is required 
    then : return the score for the 'nob'
    
    note that the cut card is assumed to be the last card in the hand
    """
    hand = deck_tools.Hand()
    hand.cards.append(deck_tools.Card(1, 1))
    hand.cards.append(deck_tools.Card(1, 3))
    hand.cards.append(deck_tools.Card(0, 12))
    hand.cards.append(deck_tools.Card(1, 11))
    hand.cards.append(deck_tools.Card(1, 6))

    s = scorer.ScoreTheShow(hand)
    assert s.score == 1
