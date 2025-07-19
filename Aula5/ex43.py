#verifica o peso e a altura da pessoa
peso = float(input("Qual é seu peso? (Kg)? "))
altura = float(input("Qual é sua altura(m)? "))
#calcula o imc da pessoa
imc = peso/(altura*altura)
#mostra na tela qual é o IMC da pessoa
print(f'O IMC dessa pessoa é de {imc:.1f}')
#verifica e mostra na tela se a pessoa está no seu imc ideial
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc <30:
    print('Sobrepeso')
elif imc >= 30 and imc <40:
    print('obesidade')
elif imc >= 40:
    print('Obesidade mórbida')