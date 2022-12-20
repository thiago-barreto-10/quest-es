
ns= 0 
s=0
s1= 0
n = int (input('quantas pessoas moram na cidade? '))
print('digite o sexo de cada pessoa: 1 para homem e 2 para mulher: ') 
 
for i in range (n):
    ns =int (input('digite aqui: '))
    if ns == 1:
        s= s + ns
    elif ns == 2:
        ns=1
        s1 = s1 + ns
    else:
        print('algum dado foi escrito errado')
        break
print(f'mulheres: {s}')
print(f'homens: {s1}')    
