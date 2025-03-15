import re

f_inp = input('Insira o nome do arquivo: ')
f_open = open(f_inp+'.txt')
listagem = list()

for line in f_open:
    line = line.rstrip()
    matching = re.findall('@([^ ]*)', line)
    if len(matching) !=1:
        continue
    else:
        all_from = (matching)
        listagem.append(all_from)


print(listagem)