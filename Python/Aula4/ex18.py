import math
valor=float(input('Digite o angulo que voce deseja '))
seno= math.sin(math.radians(valor))
cosseno=math.cos(math.radians(valor))
tangente=math.tan(math.radians(valor))
print(f'O seno, cosseno e tangente é {seno:.2f}, {cosseno:.2f} e {tangente:.2f}')