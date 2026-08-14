# declara uma função

def boas_vindas(nome):
    print("Seja bem vindo, {nome}! 😎🐍")

# algoritmo principal
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)