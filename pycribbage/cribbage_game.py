from pycribbage import player,discard_methods,the_play_methods,cribbage_round
from pycribbage.cribbage_tools import GameOver,cut_for_crib,switch_dealer
import os 

class CribbageGame():
    """
    A class used to represent a game of Cribbage

    ...

    Attributes
    ----------
    set_game : dict
        a dictionary which contains the cards to played in each hand
    rounds : dict
        a dictionary which contains each CribbageRound object
    winner : str
        a string which represents the winner of the game 
    for_set_game : dict
        a dictionary which contains the cards which were dealt in each round
    player_1 : Player 
        a Player object to represent the first player
    player_2 : Player 
        a Player object to represent the second player
    cut_player :str
        string to denote the cut player 
    batch_mode : bool 
        batch_mode = True will write the output to a log file 
    log_fd : _io.TextIOWrapper
        file object to be logged to 
        
    Methods
    -------
    play_game()
        Plays out the cribbage game
    set_pone_dealer()
        allocate players as pone and dealer
    create_log_file()
        create a log file to write game details to
    logger()
        log to console (if not batch) and file
    close_log_file()
        close the log file
    """
    def __init__(self,players,set_game={},cut_player=None,batch_mode=False):
        """
        Parameters
        ----------
        players : list
            A list (two entries) which contains the two Player objects for the game
        set_game : dict , optional
            a dictionary which contains the cards to played in each hand.
            if not set then the cards to be dealt will be randomly generated
        set_game : dict , optional
            a dictionary which contains the cards to played in each hand.
            if not set then the cards to be dealt will be randomly generated
        cut_player :str,optional
            if a given player is to be the dealer then set this as 'player_1' or 'player_2'
        batch_mode : bool, optional 
            batch_mode = True will write the output to a log file     
        """
        
        self.set_game=set_game
        self.rounds ={}
        self.winner=''
        self.for_set_game={}
        self.player_1=None
        self.player_2=None
        self.cut_player=cut_player
        self.batch_mode = batch_mode
        
        
        self.create_log_file()
        
        for i in [0,1]:
            
            #load in discard method
            if players[i]['TS_method'] =='0':
                ts_method =  discard_methods.Discard()
            elif players[i]['TS_method']=='1':
                ts_method = discard_methods.RandomDiscard()
            elif players[i]['TS_method']=='2':
                ts_method = discard_methods.HumanDiscard()
            
            
            #load in the play method
            if players[i]['TP_method'] =='0':
                tp_method =  the_play_methods.ThePlayMethod() 
            elif players[i]['TP_method']=='1':
                tp_method = the_play_methods.RandomThePlay()
            elif players[i]['TP_method']=='2':
                tp_method = the_play_methods.HumanThePlay()
            
            
            player_obj = player.Player(players[i]['name'],
                                     ts_method,
                                     tp_method)
                                     
            setattr(self,'player_%i'%(i+1),player_obj)
            
    def set_pone_dealer(self):
        """allocate players as pone and dealer

        Returns
        --------
        pone, Player
            player obj for non-dealer
        dealer, Player
            player obj for dealer
        """
        
        if self.player_1.is_dealer ==True:
            pone=self.player_2
            dealer=self.player_1
        else:
            dealer=self.player_2
            pone=self.player_1
        
        return pone,dealer
        
    def create_log_file(self,path=None):
        """create a log file to write game details to
        
        Parameters
        ----------
        path : str, optional 
            path where file is to be written
        """
        if path ==None:
            path=os.getcwd()
        
        i_log = 0
        while os.path.exists(os.path.join(path,"game%03d.log" % i_log)):
           i_log += 1
           
        fname_log = "game%03d.log" % i_log    
        
        fname = os.path.join(path,fname_log)
        f = open(fname,'w+')
 
        self.log_fd = f
        
    def logger(self,to_log):
        """ log to console (if not batch) and file"""
        
        if to_log.endswith('\n'):
            pass
        else:
            to_log = to_log +'\n'
        self.log_fd.write(to_log)
        
        if self.batch_mode == False:
            print(to_log)
            
    def close_log_file(self):
        """close the log file"""
        self.log_fd.close()
        
    def play_game(self):
        """Plays out the cribbage game"""

        self.logger('Game about to begin !')
        self.logger('Cut card to choose who is first dealer')
        
        #First choose which player should be the first dealer
        if self.cut_player ==None:
            cut_player,cut_string_ = cut_for_crib()
            cut_string = cut_string_.replace('P1',self.player_1.name).replace('P2',self.player_2.name)
        else:
            cut_player = self.cut_player
            cut_string ='%s will be dealer'%self.cut_player
        self.logger(cut_string)    
        if cut_player =='player_1':
            self.player_1.set_dealer(True)
            self.player_2.set_dealer(False)
            self.logger('%s is dealer'%self.player_1.name)

        elif cut_player =='player_2':
            self.player_1.set_dealer(False)
            self.player_2.set_dealer(True)
            self.logger('%s is dealer'%self.player_2.name)

        pone,dealer = self.set_pone_dealer()
        for_set_game ={}
        i_round= 0
        
        #keep playing rounds until someone wins
        while True:
        
            try:
                self.logger('start of round %i'%i_round)
                round_i = cribbage_round.CribbageRound(pone,dealer)
                
                if len(self.set_game.keys()) ==0:
                    for_set_game[i_round] = round_i.deal()
                else:
                    for_set_game[i_round] = round_i.deal(self.set_game[i_round])
                    
                round_i.discard()
                play = round_i.the_play()
                self.logger(play.__str__())
                show = round_i.the_show()
                self.logger(show.__str__().replace('Pone',pone.name).replace('Dealer',dealer.name).replace('Crib',"%s's Crib"%dealer.name))
                self.rounds[i_round] = round_i
                self.logger('='*30)
                self.logger('End of round %i'%i_round)
                self.logger('%s score : %i , %s score :%i\n'%(self.player_1.name,
                                                        self.player_1.score,
                                                        self.player_2.name,
                                                        self.player_2.score))
                self.logger('='*30)
                i_round +=1
                switch_dealer(self.player_1,self.player_2)
                pone,dealer = self.set_pone_dealer()
                
            except GameOver:
                
                self.logger(play.__str__())
                self.logger(show.__str__().replace('Pone',pone.name).replace('Dealer',dealer.name).replace('Crib',"%s's Crib"%dealer.name))
                self.logger('end of game scores')
                self.logger('%s %i %s %i'%(self.player_1.name,
                                     self.player_1.score,
                                     self.player_2.name,
                                     self.player_2.score))
                if self.player_1.score >=121:
                    self.winner = self.player_1.name
                else:
                    self.winner = self.player_2.name
                    
                self.for_set_game = for_set_game
                
                self.rounds[i_round] = round_i
                
                self.close_log_file()
                break 

