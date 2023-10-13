# Criar um programa que le uma entrada com uma palavra e monta essa palavra conforme as letras do alfabeto

print("Digite uma palavra para o programa montar a palavra baseado no alfabeto.")
print(59 * "*")

alfabeto = ["A", "Á", "À", "Â", "Ã", "B", "C", "Ç", "D", "E", "É", "Ê", "F", "G", "H", "I", "Í", "J", "K", "L", "M", "N", "O", "Ó", "Ô", "Õ", "P", "Q", "R", "S", "T", "U", "Ú", "Û", "V", "W", "X", "Y", "Z"]

palavra = input("Digite uma palavra: ").upper()

palavra_montada = [letra for letra in palavra if letra in alfabeto]

print(palavra_montada)
