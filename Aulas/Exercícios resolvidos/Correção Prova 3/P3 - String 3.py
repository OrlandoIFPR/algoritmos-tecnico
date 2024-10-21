info = input()

letra_ant = info[0]
cont_repetidas = 1

resultado = ''

for i in range(1, len(info)):
    if info[i] == letra_ant:
        cont_repetidas = cont_repetidas + 1
    else:
        resultado = resultado + letra_ant + str(cont_repetidas)
        letra_ant = info[i]
        cont_repetidas = 1

resultado = resultado + letra_ant + str(cont_repetidas)

print(resultado)
        