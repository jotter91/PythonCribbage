from pycribbage import cribbage_game
from pycribbage import cribbage_tools
import os,json

def test_cribbage_game_finish(init_game):
    """behaviour to test : a winner is declared when a player's score goes above 121
    given : an initialised game
    when : a player's score goes above 121
    then : game should declare the winner
    
    Parameters
    ------------
    init_game, CribbageGame 
        CribbageGame  object
    """
    game=init_game

    game.play_game()

    if game.player_1.score >= 121:
        assert game.winner == game.player_1.name
    else:
        assert game.winner == game.player_2.name

def test_cribbage_game_random_game():
    pass


def test_cribbage_game_from_set_game(tmp_path):
    """behaviour to test : a game of cribbage should be able to be played from a 
    pre allocated set of cards for each round (a set game)
    
    given : a set game
    when : after the game 
    then : the cards dealt to each player should be the same as set game
    

    """
    players=[]
    
    player={    'name': 'Player 1',
                'TS_method':'0', 
                'TP_method':'0',}
    players.append(player)
    
    player={    'name': 'Player 2',
                'TS_method':'0', 
                'TP_method':'0',}
    players.append(player)
    
    cwd=os.getcwd()
    os.chdir(tmp_path)
    for i in range(1):
        set_game = cribbage_tools.create_set_game(20)
        game = cribbage_game.CribbageGame(players,set_game =set_game,batch_mode=True)
        game.play_game() 
        
        #first check set_game was set correctly in the CribbageGame class
        for key in set_game.keys():
            for key2 in set_game[key].keys():
                for card1,card2 in zip(set_game[key][key2].cards,game.set_game[key][key2].cards):
                    assert card1.__str__() == card2.__str__()
                    
        #next check that the actual cards played were the same as set game 
        for key in game.for_set_game.keys():

            for key2 in game.for_set_game[key].keys():
                for card1,card2 in zip(game.for_set_game[key][key2].cards,set_game[key][key2].cards):
                    assert card1.__str__() == card2.__str__()

    os.chdir(cwd)

def test_cribbage_game_log_file_creation(init_game,tmp_path):
    """behaviour to test : a unique log file should be created at the start of each  game
       
    given : a cribbage game has been created 
    when: a log file needs to be created
    then : a unique file name should be created 
    
    Parameters
    ------------
    init_game, CribbageGame 
        CribbageGame  object
    tmp_path, str 
        location of temporary path     
    """
    
    game=init_game
    
    game.create_log_file(tmp_path)
    
    assert os.path.isfile(os.path.join(tmp_path,'game000.log'))==True
    
    del game 
    
    #second file should be unique
    game=init_game
    
    game.create_log_file(tmp_path)
    
    assert os.path.isfile(os.path.join(tmp_path,'game001.log'))==True
    
    
    

def test_cribbage_game_logger(init_game,tmp_path):
    """behaviour to test : any outputs should be printed to the console and a log file
       
    given : a cribbage game has been created 
    when: a string is to be logged 
    then : it should be written to a file and printed to the console 
     
    Parameters
    ------------
    init_game, CribbageGame 
        CribbageGame  object
    tmp_path, str 
        location of temporary path      

    """
    
    game=init_game
    
    
    game.logger('a test')
    
    game.close_log_file()
    
    f_log = open('game000.log','r')
    line =f_log.readline()

    assert line =='a test\n'
    
def test_cribbage_game_batch_mode(tmp_path):
    """behaviour to test : in batch mode nothing should be printed to the console
       instead it should be written to a file 
       
   given : a log file name and batch mode flag
   when: at the end of game 
   then : write the contents to a file 
    
    Parameters
    ------------
    tmp_path, str 
        location of temporary path  
    """
    players=[]
    
    player={    'name': 'Player 1',
                'TS_method':'0', 
                'TP_method':'0',}
    players.append(player)
    
    player={    'name': 'Player 2',
                'TS_method':'0', 
                'TP_method':'0',}
    players.append(player)
    
    cwd = os.getcwd()
    
    os.chdir(tmp_path)
    game = cribbage_game.CribbageGame(players,batch_mode=True)
    game.play_game()
    
    f_log = open(os.path.join(tmp_path,'game000.log'),'r')
    lines =f_log.readlines()

    
    os.chdir(cwd)
    
    assert 'Game about to begin' in lines[0]

def test_cribbage_game_check_dealer_switch(init_game_for_round):
    """behaviour to test : the dealer should alternative between P1 and P2 after 
    each round
    given : an initialised game
    when : after each round  
    then : the dealer should alternate between P1 and P2  
    
    Parameters
    ------------
    init_game_for_round, CribbageGame 
        CribbageGame  object
    """
    game=init_game_for_round

    for i in range(3):
        if i % 2 ==0:
            assert game.dealer.name =='Player 1'
        else:
            assert game.dealer.name =='Player 2'

        game.play_round(i)

def test_cribbage_game_reset_table(init_game_for_round):
    """behaviour to test : the table should be empty and table_sum zero before the play starts 
    given : an initialised game
    when : before each round  
    then : the table should be empty, neither player should say not be saying go at the start
    of the round, 
    
    Parameters
    ------------
    init_game_for_round, CribbageGame 
        CribbageGame  object
    """
    game=init_game_for_round
    game.reset_table()
        
    assert game.dealer_go == False
    assert game.pone_go == False
    assert game.go_added == False
    assert game.play_end == False
    
    assert game.table_sum == 0
    assert game.active_player_str =='pone'

    assert len(game.on_table.cards)==0

