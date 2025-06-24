"""
Professor Renato
Matéria : Teoria da computação e Compiladores

Guilherme de Oliveira Rodrigues RA: 105926 
Marcos Roberto Pinto Ribeiro Junior RA:109243
Leonardo Milani Pigatti RA:110542

"""

import os
from parser import rodar_parser # Importa a funcao com o nome novo

# Funcao principal que roda tudo
def main():
    # Pega o caminho do arquivo C++ pra analisar
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo_cpp = os.path.join(caminho_atual, "teste1.cpp ")

    # teste1.cpp 
    # teste2.cpp
    # teste3.cpp

    # Roda o parser
    resultado_final = rodar_parser(caminho_arquivo_cpp)

    if resultado_final:
        print(resultado_final)
    else:
        print("Nao foi possivel concluir a analise.")

if __name__ == "__main__":
    main()