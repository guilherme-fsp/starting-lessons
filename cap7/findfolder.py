fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
    print(line.strip())
    print('Line Count:', count)
fhand.close()
# codigo contagem + imprimir mensagem