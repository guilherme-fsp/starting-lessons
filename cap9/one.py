fhand = open('words.txt')

dict_word = {}

for texto in fhand:
    palavras = texto.split() #.strip() faz o strip da palavra por linha rs
    for escrita in palavras:
        dict_word[escrita] = True
        print(escrita)

