#Python archives 
from os import system

#Local archives 
from folder.rorganice import read_level as rd 
from folder.rorganice import count_level as lv
from folder.game import input_user as inp
from folder.game import play_game as gm


def run():
    #system('clear')
    position = 0
    flagame = False
    listgame = []
    listgameaux = []
    wordlist = rd()
    while True:
        wordplayed, position = lv(wordlist,position,flagame)
        user = inp(wordplayed)
        flagame,listgame,listgameaux = gm(wordplayed,user,listgame,listgameaux)    
        if position == 14:
            print('You have rescued the game')
            break

        
     

if __name__ == '__main__':
    run()