import re

def validar_senha():
    padrao1, padrao2, padrao3, padrao4, padrao5 = define_os_padroes()
    senha = captura_a_senha()
    mensagens_erro = []
    realiza_verificacoes(padrao1, padrao2, padrao3, padrao4, padrao5, senha, mensagens_erro)


def define_os_padroes():
    padrao1 = r"(?=.*[a-z])"
    padrao2 = r"(?=.*[A-Z])"
    padrao3 = r"(?=.*[0-9])"
    padrao4 = r"(?=.*[@#*!$%^&+])"
    padrao5 = r".{8,}"

    return padrao1, padrao2, padrao3, padrao4, padrao5


def captura_a_senha():
    senha = input("""Digite uma senha para validar.
                A senha deve conter no mínimo 8 caracteres.
                A senha deve conter pelo menos uma letra minúscula.
                A senha deve conter pelo menos uma letra maiúscula.
                A senha deve conter pelo menos um dígito (0-9).
                A senha deve conter pelo menos um caractere especial, como @, #, !, $, %, ^, *, & ou +\n""")

    return senha


def realiza_verificacoes(padrao1, padrao2, padrao3, padrao4, padrao5, senha, mensagens_erro):
    
    if not re.search(padrao1, senha):
        mensagens_erro.append("A senha deve conter pelo menos uma letra minúscula.")

    if not re.search(padrao2, senha):
        mensagens_erro.append("A senha deve conter pelo menos uma letra maiúscula.")

    if not re.search(padrao3, senha):
        mensagens_erro.append("A senha deve conter pelo menos um dígito (0-9).")

    if not re.search(padrao4, senha):
        mensagens_erro.append("A senha deve conter pelo menos um caractere especial.")

    if not re.search(padrao5, senha):
        mensagens_erro.append("A senha deve ter no mínimo 8 caracteres.")

    if not mensagens_erro:
        print("A senha é válida.")
    else:
        print("A senha é inválida.")
        for mensagem in mensagens_erro:
            print(mensagem)


if __name__ == "__main__":
    validar_senha()
