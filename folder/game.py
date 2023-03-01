
def input_user(wordplayed):
    flag = True
    while flag == True:
        user = input('PLease enter a letter: ').lower()
        flag = False
        if not user.isalpha():
            #Luego redireccionar
            flag = True
            print('Please enter a letter, not other characters')
        if len(user) > 1:
            flag = True
            print('Please enter a letter, not more than one letter')
    return user

def play_game(wordplayed,user,listgame,listgameaux):
    #wordgame = [user for character in wordplayed if user == character]
    print(len(listgameaux))
    truevector = [True for character in wordplayed]
    wordgame = list(map(lambda y: user == y, list(wordplayed)))
    print(wordgame)
    flagameuno = list(map(lambda x,y: x*y, truevector, wordgame)) #wordgame
    flagame = set(flagameuno)
    listgame = [(user) if character == True else('_')for character in wordgame]
    if len(listgameaux) == 0:
        listgameaux = ['_' for elementos in listgame]
    size = len(listgame)
    for position in range(0,size):
        if listgame[position] != '_':
            listgameaux[position] = listgame[position]
    print(listgame)

    return flagame,listgame,listgameaux
