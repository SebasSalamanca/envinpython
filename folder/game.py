
def input_user(wordplayed):
    flag = True
    while flag == True:
        user = input('PLease enter a letter: ').lower()
        flag = False
        if not user.isalpha(): #Si la letra no corresponde al abecedario
            flag = True
            print('Please enter a letter, not other characters')
        elif len(user) > 1:
            flag = True
            print('Please enter a letter, not more than one letter')
    return user

def play_game(levelflag,wordplayed,user,listgame,listgameaux,lives):
    flag = 0 
    wordgame = list(map(lambda y: user == y, list(wordplayed)))
    listgame = [(user) if character == True else('_')for character in wordgame]
    if len(listgameaux) == 0 or levelflag == 1:
        listgameaux = ['_' for elementos in listgame]
    for position in range(0,len(listgame)):
        if listgame[position] != '_':
            flag = 1
            listgameaux[position] = listgame[position]
    if flag == 0:
        lives -= 1
    return listgame,listgameaux,lives








    

    

    

