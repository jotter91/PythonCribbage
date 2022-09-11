from pycribbage import cribbage_game
from pycribbage import cribbage_tools
import os

def test_cribbage_game_init(init_game):
    """behaviour to test : cribbage game should store players, winner and the cards to be played
    given : -
    when : a game is to be initialised
    then : create object with attributes for each player, the cards to player, and the winner 
    
    Parameters
    ------------
    init_game, CribbageGame 
        CribbageGame  object
    """
    game = init_game
    
    assert hasattr(game,'player_1') ==True
    assert hasattr(game,'player_2') ==True
    assert hasattr(game,'set_game') ==True
    assert hasattr(game,'winner') ==True
    assert hasattr(game,'batch_mode') ==True

def test_cribbage_game_call_round(init_game):
    """behaviour to test : a game of cribbage should increment players scores
    given : an initialised game
    when : after the game 
    then : each player's score should be greater than 0 
    
    Parameters
    ------------
    init_game, CribbageGame 
        CribbageGame  object
    """
    game=init_game

    game.play_game()

    assert game.player_1.score >0
    assert game.player_2.score >0

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


def test_cribbage_game_set_game(tmp_path):
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
                print(game.winner)
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
    