floc = input("Insira o nome do arquivo desejado: ")

try:
    fhand = open(floc+'.txt')
except FileNotFoundError:
    exit()

bib = dict()

for lines in fhand:
    words = lines.split()
    if len(words) == 0 or words[0] != "From":
        continue
    email = words[1]
    dominio = email.split('@')[1]
    if dominio not in bib:
        bib[dominio] = 1
    else:
        bib[dominio] += 1

ordenados = sorted(bib.items(), key=lambda item:item[1], reverse=True)
for dominio, contagem in ordenados:
    print(f"{dominio} : {contagem}")


#self made ^^ amo kaloline
