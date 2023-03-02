#Python archives 
from os import system

#Local archives 
from folder.rorganice import read_level as rd 
from folder.rorganice import count_level as lv
from folder.game import input_user as inp
from folder.game import play_game as gm
from folder.rorganice import desicion as ds


def run():
    #system('clear')
    position,lives,ledsffleg = 0,5,0
    listgame, listgameaux = [],[]
    wordlist = rd()
    while lives > 0:
        wordplayed, position, lives = lv(levelflag,wordlist,position,lives)
        user = inp(wordplayed)
        listgame,listgameaux,lives = gm(levelflag,wordplayed,user,listgame,listgameaux,lives)
        levelflag, listgameaux = ds(levelflag, listgameaux)            
     
if __name__ == '__main__':
    run()