def test_cribbage_reset_crib_cut(init_game_for_round):
    """behaviour to test : the cut card and crib should be empty at the start of each round 
    given : an initialised game
    when : before each round  
    then : the  crib and cut card should be empty   
    
    Parameters
    ------------
    init_game_for_round, CribbageGame 
        CribbageGame  object
    """
    game=init_game_for_round
    game.reset_crib_and_cut_card()
        
       
    assert len(game.crib.cards)==0
    assert len(game.cut_card.cards)==0

def test_cribbage_game_play_round(init_game_for_round):
    """behaviour to test : after each round the table,crib and cut card should be empty 
    when : before each round  
    then : the table should be empty, neither player should say not be saying go at the start
    of the round, crib should be empty etc.  
    
    Parameters
    ------------
    init_game_for_round, CribbageGame 
        CribbageGame  object
    """
    game=init_game_for_round

        
    for i in range(3):
        
        assert game.dealer_go == False
        assert game.pone_go == False
        assert game.go_added == False
        assert game.play_end == False
        
        assert game.table_sum == 0
        assert game.active_player_str =='pone'
        assert len(game.on_table.cards)==0
        
        assert len(game.crib.cards)==0
        assert len(game.cut_card.cards)==0

        game.play_round(i)
        
        #pone always gets at least one point
        if i==0:
            assert game.pone.score >0

def test_cribbage_game_deal_hands(init_game_for_round):    
    """behaviour : cribbage game should be able to deal two hands to the two players
    Given : a game object 
    when : at the start of a round 
    then : deal 6 cards to each player and choose 1 cut card 
    
    Parameters: 
    -----------
    init_game_for_round CribbageGame Object    
    """
    game = init_game_for_round
    game.deal_hands()

    assert len(game.pone.hand.cards)==6 
    assert len(game.dealer.hand.cards)==6 
    assert len(game.cut_card.cards)==1 

def test_cribbage_game_deal_hands_from_set(init_game_for_round):    
    """behaviour : cribbage game should be able to deal two hands to the two players from a set game
    Given : a game object and set game dict 
    when : at the start of a round 
    then : deal 6 cards to each player and choose 1 cut card 
    
    Parameters: 
    -----------
    init_game_for_round CribbageGame Object    
    """
    game = init_game_for_round
    set_game = cribbage_tools.create_set_game(20)
    game.set_game=set_game

    for i in range(20):
        game.deal_hands()

        assert len(game.pone.hand.cards)==6 
        assert len(game.dealer.hand.cards)==6 
        assert len(game.cut_card.cards)==1 



def test_cribbage_game_create_set_game(init_game_for_round):
    """behaviour : each set of cards should be stored in a dict, and it should be possible to 
                   replay a set of cards for a round 
    Given : a round object and a set of pre determined hands 
    when : at the start of the round 
    then : deal the specified cards to each player
    
    Parameters: 
    -----------
    init_game_for_round CribbageGame Object    
    """
    game = init_game_for_round
    
    pone_hand,dealer_hand,cut_card,deck=cribbage_tools.deal()
    set_game = {'pone_hand':pone_hand,
                'dealer_hand' : dealer_hand,
                'cut_card' : cut_card,
                'deck' : deck}
    #first check that the right cards were dealt, 
    #i.e. for_set_game is the same as set_game 
    for_set_game = game.deal_hands(set_game)
    for key in for_set_game.keys():
        for card1,card2 in zip(for_set_game[key].cards,set_game[key].cards):
            assert card1.__str__() == card2.__str__() 
    
    #then check that the set_game hands end up in the player's hands 
    for hand in ['pone','dealer','cut_card']:
        obj  = getattr(game,hand)
        if 'card' in hand:
            extra=''
            obj2=obj
        else:
            extra='_hand'
            obj2 = getattr(obj,'hand')
        for card1,card2 in zip(set_game[hand+extra].cards,obj2.cards):
            assert card1.__str__() == card2.__str__() 
 

def test_cribbage_game_discard(init_game_for_round):    
    """#behaviour : round should be able to discard to the crib
    Given : a round object
    when : after the deal 
    then : each player moves 2 cards to the crib   
    
    Parameters: 
    -----------
    init_game_for_round CribbageGame Object    
    """
    game= init_game_for_round

    game.deal_hands()
    game.discard()
    
    assert len(game.crib.cards)==4 
    assert len(game.pone.hand.cards)==4 
    assert len(game.dealer.hand.cards)==4 

"""
def test_round_the_play(init_round):
    #behaviour :round should be able to execute the play
    #Given : a round object
    #when : after the discard 
    #then : 'the play' phase should happen. The dealer always gets at least one point
    
    #Parameters: 
    #-----------
    #init_round initialised CribbageRound Object
    
    round_1=init_round


    round_1.deal()
    round_1.discard()
    
    round_1.the_play()

    assert round_1.dealer.score >0
"""    
"""
def test_round_the_show(init_game_for_round):
    
    #behaviour :round should be able to execute the show
    #Given : a round object
    #when : after the play 
    #then : 'the show' phase should happen.The players scores should be incremented 
    #based on how many points they get in the show
    
    #Parameters: 
    #-----------
    #init_game_for_round CribbageGame Object    
    
    game=init_game_for_round


    game.deal()
    game.discard()
    
    pone_score,dealer_hand_score,crib_score,dealer_score,_ =   game.the_show()

    assert show.pone_score == game.pone.score 
    assert show.dealer_score == game.dealer.score 
"""

def test_cribbage_game_save_state(init_game_for_round):
    #behaviour to test : save the current state of the game 
    #given : a cribbage game object
    #when : after each player has taken their turn 
    #then : save the state as a json

    
    game=init_game_for_round
    game.deal_hands()

    game.save_state('test.json')

    assert os.path.isfile('test.json')

    with open('test.json') as json_file:
        data = json.load(json_file)
    keys =['p1_score']
    for key in keys:
        assert key in data.keys()     
