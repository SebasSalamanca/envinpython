#Python archives 
from os import system

#Local archives 
from folder.rorganice import read_level as rd 
from folder.rorganice import count_level as lv
from folder.game import input_user as inp
from folder.game import play_game as gm
from folder.rorganice import desicion as ds

from folder.screen import images as img

def run():
    #system('clear')
    position,lives,levelflag = 0,5,0
    listgame, listgameaux = [],[]
    wordlist = rd()
    while lives > 0:
        wordplayed, position, lives = lv(levelflag,wordlist,position,lives)
        user = inp(wordplayed)
        system('clear')
        listgame,listgameaux,lives = gm(levelflag,wordplayed,user,listgame,listgameaux,lives)
        levelflag, listgameaux, lives = ds(levelflag, listgameaux, lives)           
    if lives == 0:
        system('clear')
        print(img(0))
     
if __name__ == '__main__':
    run()