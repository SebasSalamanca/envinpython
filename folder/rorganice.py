
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


def desicion(levelflag, listgameaux): 
    levelflag = 0 
    deslista = list(filter(lambda x: x == '_', listgameaux))
    if not deslista:
        flag = True
        while flag == True:
            userlevel = input('You Won!, Do you want to continue with next level? y/n: ').lower()
            flag = False
            if not userlevel.isalpha():
                flag = True
                print('Please enter a letter y/n, not other characters')
            if len(userlevel) > 1:
                flag = True
                print('Please enter a letter y/n, not more than one letter')

        if userlevel == 'y':
            levelflag = 1
        else:
            levelflag = 0
            print('Thank you for playing Hangman game')
    return levelflag, listgameaux





