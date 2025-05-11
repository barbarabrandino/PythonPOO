def dividir(n1, n2):
    try:
        resultado = n1 / n2
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    else:
        print(f"O resultado da divisão é: {resultado}")


dividir(10, 2)   