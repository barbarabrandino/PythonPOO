
def cpf_idade():
    cpf=input("Digite seu cpf: ")

    if len(cpf) !=11:
        raise ValueError("Digite um cpf válido!")
    print(f"CPF válido: {cpf}")
    
    try:
        cpf()
    except ValueError as error:
        print(error)

