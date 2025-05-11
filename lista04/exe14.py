def dividir_numeros():
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        resultado = a / b
    except ValueError:
        print("Erro: você deve digitar apenas números inteiros.")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero.")
    else:
        print(f"Resultado da divisão: {resultado}")
    finally:
        print("Operação finalizada.")


dividir_numeros(20,5)
