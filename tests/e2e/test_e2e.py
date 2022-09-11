from pycribbage import cribbage_game
from pycribbage import cribbage_tools
import os

def test_cribbage_game_e2e(tmp_path):
    """behaviour to test : From a pre-determined set of cards, the same game result should be obtained
                            with the same deterministic bots
    
    given : a set game
    when : after the game 
    then : the player's scores should match that of the previous outcome 
    

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

    set_game = cribbage_tools.load_set_game(os.path.join('tests','game_1.pickle'))
    
    cwd = os.getcwd()
    os.chdir(tmp_path)
    
    game = cribbage_game.CribbageGame(players,set_game =set_game,cut_player='player_1')
    game.play_game() 
    
    os.chdir(cwd)
    assert game.player_1.score ==101
    assert game.player_2.score ==121
