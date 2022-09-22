# conftest.py
from pycribbage import player,discard_methods,the_play_methods,the_play,cribbage_game
import pytest
import os 
from _pytest.assertion import truncate
truncate.DEFAULT_MAX_LINES = 9999
truncate.DEFAULT_MAX_CHARS = 9999  

@pytest.fixture()
def init_players():
    """initialise two players with player 1 as dealer
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

    player_1.set_dealer(True)
    return player_1,player_2


@pytest.fixture()
def init_game(tmp_path):
    """initialise a game of cribbage with two players using the default 
    Discard and ThePlay methods
    
    
    Parameters
    ------------
    tmp_path, str 
        location of temporary path 
    
    Returns
    ----------
    game, CribbageGame
        CribbageGame object 
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

