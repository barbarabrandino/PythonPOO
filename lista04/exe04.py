def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade inválida: a idade não pode ser negativa.")
    else:
        print(f"Idade registrada: {idade} anos")


verificar_idade(20)   
verificar_idade(-5)   
