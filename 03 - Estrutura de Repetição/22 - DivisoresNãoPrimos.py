# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
# por quais número ele é divisível.

num = int(input('Digite um numero: '))
primo = True

cont = 0
for cada in range(1, num+1):
    if num % cada == 0:
        cont += 1
        
if cont > 2 or num < 2:
    primo = False


if primo == True:
    print('é primo')
else:
    print(f'O numero {num} não é primo, ele é divisivel por: ', end='')
    for cada in range(1, num+1):
        if num % cada == 0:
            if cada == num:
                print(cada, end='')
            else:
                print(cada, end=',')