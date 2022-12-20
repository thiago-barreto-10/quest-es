
nota1 = int (input('digite a nota da primeira unidade: '))
nota2 = int (input('digite a nota da segunda unidade: '))
nota3 = int (input('digite a nota da terceira unidade: '))
print('o semestre teve 60 aulas')
p= int (input('quantas aulas vc participou? '))
media= (nota1 + nota2 + nota3) / 3
if media >= 6 and p >=40:
    print(f'sua média {media} e sua preseça foi de {p}. APROVADO!')
elif media>= 6 and p <40:
    print(f'sua média {media} e sua preseça foi de {p}. REPROVADO!')
elif media < 6 and p<40:
    print(F'sua média {media} e sua preseça foi de {p}. REPROVADO!')
elif media < 6 and p>=40:
    print(F'sua média {media} e sua preseça foi de {p}. REPROVADO!')