import math
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def area_qudrilatero(b, h):
    return b*h

def area_triangulo(b,h):
    return(b*h)/2

def area_circulo(r):
    return math.pi(r**2)

# algoritmo principal
limpar()

while True:
    print("1 _ Calcular área quadrilaátero.")
    print("2 _ Calcular área do triângulo.")
    print("3 _ Calcular área do circulo.")
    print("4 _ Sair do programa.")
    opção = input("informe a opção desejada: ").strip()
    limpar()
    match opção:
        case "1":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"Área do quadrilátero é {area_qudrilatero(b,h)}.")
            continue
        case "2":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"Área do quadrilátero é triângulo é {area_triangulo(b,h)}")
            continue
        case "3":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"Área do circulo é {area_circulo(b,h)}.")
            continue