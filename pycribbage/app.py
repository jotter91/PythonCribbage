from flask import Flask, render_template, request, current_app
from pycribbage.main import read_players
from pycribbage.cribbage_game import CribbageGame
app = Flask(__name__)


@app.route('/' )
def home():
    return render_template('game.html', )
@app.route('/send', methods=['POST'])
#TODO: replace sum 
def send(sum=sum):
    if request.method == 'POST':
        #TODO :check type for inputs
        pass
    return render_template('game.html', )
@app.route('/launch' )
def launch():
    
    players = read_players()
    
    game = CribbageGame(players)
    
    game.play_game()
    
    return render_template('game.html', )
if __name__ == ' __main__':
    app.run(debug=True)
