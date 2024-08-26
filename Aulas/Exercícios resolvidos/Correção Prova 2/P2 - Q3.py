n = int(input())

nota_validas = 0

for i in range(n):
    nota = float(input())
    if nota >= 0 and nota <= 10:
        nota_validas = nota_validas + 1
print(f"Foram encontradas {nota_validas} validas!")