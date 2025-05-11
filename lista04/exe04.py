
def validade_idade():
    idade=int(input("Digite sua idade: "))

    if idade <0:
        raise ValueError("Digite a idade maior do que zero!")
        print(f"Idade válida: {idade}")
    
    try:
        validade_idade()
    except ValueError as error:
        print(error)
