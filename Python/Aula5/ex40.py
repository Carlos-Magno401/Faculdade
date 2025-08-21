#recebe a primeira nota
nota_um = float(input("Digite a primeira nota: "))
#recebe a segunda nota
nota_dois = float(input("Digite a segunda nota: "))
#faz a media da nota
nota_final = (nota_um + nota_dois)/2

print(f'Tirando {nota_um} e {nota_dois}, a média do aluno é {nota_final}')

if nota_final >= 7:
    print(f"Media {nota_final}. Aprovado")
elif nota_final < 5:
    print(f"Media {nota_final}. Reprovado")
elif nota_final >=5 and nota_final <7:
    print(f"Media {nota_final}. Recuperação")