fhand = open('mbox.txt')
count = 0
for line in fhand:
   words = line.split()
   if len(words) == 0 or words[0] != 'From':
     continue # Ignora linhas vazias
   count = count + 1
   print(words[1]) # Imprime o terceiro elemento (dia da semana)
print(count)