#recebe o valor de cada lado do trinagulo
lado_um= float(input('Coloque o valor de um lado: '))
lado_dois = float(input('Coloque o valor de outro lado: '))
lado_tres = float(input('Coloque o valor de outro lado: '))

#verifica se é um trinangulo e qual tipo de triangulo é
if lado_um < lado_dois + lado_tres and lado_dois < lado_um + lado_tres and lado_tres < lado_um +lado_dois:
    print('Pode ser um triangulo')
    if lado_um == lado_dois and lado_dois == lado_tres:
        print(f'É um trinangulo Equilátero')
    elif lado_um == lado_dois or lado_dois == lado_tres or lado_tres == lado_um:
        print(f'É um triangulho Isósceles')
    elif lado_um != lado_dois and lado_dois != lado_tres and lado_tres != lado_um:
        print(f'É um trinagulo Escaleno')
else:
    print('Não pode ser um trinangulo')