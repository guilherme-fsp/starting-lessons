fname = input("Insira o nome do arquivo: ")
try:
    fhand = open(fname + ".txt")
except:
    print("File cannot be opened:", fname)

for linha in fhand:
    palavra = linha.split()
    if len(palavra) == 0 or palavra[0] != 'From':
        continue
    print(palavra[2], palavra[4])


