#recebe o valor da compra e a forma de pagamento
preco = int(input("Qual é o valor da sua compra? "))
forma_pagamento = int(input('''
Aperte [1] para à vista em dinheiro
Aperte [2] para à vista no cartão
Aperte [3] para 2x no cartão
Aperte [4] para 3x no cartão
Sua opção: '''))
#verifica qual foi a forma de pagamento e mostra na tela o valor com ou sem desconto
if forma_pagamento == 1:
    valor = preco-(preco*0.1)
    print(f'O valor com desconto de 10% ficou em R$:{valor:0.2f}')
elif forma_pagamento == 2:
    valor = preco-(preco*0.05)
    print(f'o valor com desconto de 5% ficou em R$:{valor:0.2f}')
elif forma_pagamento == 3:
    valor = preco
    print(f'O valor ficou em R$:{valor:0.2f}, ou R$:{valor/2:0.2f} em 2x')
elif forma_pagamento == 4:
    valor = preco+(preco*0.2)
    print(f'O valor ficou em R$:{valor:0.2f}, ou em R$:{valor/3:0.2f} em 3x')
else:
    print('forma de pagamento incorreta.')