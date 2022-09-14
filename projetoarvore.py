print("\n")
print("|>>>>>>O famoso banco de dados de doenças da soja de Michalski<<<<<<|")
print("|                                                                   | ")
print("|                                                                   | ")
print("|>>>>>>--------------------SEJA BEM VINDO!------------------<<<<<<<<| ")
print("|                                                                   | ")
print("|>>>>>>--------------------Qual seu nome?-------------------<<<<<<<<| ")
print("|                                                                   |\n")
nome=input(" Nome: ")
print("")
valorfru=int(input(" {} Escolha um valor para Fruitpods: " .format(nome)))
if valorfru > 0: #cankerlesion#
    valorcan=int(input(" {} Escolha um valor para Cankerlesion: " .format(nome)))
    if valorcan > 1:
        print("")
        print(' Resultado da classe \033[1;30;43mD4\033[m')
    else:
        print("")
        print(' Resultado da classe \033[1;30;42mD3\033[m')
else:
    precip=int(input(" {} Escolha um valor para Precip: ".format(nome)))
    if precip > 0:
        print("")
        print(' Resultado da classe \033[1;30;44mD1\033[m')
    else:
        print("")
        print(' Resultado da classe \033[1;30;41mD2\033[m')