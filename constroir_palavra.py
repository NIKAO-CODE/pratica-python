# Criar um programa que recebe letras aleatórias e adivinha a palavra

lista_palavras = ['uva']
verifica = []
palavra_da_lista_separada = []

letras = input("Digite até 46 letras: ")
letras_quantidade = int(len(letras))

for l in letras:
    verifica.append(l)
print(verifica, "separando letras")


for palavra in lista_palavras:
    caracteres_item = [letra for letra in palavra]
    palavra_da_lista_separada.append(caracteres_item)
print(palavra_da_lista_separada, "separando letras da palavra da lista")


for item in lista_palavras:
    palavra_atual = item
    numero_caracteres = len(palavra_atual)
    if(letras_quantidade == numero_caracteres) and (verifica in palavra_da_lista_separada):
        print(palavra_atual)
