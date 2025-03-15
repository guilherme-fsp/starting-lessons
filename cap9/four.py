flocate = input("Insira o nome do arquivo: ")

count = 0
maior = None
menor = None
bib = dict()
total = 0

try:
    fhand = open(flocate + ".txt")
except FileNotFoundError:
    print("Não foi possível localizar", flocate)
    exit()

for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != "From":
        continue
    email = words[1]
    if email not in bib:
        bib[email] = 1
    else:
        bib[email] += 1
for email, contagem in bib.items():
    print(email, contagem)
print("\n")


maior = max(bib, key = bib.get)
menor = min(bib, key =bib.get)
menor_valor = min(bib.values())
menores = [email for email, contagem in bib.items() if contagem == menor_valor]
for email in menores:
    print(f"Quem menos recebeu emails foi {email} com {menor_valor}")
print(f"Quem mais recebeu emails foi: {maior} com {bib[maior]} mensagens")
print(f"Quem menos recebeu emails foi: {menor} com {bib[menor]} mensagens")
print("\n")



    


