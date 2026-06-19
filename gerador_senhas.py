import random
import string


def gerar_senha_numerica(tamanho):
    numeros = string.digits
    senha = "".join(random.choice(numeros) for _ in range(tamanho))
    return senha


def gerar_senha_completa(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def salvar_senhas(senhas):
    with open("senhas_geradas.txt", "a") as arquivo:
        arquivo.write("=== NOVA GERAÇÃO ===\n")
        for senha in senhas:
            arquivo.write(senha + "\n")
        arquivo.write("\n")


def pedir_quantidade():
    while True:
        entrada = input("Quantas senhas deseja gerar? ")

        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)

        print("Digite um número válido maior que 0.")


def pedir_tamanho():
    while True:
        entrada = input("Quantos caracteres você quer na senha? ")

        if entrada.isdigit() and int(entrada) >= 4:
            return int(entrada)

        print("Por favor, digite um número inteiro de pelo menos 4.")


def mostrar_menu():
    print("\n=== Gerador de Senhas ===")
    print("1 - Senha numérica (múltiplas)")
    print("2 - Senha completa (múltiplas)")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()
    return opcao


def main():
    print("Bem-vindo ao gerador de senhas!")

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            tamanho = pedir_tamanho()
            quantidade = pedir_quantidade()

            senhas = []

            for _ in range(quantidade):
                senhas.append(gerar_senha_numerica(tamanho))

            for i, senha in enumerate(senhas, 1):
                print(f"Senha {i}: {senha}")

            salvar_senhas(senhas)
            print("\nSenhas salvas em senhas_geradas.txt")

        elif opcao == "2":
            tamanho = pedir_tamanho()
            quantidade = pedir_quantidade()

            senhas = []

            for _ in range(quantidade):
                senhas.append(gerar_senha_completa(tamanho))

            for i, senha in enumerate(senhas, 1):
                print(f"Senha {i}: {senha}")

            salvar_senhas(senhas)
            print("\nSenhas salvas em senhas_geradas.txt")

        elif opcao == "0":
            print("\nAté mais!")
            break

        else:
            print("\nOpção inválida. Digite 1, 2 ou 0.")


if __name__ == "__main__":
    main()
