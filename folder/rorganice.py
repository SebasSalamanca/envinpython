
def read_level():
    wordlist = []
    with open('./folder/data.txt', 'r', encoding='utf-8') as data:
        for line in data:
            wordlist.append(line)
    wordlist = sorted(wordlist, key=lambda x: len(x))  ##(1) Lista a ordenar (2) modo de ordenamiento, funciona con key
    return wordlist

def count_level(position,wordlist):
    wordplayed = wordlist[position]
    return wordplayed


