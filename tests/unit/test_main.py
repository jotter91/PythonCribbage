""" global behaviour of __main__ to test: read and check inputs required to start a game """
from pycribbage import __main__
import pycribbage.the_play_methods as the_play_methods
import pycribbage.discard_methods as discard_methods

def test_main_the_show_method():
    """ behaviour to test : user can only input certain strings for discard method
    given : a user's input for method
    when : at the start of __main__
    then : return the method as-is if it is OK, else return -1

    """
    method = '1'
    assert __main__.check_the_show_method(method) == '1'
    method = '-1'
    assert __main__.check_the_show_method(method) == -1


def test_main_the_play_method():
    """ behaviour to test : user can only input certain strings for the play method
    given : a user's input for method
    when : at the start of __main__
    then : return the method as-is if it is OK, else return -1

    """
    method = '1'
    assert __main__.check_the_play_method(method) == '1'
    method = '-1'
    assert __main__.check_the_play_method(method) == -1


def test_main_player_reader():
    """ behaviour to test : user can only input  string for player name
    given : a user's name
    when : at the start of __main__
    then : return the name as-is if it is OK, else return -1

    """
    player_name = 'Player 1'

    assert __main__.check_player_name(player_name) == player_name

    assert __main__.check_player_name(1) == -1


def test_main_read_players(monkeypatch):
    """ behaviour to test : users input settings from stdin
    given : user's respones
    when : at the execution of __main__
    then : create players based on users inputs

    Parameters:
    -----------
    monkeypatch,
        monkeypatch object to handle stdin
    """
    responses = iter(['Player 1', '1', '1', 'Player 2', '1', '1'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    players = __main__.read_players()
    for i, player in zip([0, 1], ['Player 1', 'Player 2']):
        assert players[i].name == player
        assert issubclass(players[i].discard_method.__class__,discard_methods.Discard)
        assert issubclass(players[i].the_play_method.__class__,the_play_methods.ThePlayMethod)
