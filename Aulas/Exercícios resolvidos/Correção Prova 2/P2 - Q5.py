n = int(input())

tot_baralho = 0
tot_cartas = 0

for i in range(1, n+1):
    tot_baralho = tot_baralho + i

for i in range(n-1):
    carta = int(input())
    tot_cartas = tot_cartas + carta

print(f"{tot_baralho-tot_cartas}")