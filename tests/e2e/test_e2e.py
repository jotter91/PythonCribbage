from pycribbage import cribbage_game
import os

def test_cribbage_game_e2e(tmp_path,init_players,set_game_1):
    """behaviour to test : From a pre-determined set of cards, the same game result should be obtained
                            with the same deterministic bots
    
    given : a set game
    when : after the game 
    then : the player's scores should match that of the previous outcome 
    

    """
    player_1,player_2 = init_players
    players=[player_1,player_2]

    cwd = os.getcwd()
    os.chdir(tmp_path)
    
    game = cribbage_game.CribbageGame(players,set_game =set_game_1,cut_player='player_1')
    game.play_game() 
    
    os.chdir(cwd)
    assert game.player_1.score ==101
    assert game.player_2.score ==121
