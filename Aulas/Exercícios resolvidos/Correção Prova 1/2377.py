
km_rodovia, dist_pedagio = input().split()
km_rodovia = int(km_rodovia)
dist_pedagio = int(dist_pedagio)

custo_km, custo_pedagio = input().split()
custo_km = int(custo_km)
custo_pedagio = int(custo_pedagio)


custo = km_rodovia*custo_km + km_rodovia//dist_pedagio*custo_pedagio

print(custo)