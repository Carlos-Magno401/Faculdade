import math
valor=float(input('Valor do cateto oposto: '))
valor2=float(input('Valor do cateto adjacente'))
valor_total=math.hypot(valor, valor2)
#valor_total= (valor**2 + valor2**2) ** (1/2)
print(f'A hipotenusa vai medir {valor_total:.2f}')