def get_values():
    valores = []
    while True:
        try:
            val = input("Insira os valores: ")
            if val == 'done':
                break
            val = int(val)
            valores.append(val)
        except ValueError:
            print("Inválido tente novamente")
    print("Os números escolhidos são: ", valores)
    return valores

numeros = get_values()

def calc_val(numeros):
    total = 0
    cont = 0
    mini = None
    maxi = None
    for num in numeros:
        total += num
        cont += 1
        media = total / cont
        if mini is None or num < mini:
            mini = num
        if maxi is None or num > maxi:
            maxi = num
    print(f"Total: {total}, Contagem: {cont}, Média: {media}, Mínimo: {mini}, Máximo: {maxi}")
    return total, cont, media, mini, maxi

calculo = calc_val(numeros)




