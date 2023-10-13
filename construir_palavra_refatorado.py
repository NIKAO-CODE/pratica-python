arquivo = open("palavras.txt", "r", encoding="utf8")
lista_palavras = []

for linha in arquivo:
    linha = linha.strip().lower()
    lista_palavras.append(linha)

arquivo.close()

letras = input("Digite até 46 letras: ")
letras_quantidade = len(letras)

for palavra in lista_palavras:
    if (len(palavra) == letras_quantidade):
        letras_palavra = list(palavra)
        letras_disponiveis = list(letras)
        formavel = True

        for letra in letras_palavra:
            if (letra in letras_disponiveis):
                letras_disponiveis.remove(letra)
            else:
                formavel = False
                break

        if (formavel):
            print(palavra.capitalize(), "pode ser formada com as letras fornecidas.")
