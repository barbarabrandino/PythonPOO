def validar_cpf(cpf):
    try:
        if len(cpf) < 11:
            raise ValueError("CPF inválido: deve conter pelo menos 11 caracteres.")
    except ValueError as erro:
        print(f"Erro ao validar CPF: {erro}")
    else:
        print("CPF válido.")
