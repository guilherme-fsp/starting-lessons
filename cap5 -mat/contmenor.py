menor = None
print('Valor menor: ', menor)
for cont in [3, 4, 5, 6, 7, 8, 10, 16, 30]:
    if menor is None or cont < menor:
        print('Loop: ', cont, menor)
print('menor: ', menor)