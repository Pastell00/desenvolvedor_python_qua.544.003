# Lista de dicionarios

usuários = [
    {
    "nome": "Fulano de tal",
    "idade": 24,
    "email": "Fulano@gmail.com",
    "cpf": "123.456.789-12"
    },
    {
    "nome": "Cicrano",
    "idade": 40,
    "email": "Fulano@gmail.com",
    "cpf": "123.456.789-12"
    }
]

# Percorre a lista de dicionários
for usuário in usuários:
    for chave, valor in usuário.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")