


def read_level():
    wordlist = []
    with open('./folder/data.txt', 'r', encoding='utf-8') as data:
        for line in data:
            wordlist.append(line)
    wordlist = sorted(wordlist, key=lambda x: len(x))  ##(1) Lista a ordenar (2) modo de ordenamiento, funciona con key
    return wordlist

def count_level(levelflag,wordlist,position,lives):
    if levelflag == 1:
        lives = 5
        position += 1
    wordplayed = wordlist[position].rstrip()
    return wordplayed,position,lives 

def one_time(wordplayed, listgame, deslista):
    if len(listgame) == 0 or not deslista:
        auxword = ['_' for character in wordplayed]
        print(auxword)


def desicion(levelflag, listgameaux, lives, position): 
    levelflag, rescue = 0,0 
    deslista = list(filter(lambda x: x == '_', listgameaux))
    if not deslista: ##Acá solo entra si está vacía
        flag = True
        while flag == True:
            userlevel = input('You Won!, Do you want to continue with next level? y/n: ').lower()
            flag = False
            if not userlevel.isalpha():
                flag = True
                print('Please enter a letter y/n, not other characters')
            elif len(userlevel) > 1:
                flag = True
                print('Please enter a letter y/n, not more than one letter')
            elif userlevel == 'y':
                flag = False
            elif userlevel == 'n':
                flag = False
            else:
                flag = True
                print('Please enter a letter y/n, not other characters')

        if userlevel == 'y':
            levelflag = 1
            if position == 13: 
                print('You have rescued the GAME congratulations, you are the best!')
                lives = 0 
                rescue = 1 
        else:
            levelflag = 0
            lives = 0
            print('Thank you for playing Hangman game')
    return levelflag, listgameaux, lives, deslista, rescue





