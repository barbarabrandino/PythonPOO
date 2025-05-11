def calcular_media(lista):
    try:
        soma = sum(lista)
        media = soma / len(lista)
    except TypeError:
        print("Erro: A lista contém elementos que não são números.")
    else:
        print(f"A média é: {media:.2f}")


numeros_validos = [10, 20, 30]
numeros_invalidos = [10, "vinte", 30]

calcular_media(numeros_validos)     
calcular_media(numeros_invalidos)   
