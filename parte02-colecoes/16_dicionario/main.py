# Dicionário
usuário = {
    "nome": "Fulano de tal",
    "idade": 24,
    "email": "Fulano@gmail.com",
    "cpf": "123.456.789-12"
}

# Exibe os dados do dicionário
print("Forma 1:")
print(f"Nome: {usuário["nome"]}")
print(f"Idade: {usuário["idade"]}")
print(f"email: {usuário["email"]}")
print(f"cpf: {usuário["cpf"]}")

# Forma 2
print("Forma 2:")
print(f"Nome: {usuário.get("nome")}")
print(f"Idade: {usuário.get("idade")}")
print(f"email: {usuário.get("email")}")
print(f"cpf: {usuário.get("cpf")}")

# Forma 3
print("forma 3:")
for chave in usuário:
    print(f"{chave.capitalize()}: {usuário.get(chave)}")