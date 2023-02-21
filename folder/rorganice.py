
def read_level():
    word_list = []
    with open('./folder/data.txt', 'r', encoding='utf-8') as data:
        for line in data:
            word_list.append(line)
    word_list = sorted(word_list, key=lambda x: len(x))  ##(1) Lista a ordenar (2) modo de ordenamiento, funciona con key
    return word_list

