maior = 0 #largest = None (original)
x = 10 #nao tem no codigo original
y = 20 #nao tem no codigo original
z = 50 #nao tem no codigo original
k = 100 #nao tem no codigo original
t = 200 #nao tem no codigo original
l = 500 #nao tem no codigo original
m = 1000 #nao tem no codigo original
last = m #nao tem no codigo original
print("Antes é: ", maior) #print('Before: ', largest)
for maior in [x, y, z, k, t, l, m]: # for itervar in [3, 41, 12, 9, 74, 15]:
    if maior != last: #if largest is None or itervar > largest: ------ para o minimo-> if smallest is None or itervar < smallest:
        #largest = itervar
        print("Não é esse:  ", maior) #print('Loop: ', itervar, largest)
        #print('Largest: ', largest)
    else: #nao tem no codigo original
        print("Maior é: ", maior) #nao tem no codigo original
        #variable largest is best thought of as the "largest value we have seen so far."