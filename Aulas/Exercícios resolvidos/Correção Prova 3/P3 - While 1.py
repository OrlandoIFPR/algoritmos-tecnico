
saque = int(input())

while saque%10 != 0:
    
    print('Valor invalido')
    
    saque = int(input())

notas_50 = saque//50
notas_10 = saque%50//10

print(f"{notas_50} notas de R$ 50.00")
print(f"{notas_10} notas de R$ 10.00")