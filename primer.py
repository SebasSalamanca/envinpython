from folder.rorganice import read_level as rd 
from folder.rorganice import count_level as lv

position = 0
def run():
    wordlist = rd()
    wordplayed = lv(position,wordlist)
    print(wordplayed)
    

if __name__ == '__main__':
    run()