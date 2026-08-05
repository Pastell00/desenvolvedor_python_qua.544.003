nomes = [
    "Fulano",
    "Cicrano",
    "Beltrano",
    "João",
    "Maria",
    "José",
    "Esmeralda"
]

nome =  input("Informe o nome a ser deletado: ").strip().title()

if nome in nomes:
    índice = nomes.index(nome)

    # apaga item da lista
    del(nomes[índice])

    # exibe a nova lista sem o item deletado
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado.")