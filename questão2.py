idade = 0
s = 0
t1=0
t2=0
t3=0
t4=0
t5=0
for i in range(15):
    idade = int(input('digite sua idade: '))
    if idade <=15:
        idade = 1
        t1 = t1 + idade  
    elif idade>15 and idade<=30:
        idade = 1
        t2 = t2 + idade
    elif idade>30 and idade<=45:
        idade = 1
        t3 = t3 + idade
    elif idade>45 and idade<=60:
        idade = 1
        t4 = t4 + idade
    elif idade>60:
        idade = 1
        t5 = t5 + idade
t15 = 100*t1/15
t60 = 100 *t5/15
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(f'porcentagem de crianças menores de 15 anos: {t15}%')
print(f'porcentagem de pessoas com mais de 60 anos: {t60}%')