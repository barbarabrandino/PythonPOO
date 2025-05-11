def solicitar_inteiro():
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número inteiro.")
    else:
        print(f"Você digitou o número: {numero}")


solicitar_inteiro()
