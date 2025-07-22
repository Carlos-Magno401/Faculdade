frase = str(input("Digite um frase: ")).strip().upper()
pali = frase.split()
junto= ''.join(pali)
inverso = ''
for letra in range(len(junto) -1, -1, -1): 
    inverso= inverso + junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
print(junto, inverso)