fhand = open('romeo.txt')

counts = dict()

for texto in fhand:
    palavras = texto.split()
    for contagem in palavras:
        if contagem not in counts:
            counts[contagem] = 1
        else: 
            counts[contagem] +=1
print(counts)


