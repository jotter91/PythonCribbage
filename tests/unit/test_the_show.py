from pycribbage import deck_tools,the_show



def test_the_show(init_game):
    """behaviour to test : scoring a set of hands as part of the show 
    Given : pone hand ,dealer hand  and a cut card 
    When :  a score is needed 
    Then : calculate the score for pone's hand ,dealer's hand, dealer's 
            crib and dealer's total score
    """
    #create an example set of hands 
    pone = deck_tools.Hand()
    pone.cards.append(deck_tools.Card(0, 1))
    pone.cards.append(deck_tools.Card(1, 1))
    pone.cards.append(deck_tools.Card(1, 11))
    pone.cards.append(deck_tools.Card(0, 10))
    

    dealer = deck_tools.Hand()
    dealer.cards.append(deck_tools.Card(0, 2))
    dealer.cards.append(deck_tools.Card(1, 3))
    dealer.cards.append(deck_tools.Card(1, 12))
    dealer.cards.append(deck_tools.Card(0, 13))
    
    crib = deck_tools.Hand()
    crib.cards.append(deck_tools.Card(3, 2))
    crib.cards.append(deck_tools.Card(3, 3))
    crib.cards.append(deck_tools.Card(3, 12))
    crib.cards.append(deck_tools.Card(3, 13))
    
    cut_card = deck_tools.Hand()
    cut_card.cards.append(deck_tools.Card(0, 9))

    #add to game create a game 
    
    init_game.player_1.update_hand(pone)
    init_game.player_2.update_hand(dealer)
    init_game.update_crib(crib)
    init_game.update_cut_card(cut_card)
    init_game.set_pone_dealer()
    pone_score,dealer_hand_score,crib_score,dealer_score,out_string = init_game.the_show()

    assert pone_score ==5
    assert dealer_hand_score ==4
    assert crib_score ==4
    assert dealer_score ==8
    
    output = '''==============================
Pone Hand, Score : 5
==============================
Ace of Clubs
Ace of Diamonds
Jack of Diamonds
10 of Clubs
9 of Clubs
==============================
Dealer Hand, Score 4
==============================
2 of Clubs
3 of Diamonds
Queen of Diamonds
King of Clubs
9 of Clubs
==============================
Crib, Score : 4
==============================
2 of Spades
3 of Spades
Queen of Spades
King of Spades
9 of Clubs
==============================
Final Scores
==============================
Pone : 5  Dealer : 8'''
    assert out_string.strip('\n')==output.strip('\n')
