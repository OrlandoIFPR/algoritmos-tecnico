num_linhas = int(input())
for _ in range(num_linhas):
    linha = input()
    meio = len(linha)//2
    
    lado1 = linha[:meio]
    lado2 = linha[meio:]
    lado1_invertido = lado1[::-1]
    lado2_invertido = lado2[::-1]
    
    print(f"{lado1_invertido}{lado2_invertido}")