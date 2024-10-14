casos = int(input())
for _ in range(casos):
    num_pessoas = int(input())
    idioma_ant = ""
    idioma_at = ""
    ingles = False
    for j in range(num_pessoas):
        if j==0:
            idioma_ant = input()
        else:
            idioma_at = input()
            if idioma_ant != idioma_at:
                ingles = True
            
            idioma_ant = idioma_at
    if ingles:
        print('ingles')
    else:
        print(idioma_ant)
    
    