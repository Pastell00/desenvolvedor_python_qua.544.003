# TODO: atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
# O programa deve calcular a média do aluno e informar se 
# o aluno está aprovado (média mínima = 7) ou reprovado.
# O programa deve gravar esses dados em um JSON.
# Ao final, o usuário deverá escolher se deseja inserir as 
# notas de outro aluno, que deverão ser gravadas no mesmo
# arquivo JSON.

import json
import os

Alunos = []
abrir = ""

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Cadastrar aluno")
    print("2 - Cadastrar outro aluno")
    print("3 - Mostrar lista dos alunos")
    print("4 - Sair do programa")

    

    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    if opcao == "1" or opcao == "2":
        aluno = {}
        aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
        aluno['nota'] = input("Informe a nota do aluno: ").strip().lower()

   
        Alunos.append(aluno)

        match opcao:
            case "1":
                arquivo = input("Informe o nome do aluno: ")

                with open(f"atividade_03/{arquivo}.json","w",encoding="utf-8") as f:
                    json.dump(Alunos, f)
            case "2":
                if abrir:
                    with open(f"atividade_03/{abrir}.json","w",encoding="utf-8") as f:
                        json.dump(Alunos, f)
    else:
        match opcao:
            case "3":
                abrir = input("Informe o nome do arquivo que deseja abrir: ")

                with open(f"atividade_03/{abrir}.json","r",encoding="utf-8") as f:
                    Alunos = json.load(f)

                for aluno in Alunos:
                    for chave, valor in aluno.items():
                        print(f"{chave.capitalize()}: {valor}")
            case "4":
                break
            case _:
                print("Opção inválida.")
                continue

numeros = []

total_soma = sum(numeros)

print(f"Total da soma: {total_soma}")