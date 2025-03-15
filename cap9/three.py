flocate = input('Escreva o nome do arquivo: ')
fhand = open(flocate + ".txt")
count = dict()

for line in fhand:
    words = line.split() 
    if len(words) == 0 or words [0] != 'From':
         continue
    email = words [1]
    if email not in count:
          count[email] = 1
    else:
         count[email] += 1
#for email, contagem in count.items(): #.items() transforma o dicionário em pares (chave, valor). + (2)
     #print(f"{email}: {contagem}") #faz com que a contagem com emails saia linha a linha (2)
print(count)

