flocate = input('Insira o nome do arquivo: ')

try:
    fhand = open(flocate + '.txt')
except FileNotFoundError:
    exit()

bib = dict()

for lines in fhand:
    words = lines.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    time = words [5]
    hour = time.split(':')[0]
    if hour not in bib:
        bib[hour] = 1
    else:
        bib[hour] += 1

ordenado = sorted(bib.items(), key=lambda item:item[1], reverse=True)
for hour, contagem in ordenado:
    print(f'Foram enviados {contagem} emails, as {hour} horas')
