def get_numbers():
    numbers = []
    while True:
        try:
            l_num = input("Insira um número: ")
            if l_num == 'done':
                break
            l_num = int(l_num)
            numbers.append(l_num)
        except ValueError:
            print('Bad data')
    #print('Números escolhidos: ', numbers)
    return numbers

numeros = get_numbers()
#print('Lista de numeros retornada: ', numeros)

def calc(numeros):
    total = 0
    cont = 0
    for l_num in numeros:
        total += l_num
        cont += 1
        media = total / cont
    print(total, cont, media)
    #print("Contagem dos números: ", cont)
    #print("Média: ", media)
    return total, cont, media

calculo = calc(numeros)

    

