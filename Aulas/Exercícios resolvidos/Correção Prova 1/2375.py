diametro = int(input())
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if diametro <= x and diametro <= y and diametro <= z:
    print('S')
else:
    print('N')