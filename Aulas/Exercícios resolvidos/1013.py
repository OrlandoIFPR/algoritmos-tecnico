valorA, valorB, valorC = input().split()
valorA = int(valorA)
valorB = int(valorB)
valorC = int(valorC)

#Podendo continuar o desenvolvimento de assim por diante.

maiorAB = (valorA + valorB + abs(valorA - valorB))/2

maiorABC = (maiorAB + valorC + abs(maiorAB - valorC))/2

print(f"{int(maiorABC)} eh o maior")
