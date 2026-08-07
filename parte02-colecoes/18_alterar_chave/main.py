usuário = {
    "nome": "Fulano de tal",
    "idade": 24,
    "email": "Fulano@gmail.com",
    "cpf": "123.456.789-12"
}

# Usuário informa a chave que deseja alterar
chave = input("Informe o nome da chave: ").strip().lower()

if chave in usuário:
    usuário[chave] = input(f"Informe o novo valor para {chave}: ").strip()
    # Exibe o dicionário com o novo valor da chave escolhida

    for chave, valor in usuário.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print("Chave não encontrada.")
    