#Python archives 
from os import system

#Local archives 
from folder.rorganice import read_level as rd 
from folder.rorganice import count_level as lv
from folder.game import input_user as inp
from folder.game import play_game as gm
from folder.rorganice import desicion as ds
from folder.rorganice import one_time as one
from folder.screen import images as img

def run():
    #system('clear')
    position,lives,levelflag,wordplayed = 0,5,0,'s'
    listgame, listgameaux, deslista = [],[],[]
    wordlist = rd()
    print(img(5, wordplayed))
    while lives > 0:
        position = 13
        wordplayed, position, lives = lv(levelflag,wordlist,position,lives)
<<<<<<< HEAD
=======
        position = 13
>>>>>>> origin/master
        one(wordplayed, listgame, deslista)
        user = inp(wordplayed)
        system('clear')
        listgame,listgameaux,lives = gm(levelflag,wordplayed,user,listgame,listgameaux,lives)
        levelflag, listgameaux, lives, deslista, rescue = ds(levelflag, listgameaux, lives, position)   
    if lives == 0 and levelflag == 1 and rescue == 0:
        system('clear')
        print(img(0, wordplayed))
     
if __name__ == '__main__':
    run()