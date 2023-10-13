arquivo = open("palavras.txt", "r", encoding="utf8")
lista_palavras = []

for linha in arquivo:
    linha = linha.strip().lower()
    lista_palavras.append(linha)

arquivo.close()

palavra_da_lista_separada = []

letras = input("Digite até 46 letras: ")
letras_quantidade = len(letras)

verifica = [l for l in letras]

for palavra in lista_palavras:
    caracteres_item = [letra for letra in palavra]
    palavra_da_lista_separada.append(caracteres_item)

for item in lista_palavras:
    palavra_atual = item
    numero_caracteres = len(palavra_atual)
    if letras_quantidade == numero_caracteres:
        formavel = True
        for letra in palavra_da_lista_separada[0]:
            if letra not in verifica:
                formavel = False
                break
        if formavel:
            print(palavra_atual)
