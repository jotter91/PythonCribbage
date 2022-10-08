from flask import Flask, render_template, request, current_app,jsonify,redirect,url_for
from pycribbage.main import read_players
from pycribbage.cribbage_game import CribbageGame
import multiprocessing 
import time
app = Flask(__name__)

state={'p1_score':1}
state={"active_player_str": "pone",
  "crib": "Jack of Hearts\nKing of Diamonds",
  "cut_card": "4 of Diamonds",
  "on_table": "",
  "p1_dealer": True,
  "p1_hand": "2 of Diamonds\n4 of Hearts\n7 of Diamonds\n9 of Clubs\nQueen of Hearts\n9 of Spades",
  "p1_score": 0,
  "p2_dealer": False,
  "p2_hand": "Ace of Spades\n8 of Spades\n5 of Clubs\n5 of Diamonds",
  "p2_score": 0,
  "table_sum": 0}
p1_index=[]
info='some info'

#@app.route('/' )
#def home():
#    return render_template('game.html', )
    
@app.route('/game' )
def game():
    #if state==None:
        jsonify(state)
        return render_template('game.html',**state ,info=info)
    #else:
    #    return render_template('game.html',p1_score=1 )
    
@app.route('/send', methods=['POST'])

def send():
    global p1_index 
    if request.method == 'POST':

        index_1  = int(request.form['index_1'])
        index_2  = int(request.form['index_2'])
        p1_index=[index_1,index_2]
        
        #game()
    return redirect(url_for('game'))
    
@app.route('/launch' )
def launch():
    
    players=[]
    
    player={    'name': 'Player 1',
                'TS_method':'2', 
                'TP_method':'0',}
    players.append(player)
    
    player={    'name': 'Player 2',
                'TS_method':'0', 
                'TP_method':'0',}
    players.append(player)
    
    
    process = multiprocessing.Process(
            target = start_game,
            args = (players,))
    process.start()
    
    time.sleep(1)
    
    return redirect(url_for('game'))

def start_game(players):
    game = CribbageGame(players)
    
    game.play_game()

@app.post('/p1_choice' )
def p1_choice():
    global p1_index 
    
    if request.is_json:
        _ = request.get_json()
        p1_index = _
        return _, 201
    return {"error": "Request must be JSON"}, 415
    
@app.get("/p1_choice")
def get_p1_choice():
    return jsonify(p1_index)    
    
@app.post('/state' )
def add_state():
    #state=[]
    global state 
    
    if request.is_json:
        state_ = request.get_json()
        state = state_
        return state_, 201
    return {"error": "Request must be JSON"}, 415
    
@app.get("/state")
def get_state():
    return jsonify(state)  

@app.post('/info' )
def add_info():
    #state=[]
    global info 
    
    if request.is_json:
        info_ = request.get_json()
        info = info_
        return info_, 201
    return {"error": "Request must be JSON"}, 415
    
@app.get("/info")
def get_info():
    return jsonify(info)  
    
if __name__ == ' __main__':
    app.run(debug=True)
