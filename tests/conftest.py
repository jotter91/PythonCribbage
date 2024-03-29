# conftest.py
import sys
print(sys.path)
from pycribbage import player,discard_methods,the_play_methods,cribbage_game,cribbage_tools
import pytest
import pathlib
import os 
from _pytest.assertion import truncate
truncate.DEFAULT_MAX_LINES = 9999
truncate.DEFAULT_MAX_CHARS = 9999  

@pytest.fixture()
def init_players():
    """initialise two players with player 2 as dealer
        this uses the default Discard and ThePLay Methods
    Returns
    ----------
    player_1, Player
        Player obj for player 1
    player_2, Player
        Player obj for player 2    
    """
    player_1 = player.Player('Player 1',
                             discard_methods.Discard(),
                             the_play_methods.ThePlayMethod() )

    player_2 = player.Player('Player 2',
                             discard_methods.Discard(),
                             the_play_methods.ThePlayMethod() )

    #player_1.set_dealer(True)
    player_2.set_dealer(True)
    return player_1,player_2


@pytest.fixture()
def init_game(tmp_path,init_players):
    """initialise a game of cribbage with two players using the default 
    Discard and ThePlay methods
    
    
    Parameters
    ------------
    tmp_path, str 
        location of temporary path 
    init_players, tuple
        tuple of Player objs 
    Returns
    ----------
    game, CribbageGame
        CribbageGame object 
    """
    player_1,player_2 = init_players
    players=[player_1,player_2]
    os.chdir(tmp_path)
    game = cribbage_game.CribbageGame(players,batch_mode=True)
    return game
@pytest.fixture()
def init_game_for_round(init_game):
    """    
    Parameters
    ------------
    init_game, CribbageGame 
        CribbageGame  object
    
    Returns
    ------------
    game, CribbageGame 
        CribbageGame  object
    """
    game=init_game
    game.player_1.set_dealer(True)
    game.player_2.set_dealer(False)
    game.set_pone_dealer()

    return game

@pytest.fixture()
def set_game_1():
    return  cribbage_tools.load_set_game(os.path.join(pathlib.Path(__file__).parent.resolve(), 'game_1.pickle'))

