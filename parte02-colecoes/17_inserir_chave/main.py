usuário = {
    "nome": "Fulano de tal",
    "idade": 24,
    "email": "Fulano@gmail.com",
    "cpf": "123.456.789-12"
}

# Adiciona a chave telefone ao dicionário
usuário["telefone"] = input(f"Informe o tlefone de {usuário.get("nome")}: ").strip()

# Exibe o dicionário
for chave in usuário:
    print(f"{chave.capitalize()}: {usuário.get(chave)}")