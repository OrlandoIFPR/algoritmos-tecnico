num_ent = int(input())
for _ in range(num_ent):
    palavra1, palavra2 = input().split()
    
    saida = ""
    
    if len(palavra1) < len(palavra2):
        for i in range(len(palavra1)):
            saida = saida + palavra1[i] + palavra2[i]
        
        saida = saida + palavra2[len(palavra1): ]
    else:
        for i in range(len(palavra2)):
            saida = saida + palavra1[i] + palavra2[i]
        
        saida = saida + palavra1[len(palavra2): ]
  
    
    print(saida)