from pycribbage import deck_tools



def test_card_string_representation():
    """behaviour to test : a card needs to be output as a card as human readable string 
    Given : a desired suit and rank
    when : need to display the card as a string
    then : should get a nice human readable string
    """
    ace_of_spades = deck_tools.Card(3,1)
    assert ace_of_spades.__str__()=='%s of %s'%('Ace','Spades') 


def test_card_face_value():   
    """
    behaviour to test : need to know a card's face value 
    Given : a card 
    when : need to obtain its face value
    then : should return the  integer face value  
    """
    ace_of_spades = deck_tools.Card(3,1)
    assert ace_of_spades.face_value ==1
    
    jack_of_hearts = deck_tools.Card(2,11)
    assert jack_of_hearts.face_value ==10
    
    ten_of_diamonds = deck_tools.Card(1,10)
    assert ten_of_diamonds.face_value ==10



def test_shuffle_deck():
    """
    behaviour to test : a deck must be able to be shuffled to give a random order
    given : a deck is required
    when  : a deck is to be shuffled
    then  : create new deck and shuffle to get new random deck
    """

    #TODO: this is a poor test as it is possible to shuffle to get the same deck
    new_deck = deck_tools.Deck() 
    first_order = new_deck.__str__()
    new_deck.shuffle()
    assert new_deck.__str__() != first_order


def test_remove_from_deck():
    """
    behaviour to test : remove card from deck 
    given : card suit and rank and a full deck
    when : a card is to be removed 
    then : remove from the deck
    """
    new_deck = deck_tools.Deck()
    ace_of_spades = deck_tools.Card(3,1)
    
    for i,card in enumerate(new_deck.cards):
        if card.__str__() == '%s of %s' % ('Ace','Spades'):
            index=i
    
    new_deck.remove_card(new_deck.cards[index])

    assert '%s of %s'%('Ace','Spades') not in new_deck.__str__()


def test_remove_from_deck():
    """behaviour to test : deal n cards into a hand 
    given : number of cards for a hand 
    when : a hand is to be dealt 
    then : remove from the deck and place into the hand
    """
    new_deck = deck_tools.Deck()
    hand = deck_tools.Hand()
    n=6

    new_deck.move_cards(hand,n)

    for i in range(n):
        assert hand.cards[i].__str__() not in new_deck.__str__()

