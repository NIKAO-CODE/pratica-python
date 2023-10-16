def analise_de_frase():
    vogais     = ['a', 'e', 'i', 'o', 'u']
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    frase, escolha = captura_frase_e_escolha()

    match escolha:
        case 1:
            contar_caracteres(frase)

        case 2:
            contar_vogais(frase, vogais)

        case 3:
            contar_consoantes(frase, consoantes)

        case 4:
            transformar_em_minuscula(frase)

        case 5:
            transformar_em_maiuscula(frase)

        case 6:
            inverter_frase(frase)

        case 7:
            colocar_quebra_de_linha(frase)

        case 8:
            verifica_palindromo(frase)

        case 9:
            porcentagem_da_letra(frase)
        
        case 0:
            sair(escolha)


def captura_frase_e_escolha():
    frase = input("Digite uma frase para analisar: ")

    escolha = int(input("""O que você deseja fazer?
        [0] Sair.
        [1] Quantidade de letras.
        [2] Quantidade de vogais.
        [3] Quantidade de consoantes.
        [4] Transformar em minúscula.
        [5] Transformar em maiúscula.
        [6] Inverter a frase.
        [7] Colocar quebra de linha nos espaços.
        [8] Verificar se é um Palíndromo
        [9] Verificar quantos % uma letra representa em uma frase.\n"""))
    
    return frase, escolha


def contar_caracteres(frase):
    frase_formatada = frase.strip().replace(" ", "")
    qtd = len(frase_formatada)
    print("A frase tem {} caracteres".format(qtd))


def contar_vogais(frase, vogais):
    frase_formatada = frase.strip().lower().replace(" ", "")
    vogais_encontradas = [l for l in frase_formatada if l in vogais]
    qtd_vogais = len(vogais_encontradas)
    print("Encontramos {} vogais, são elas: {}".format(qtd_vogais, vogais_encontradas))


def contar_consoantes(frase, consoantes):
    frase_formatada = frase.strip().lower().replace(" ", "")
    consoantes_encontradas = [l for l in frase_formatada if l in consoantes]
    qtd_consoantes = len(consoantes_encontradas)
    print("Encontramos {} consoantes, são elas: {}".format(qtd_consoantes, consoantes_encontradas))


def transformar_em_minuscula(frase):
    frase_formatada = frase.strip().lower()
    print(frase_formatada)


def transformar_em_maiuscula(frase):
    frase_formatada = frase.strip().upper()
    print(frase_formatada)


def inverter_frase(frase):
    frase_formatada = frase.strip()
    print(frase_formatada[::-1])


def colocar_quebra_de_linha(frase):
    frase_formatada = frase.strip().replace(" ", "\n")
    print(frase_formatada)


def verifica_palindromo(frase):
    frase_formatada = frase.strip().lower().replace(" ", "").replace("-", "")
    frase_invertida = frase_formatada[::-1]

    if (frase_formatada == frase_invertida):
        print("'{}' é um Palíndromo.".format(frase))
    else:
        print("'{}' não é um Palíndromo.".format(frase))


def porcentagem_da_letra(frase):
    frase_formatada = frase.strip().lower()
    letra_escolhida = input("Qual letra você quer verificar? ")

    ocorrencia = frase_formatada.count(letra_escolhida)

    porcentagem = (ocorrencia / len(frase_formatada)) * 100

    print("A letra '{}' representa {:.1f}% da frase.".format(letra_escolhida, porcentagem))


def sair(escolha):
    while True:
        if (escolha == 0):
            print("Execução finalizada!")
            break


if __name__ == "__main__":
    analise_de_frase()
