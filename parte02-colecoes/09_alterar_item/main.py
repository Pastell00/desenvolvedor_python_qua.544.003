nomes = [
    "Fulano",
    "Cicrano",
    "Beltrano",
    "João",
    "Maria",
    "José",
    "Esmeralda"
]

# usuário informa o nome que deseja alterar
nome_antigo = input("Informe o nome que deseja alterar: ").strip().title()

# armazena a posição do nome na lsita caso exista
if nome_antigo in nomes:
    índice = nomes.index(nome_antigo)
    nomes[índice] = input("Informe o novo nome: ").strip().title()
    print("Nome alterado com sucesso!")
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado.")