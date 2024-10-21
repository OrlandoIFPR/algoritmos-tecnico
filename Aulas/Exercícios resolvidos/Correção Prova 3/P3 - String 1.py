palavra = input()

#if palavra == palavra.upper():
#    print('S')
#else: 
#    print('N')

todas_maiusculas = True

for letra in palavra:
    if letra < 'A' or letra > 'Z':
        todas_maiusculas = False
        
if todas_maiusculas:
    print('S')
else: 
    print('N')
    
