países = [
    "Brasil",
    "Estados Unidos",
    "México",
    "Argentina",
    "Brasil",
    "Argentina",
    "Arábia Saudita",
    "Irã",
    "Brasil",
    "México",
    "Estados Unidos",
    "Brasil"
]

país = input("Informe o país a ser pesquisado: ").strip().title()

#armazena a quantidade de ocorrências na lista
quantidade = países.count(país)

print(f"{país} foi encontradp {quantidade} vezes na lista.")