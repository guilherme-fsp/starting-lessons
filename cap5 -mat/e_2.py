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
    return numbers
    
numeros = get_numbers()

def calc_num(numeros):
    total = 0
    cont = 0
    maior = None
    menor = None
    for num in numeros:
        total += num
        cont += 1
        if maior is None or num > maior:
            maior = num
        if menor is None or num < menor:
            menor = num    

    print(total, cont, maior, menor)
    return total, cont, maior, menor
    
calculo = calc_num(numeros)    


