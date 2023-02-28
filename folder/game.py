
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

def play_game(wordplayed,user,listgame):
    #wordgame = [user for character in wordplayed if user == character]
    truevector = [True for character in wordplayed]
    wordgame = list(map(lambda y: user == y, list(wordplayed)))
    print(wordgame)
    flagameuno = list(map(lambda x,y: x*y, truevector, wordgame)) #wordgame
    flagame = set(flagameuno)
    listgameuno = listgame
    listgame = [(user) if character == True else('_')for character in wordgame]
    definitivo = listgameuno+listgame 
    print(listgame)
    
    return flagame,listgame,listgameuno
