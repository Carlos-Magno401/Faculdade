print('Sequeência de Fibonacci')
numero = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2= 1
print(f'{t1} -> {t2}', end='')
count = 3
while count <= numero:
    t3= t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    count += 1
print('Fim')