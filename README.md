# Projeto CalcSintaxe

Analisador Léxico e Sintático desenvolvido para a disciplina de Teoria da Computação e Compiladores.

---

### **Informações da Turma**

* **Professor:** Renato
* **Matéria:** Teoria da Computação e Compiladores

### **Autores**

* Guilherme de Oliveira Rodrigues - RA: 105926
* Marcos Roberto Pinto Ribeiro Junior - RA: 109243
* Leonardo Milani Pigatti - RA: 110542

---

## 1. Descrição do Projeto

Este projeto consiste na implementação do **front-end de um compilador**, responsável por realizar a **análise léxica** e a **análise sintática** de um código-fonte escrito em uma linguagem que é um subconjunto simplificado do C++.

O analisador é capaz de processar um arquivo de código, validá-lo contra um conjunto de regras gramaticais e realizar checagens semânticas básicas, como a declaração de variáveis.

## 2. Funcionalidades Implementadas

* **Análise Léxica:** Reconhecimento de tokens, incluindo:
    * Palavras-chave (`if`, `else`, `while`, `int`, `float`, etc.).
    * Identificadores (nomes de variáveis e funções).
    * Constantes (números inteiros e de ponto flutuante).
    * Operadores (aritméticos, relacionais e de atribuição).
    * Símbolos de pontuação (parênteses, chaves, ponto e vírgula).
    * Ignora comentários (`// ...` e `/* ... */`) e diretivas de pré-processador (`#include ...`).

* **Análise Sintática:** Validação da estrutura do código com suporte a:
    * Múltiplas definições de funções.
    * Declarações de variáveis (únicas ou múltiplas na mesma linha).
    * Comandos de atribuição.
    * Estruturas de controle `if-else` e laços `while`.
    * Aninhamento de blocos de controle (ex: `if` dentro de um `while`).
    * Expressões aritméticas e relacionais complexas, com respeito à precedência de operadores.

* **Análise Semântica (Básica):**
    * Uso de uma **Tabela de Símbolos** para armazenar informações sobre as variáveis.
    * Detecção de erro para **redeclaração de variáveis**.
    * Detecção de erro para **uso de variáveis não declaradas**.

## 3. Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Biblioteca:** `PLY` (Python Lex-Yacc) - para a construção dos analisadores léxico e sintático.

## 4. Estrutura do Projeto

* `main.py`: O script principal que inicializa a análise e orquestra a execução.
* `lexer.py`: Contém a definição de todos os tokens da linguagem e as regras para o analisador léxico.
* `parser.py`: Contém a gramática da linguagem, as regras de produção, a lógica da análise sintática e o tratamento da tabela de símbolos.
* `testes.cpp`: Arquivos de exemplo com código-fonte para serem analisados pelo compilador.

## 5. Como Executar

**Pré-requisitos:**
* Ter o Python 3 instalado.
* Instalar a biblioteca PLY.

**1. Instale a biblioteca PLY:**
```bash
pip install ply
```

**2. Configure o arquivo de entrada:**
Abra o arquivo `main.py` e certifique-se de que a variável `caminho_arquivo_cpp` aponta para o arquivo de teste que você deseja analisar (ex: `main.cpp`, `teste_final.cpp`).

```python
# Em main.py
caminho_arquivo_cpp = os.path.join(caminho_atual, "teste_final.cpp")
```

**3. Execute o projeto:**
Abra um terminal na pasta raiz do projeto e execute o seguinte comando:
```bash
python main.py
```

A saída da análise será exibida no terminal, mostrando a estrutura do programa reconhecida e a tabela de símbolos final.

## 6. Limitações e Próximos Passos

Este projeto é uma base funcional, mas possui limitações que podem ser abordadas em trabalhos futuros:
* **Geração de Código:** O projeto não gera código de máquina nem uma representação intermediária, como uma Árvore de Sintaxe Abstrata (AST).
* **Escopo de Variáveis:** A tabela de símbolos é global. Não há distinção entre escopo local de função e escopo global.
* **Análise Semântica Avançada:** Não há verificação de compatibilidade de tipos em atribuições (ex: atribuir `float` para `int`).
* **Funções:** Não há suporte para parâmetros em funções ou para a instrução `return`.
