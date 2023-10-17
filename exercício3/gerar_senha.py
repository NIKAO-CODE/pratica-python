import random

#função principal
def gerar_senha():
    print(48 * "*")
    print(3 * "*" + " Bem-vindo(a) ao gerador de senhas online " + 3 * "*")
    print(48 * "*")

    print("""Para gerar a senha informe a quantidade de caracteres e escolha a opção que atende a sua solicitação.
        Lembrando que não geramos senha com apenas 1 tipo de caractere,
        por exemplo: 'aaaa'
        Opções:
                [1] Letras minúsculas, dígitos
                [2] Letras minúsculas, letras maiúsculas
                [3] Letras minúsculas, caracteres especiais
                [4] Letras minúsculas, letras maiúsculas, dígitos
                [5] Letras minúsculas, dígitos, caracteres especiais
                [6] Letras minúsculas, letras maiúsculas, caracteres especiais
                [7] Letras minúsculas, letras maiúsculas, dígitos, caracteres especiais""")


    #cria listas para usar ao gerar as senhas
    alfabeto_maiusculo = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    alfabeto_minusculo = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres_especiais = ['@', '#', '*', '!', '$', '%', '^', '&', '+']

    
    gerar_senha = []
    impar = 0


    #captura a escolha do usuário
    escolha_usuario = int(input("Digite sua escolha: "))
    qtd_caracteres = int(input('Digite a quantidade de caracteres: '))
    qtd_caracteres_original = qtd_caracteres


    #desenvolve a lógica
    match escolha_usuario:

        #Letras minúsculas, dígitos
        case 1:

            if (qtd_caracteres % 2 == 0):
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
            else:
                impar = qtd_caracteres
                qtd_caracteres += 1
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
        
        #Letras minúsculas, letras maiúsculas
        case 2:
            if (qtd_caracteres % 2 == 0):
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
            else:
                impar = qtd_caracteres
                qtd_caracteres += 1
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)

        #Letras minúsculas, caracteres especiais
        case 3:
            if (qtd_caracteres % 2 == 0):
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
            else:
                impar = qtd_caracteres
                qtd_caracteres += 1
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)

        #Letras minúsculas, letras maiúsculas, dígitos
        case 4:
            if (qtd_caracteres % 2 == 0):
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
            else:
                impar = qtd_caracteres
                qtd_caracteres += 1
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)

        #Letras minúsculas, dígitos, caracteres especiais
        case 5:
            if (qtd_caracteres % 2 == 0):
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
            else:
                impar = qtd_caracteres
                qtd_caracteres += 1
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)

        #Letras minúsculas, letras maiúsculas, caracteres especiais
        case 6:
            if (qtd_caracteres % 2 == 0):
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
            else:
                impar = qtd_caracteres
                qtd_caracteres += 1
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)

        #Letras minúsculas, letras maiúsculas, dígitos, caracteres especiais
        case 7:
            if (qtd_caracteres % 2 == 0):
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)
            else:
                impar = qtd_caracteres
                qtd_caracteres += 1
                adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original)


#funções

#função geral
def adiciona_caractere(qtd_caracteres, escolha_usuario, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais, gerar_senha, impar, qtd_caracteres_original):

    qtd_caracteres = int(qtd_caracteres / 2)

    if (escolha_usuario == 1):
        opcao1(qtd_caracteres, gerar_senha, alfabeto_minusculo, digitos)
    elif (escolha_usuario == 2):
        opcao2(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo)
    elif (escolha_usuario == 3):
        opcao3(qtd_caracteres, gerar_senha, alfabeto_minusculo, caracteres_especiais)
    elif (escolha_usuario == 4):
        opcao4(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo, digitos)
    elif (escolha_usuario == 5):
        opcao5(qtd_caracteres, gerar_senha, alfabeto_minusculo, digitos, caracteres_especiais)
    elif (escolha_usuario == 6):
        opcao6(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo, caracteres_especiais)
    else:
        opcao7(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais)


    #caso o usuário escolha uma quantidade ímpar
    if (impar):
        gerar_senha.pop()

    senha = "".join(gerar_senha)

    print("Senha gerada: {}".format(senha[:qtd_caracteres_original]))



#funções secundárias, responsáveis por criar a senha

#Letras minúsculas, dígitos
def opcao1(qtd_caracteres, gerar_senha, alfabeto_minusculo, digitos):
    for _ in range(qtd_caracteres):
        gerar_senha.append(random.choice(alfabeto_minusculo))
        gerar_senha.append(random.choice(digitos))


#Letras minúsculas, letras maiúsculas
def opcao2(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo):
    for _ in range(qtd_caracteres):
        gerar_senha.append(random.choice(alfabeto_minusculo))
        gerar_senha.append(random.choice(alfabeto_maiusculo))


#Letras minúsculas, caracteres especiais
def opcao3(qtd_caracteres, gerar_senha, alfabeto_minusculo, caracteres_especiais):
    for _ in range(qtd_caracteres):
        gerar_senha.append(random.choice(alfabeto_minusculo))
        gerar_senha.append(random.choice(caracteres_especiais))


#Letras minúsculas, letras maiúsculas, dígitos
def opcao4(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo, digitos):
    for _ in range(qtd_caracteres):
        gerar_senha.append(random.choice(alfabeto_minusculo))
        gerar_senha.append(random.choice(alfabeto_maiusculo))
        gerar_senha.append(random.choice(digitos))


#Letras minúsculas, dígitos, caracteres especiais
def opcao5(qtd_caracteres, gerar_senha, alfabeto_minusculo, digitos, caracteres_especiais):
    for _ in range(qtd_caracteres):
        gerar_senha.append(random.choice(alfabeto_minusculo))
        gerar_senha.append(random.choice(digitos))
        gerar_senha.append(random.choice(caracteres_especiais))


#Letras minúsculas, letras maiúsculas, caracteres especiais
def opcao6(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo, caracteres_especiais):
    for _ in range(qtd_caracteres):
        gerar_senha.append(random.choice(alfabeto_minusculo))
        gerar_senha.append(random.choice(alfabeto_maiusculo))
        gerar_senha.append(random.choice(caracteres_especiais))


#Letras minúsculas, letras maiúsculas, dígitos, caracteres especiais
def opcao7(qtd_caracteres, gerar_senha, alfabeto_minusculo, alfabeto_maiusculo, digitos, caracteres_especiais):
    for _ in range(qtd_caracteres):
        gerar_senha.append(random.choice(alfabeto_minusculo))
        gerar_senha.append(random.choice(alfabeto_maiusculo))
        gerar_senha.append(random.choice(digitos))
        gerar_senha.append(random.choice(caracteres_especiais))



if __name__ == '__main__':
     gerar_senha()