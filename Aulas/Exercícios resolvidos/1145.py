
passo, fim = map(int, input().split())

for i in range (1, fim+1):
    if i%passo == 0:
        print(i)
    else:
        print(i, end=" ")