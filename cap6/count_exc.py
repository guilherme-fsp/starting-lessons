def get_count():
    get_word = input("Insira a palavra ou frase: ")
    get_letter = input("Insira uma letra ou frase: ")
    count = 0
    for count_letter in get_word:
        if count_letter == get_letter:
            count = count + 1
    if count > 0:
            print(f"A letra '{get_letter}' aparece '{count}' vezes dentro da palavra/frase '{get_word}'")
            #print(count)
    else:
            print(f"Não existe a letra '{get_letter}' dentro da palavra/frase '{get_word}'")

contagem = get_count()