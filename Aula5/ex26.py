frase=str(input('Digite uma frase: ')).lower().strip()
print(f'A letra A aparece {frase.count('a')} vezes')
print(f'A letra A aparece na {frase.find('a')+1} posição')
print(f'E aparece {frase.rfind('a')+1} como ultima posição')