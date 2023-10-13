# Criar um programa que le uma entrada com letras aleatórias e monta essa palavra conforme as lista de palavras

lista_palavras = ['uva']

letras = input("Digite até 46 letras: ").lower()

criar_lista_com_letras = [i for i in letras]
delimitador = ''
letras_concatenadas = delimitador.join(criar_lista_com_letras)


if(len(letras_concatenadas) == len(lista_palavras[0])) and (letras_concatenadas in lista_palavras[0]):
    print("oi")
else:
    print("Erro")

    