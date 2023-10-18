def calculadora():
    try:
        imprime_mensagens_inicias()
        escolha, entrada = captura_escolha_do_usuario()
        lista_notas = cria_lista_de_notas(entrada)
        realiza_as_condiconais(escolha, lista_notas)
    except:
        print("Aconteceu um erro. Certifique-se de fornecer uma escolha válida e notas válidas.")


# funções responsáveis pelo funcionamento da função calculadora
def imprime_mensagens_inicias():
    print("*" * 50)
    print("Calculadora de Estatística")
    print("*" * 50)
    print("""O que você deseja fazer?
        [1] Média das notas.
        [2] Nota mais alta.
        [3] Nota mais baixa.
        [4] Quantas notas estão acima da média.
        [5] Quantas notas estão abaixo da média""")


def captura_escolha_do_usuario():
    try:
        while True:
            escolha = int(input("Digite a sua escolha: "))
            if (escolha < 1 or escolha > 5):
                print("Opção inválida!")
                continue
            else:
                entrada = input("Digite as notas separado por espaço: (somente números) ")

            return escolha, entrada
    except:
        print("Aconteceu um erro. Certifique-se de fornecer uma escolha válida e notas válidas.")


def cria_lista_de_notas(entrada):
    notas = entrada.split(" ")
    lista_notas = [float(n) for n in notas]

    return lista_notas


def realiza_as_condiconais(escolha, lista_notas):

    notas_acima_da_media = []
    notas_abaixo_da_media = []
    nts_acima = ""
    nts_abaixo = ""

    match escolha:

        #Média das notas
        case 1:
            media = (sum(lista_notas)) / len(lista_notas)
            print("A média das notas é {:.1f}".format(media))

        #Nota mais alta
        case 2:
            maior_nota = max(lista_notas)
            print("A maior nota é {}".format(maior_nota))

        #Nota mais baixa
        case 3:
            menor_nota = min(lista_notas)
            print("A menor nota é {}".format(menor_nota))

        #Quantas notas estão acima da média
        case 4:
            media = (sum(lista_notas)) / len(lista_notas)

            notas_acima_da_media = [str(n) for n in lista_notas if n > media]
            nts_acima = ", ".join(notas_acima_da_media)

            verifica_como_deve_imprimir(notas_acima_da_media, notas_abaixo_da_media, nts_acima, nts_abaixo, media)

        #Quantas notas estão abaixo da média
        case 5:
            media = (sum(lista_notas)) / len(lista_notas)

            notas_abaixo_da_media = [str(n) for n in lista_notas if n < media]
            nts_abaixo = ", ".join(notas_abaixo_da_media)

            verifica_como_deve_imprimir(notas_acima_da_media, notas_abaixo_da_media, nts_acima, nts_abaixo, media)


#verifica como imprimir a mensagem para o usuário
def verifica_como_deve_imprimir(notas_acima_da_media, notas_abaixo_da_media, nts_acima, nts_abaixo, media):

    if (len(notas_acima_da_media) > 1):
        print("As notas {} estão acima da média: {:.2f}.".format(nts_acima, media))
    elif (len(notas_abaixo_da_media) > 1):
        print("As notas {} estão abaixo da média: {:.2f}.".format(nts_abaixo, media))
    elif (len(notas_acima_da_media) == 1):
        print("A nota {} está acima da média: {:.2f}.".format(nts_acima, media))
    else:
        print("A nota {} está abaixo da média: {:.2f}.".format(nts_abaixo, media))



if __name__ == "__main__":
    calculadora()