votantes = int(input())

cand1 = 0
cand2 = 0
cand3 = 0

for i in range(votantes):
    voto = int(input())
    if voto == 1:
        cand1 = cand1 + 1
    elif voto == 2:
        cand2 = cand2 + 1
    elif voto == 3:
        cand3 = cand3 + 1
        
if cand1 > cand2 and cand1 > cand3:
    print("Candidato 1")
elif cand2 > cand1 and cand2 > cand3:
    print("Candidato 2")
elif cand3 > cand1 and cand3 > cand2:
    print("Candidato 3")