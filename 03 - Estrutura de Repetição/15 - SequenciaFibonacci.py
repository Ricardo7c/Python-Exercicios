# Faça um programa capaz de gerar a série até o n−ésimo termo da sequencia de Fibonacci.
# Exemplo: 1,1,2,3,5,8,13,21,34,55,... 

num = int(input('Digite o final da sequencia: '))
a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
for cada in range(0, num):
    a, b = b, a+b
    print(b, end=' ')