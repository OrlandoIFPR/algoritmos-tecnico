notas = int(input())

n_100 = notas//100
resto = notas%100

n_50 = resto//50
resto = resto%50

n_20 = resto//20
resto = resto%20

n_10 = resto//10
resto = resto%10

n_5 = resto//5
resto = resto%5

n_2 = resto//2
resto = resto%2

print(notas)

print(f"{n_100} nota(s) de R$ 100,00")
print(f"{n_50} nota(s) de R$ 50,00")
print(f"{n_20} nota(s) de R$ 20,00")
print(f"{n_10} nota(s) de R$ 10,00")
print(f"{n_5} nota(s) de R$ 5,00")
print(f"{n_2} nota(s) de R$ 2,00")
print(f"{resto} nota(s) de R$ 1,00")