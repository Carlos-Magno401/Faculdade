r1 = float(input('Coloque o valor de um lado: '))
r2 = float(input('Coloque o valor de outro lado: '))
r3 = float(input('Coloque o valor de outro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print(f'Os lados {r1}, {r2} e {r3} podem formar triângulo.')
else:
    print(f'Os lados {r1}, {r2} e {r3} não podem formar triângulo.')