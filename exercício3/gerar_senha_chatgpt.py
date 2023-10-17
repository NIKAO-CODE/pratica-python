import random
import string

def gerar_senha():
    comprimento = int(input("Digite o comprimento desejado da senha: "))

    usar_minusculas = input("Incluir letras minúsculas? (S ou N): ").strip().lower() == 's'
    usar_maiusculas = input("Incluir letras maiúsculas? (S ou N): ").strip().lower() == 's'
    usar_digitos = input("Incluir dígitos? (S ou N): ").strip().lower() == 's'
    usar_especiais = input("Incluir caracteres especiais? (S ou N): ").strip().lower() == 's'

    caracteres = ''

    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_digitos:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("Você deve selecionar pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))

    print("Senha gerada:", senha)

if __name__ == "__main__":
    gerar_senha()
