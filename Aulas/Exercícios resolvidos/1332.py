num_ent = int(input())
for _ in range(num_ent):
    numero = input()
    
    if len(numero) == 5:
        print(3)
    elif (numero[0] == 'o' and numero[1] == 'n') or (numero[0] == 'o' and numero[2] == 'e') or (numero[1] == 'n' and numero[2] == 'e'):
        print(1)
    else:
        print(2)