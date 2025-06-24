"""
Professor Renato
Matéria : Teoria da computação e Compiladores

Guilherme de Oliveira Rodrigues RA: 105926 
Marcos Roberto Pinto Ribeiro Junior RA:109243
Leonardo Milani Pigatti RA:110542

"""
import ply.yacc as yacc
from lexer import cria_lexer 
import sys

# Tokens que o parser vai usar
tokens = (
    "TIPO_DADO",
    "IDENTIFICADOR",
    "CONSTANTE_INTEIRA",
    "CONSTANTE_FLUTUANTE",
    "OPERADOR_ARITMETICO",
    "OPERADOR_ATRIBUICAO",
    "OPERADOR_RELACIONAL",
    "SEPARADOR",
    "FIM_COMANDO",
    "ABRE_PARENTESES",
    "FECHA_PARENTESES",
    "ABRE_CHAVES",
    "FECHA_CHAVES",
    "PALAVRA_CHAVE_IF",
    "PALAVRA_CHAVE_ELSE",
    "PALAVRA_CHAVE_WHILE",
    "PALAVRA_CHAVE_PRINT",
)

# Tabela de simbolos e funcoes de ajuda
tabela_simbolos = {}

def add_variavel_tabela(nome_var, tipo, linha):
    if nome_var in tabela_simbolos:
        print(f"Erro semantico({linha}): Variavel '{nome_var}' ja foi declarada antes.")
        sys.exit(1)
    else:
        tabela_simbolos[nome_var] = {"tipo": tipo, "valor": None}

def checa_variavel_declarada(nome_var, linha):
    if nome_var not in tabela_simbolos:
        print(f"Erro semantico({linha}): Variavel '{nome_var}' nao foi declarada.")
        sys.exit(1)
    return tabela_simbolos[nome_var]

# Define a precedencia dos operadores
precedence = (
    ('left', 'OPERADOR_RELACIONAL'),
    ('left', 'OPERADOR_ARITMETICO'),
    ('right', 'OPERADOR_ATRIBUICAO'),
)

# Regras da Gramatica

# Regra principal, comeco de tudo
def p_programa(t):
    '''programa : lista_declaracoes_globais_ou_funcoes'''
    print("\n--- Analise do Programa ---")
    if t[1]:
        for item in t[1]:
            print(f"-> {item}")
    print("--- Fim da Analise ---")
    t[0] = "Analise concluida com sucesso."

def p_lista_declaracoes_globais_ou_funcoes(t):
    '''lista_declaracoes_globais_ou_funcoes : declaracao_global_ou_funcao
                                            | lista_declaracoes_globais_ou_funcoes declaracao_global_ou_funcao
                                            |''' # Permite arquivo vazio
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[2]]

def p_declaracao_global_ou_funcao(t):
    '''declaracao_global_ou_funcao : declaracao
                                   | funcao_definicao'''
    t[0] = t[1]

def p_declaracao(t):
    '''declaracao : TIPO_DADO lista_identificadores FIM_COMANDO'''
    tipo = t[1]
    identificadores = t[2]
    lista_declaracoes_texto = []
    for nome_var in identificadores:
        add_variavel_tabela(nome_var, tipo, t.lineno(1))
        lista_declaracoes_texto.append(f"{tipo} {nome_var}")
    t[0] = f"Declaracao: {', '.join(lista_declaracoes_texto)};"

def p_lista_identificadores(t):
    '''lista_identificadores : IDENTIFICADOR
                             | lista_identificadores SEPARADOR IDENTIFICADOR'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

def p_funcao_definicao(t):
    '''funcao_definicao : TIPO_DADO IDENTIFICADOR ABRE_PARENTESES FECHA_PARENTESES bloco_de_codigo'''
    t[0] = f"Definicao da funcao: {t[1]} {t[2]}() {t[5]}"

def p_bloco_de_codigo(t):
    '''bloco_de_codigo : ABRE_CHAVES lista_comandos_e_declaracoes FECHA_CHAVES'''
    texto_do_bloco = "{\n"
    if t[2]:
        for item in t[2]:
            texto_do_bloco += f"    {item}\n"
    texto_do_bloco += "}"
    t[0] = texto_do_bloco

def p_lista_comandos_e_declaracoes(t):
    '''lista_comandos_e_declaracoes : comando_ou_declaracao
                                    | lista_comandos_e_declaracoes comando_ou_declaracao
                                    |''' # Permite blocos vazios
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[2]]

def p_comando_ou_declaracao(t):
    '''comando_ou_declaracao : declaracao
                             | comando'''
    t[0] = t[1]

def p_comando(t):
    '''comando : atribuicao_comando
               | if_comando
               | while_comando
               | print_comando'''
    t[0] = t[1]

def p_atribuicao_comando(t):
    '''atribuicao_comando : IDENTIFICADOR OPERADOR_ATRIBUICAO expressao FIM_COMANDO'''
    info_da_variavel = checa_variavel_declarada(t[1], t.lineno(1))
    tabela_simbolos[t[1]]["valor"] = t[3]
    t[0] = f"Atribuicao: {t[1]} = {t[3]};"

def p_if_comando(t):
    '''if_comando : PALAVRA_CHAVE_IF ABRE_PARENTESES expressao FECHA_PARENTESES bloco_de_codigo
                  | PALAVRA_CHAVE_IF ABRE_PARENTESES expressao FECHA_PARENTESES bloco_de_codigo PALAVRA_CHAVE_ELSE bloco_de_codigo'''
    if len(t) == 6:
        t[0] = f"IF ({t[3]}) {t[5]}"
    else:
        t[0] = f"IF ({t[3]}) {t[5]} ELSE {t[7]}"

def p_while_comando(t):
    '''while_comando : PALAVRA_CHAVE_WHILE ABRE_PARENTESES expressao FECHA_PARENTESES bloco_de_codigo'''
    t[0] = f"WHILE ({t[3]}) {t[5]}"

def p_print_comando(t):
    '''print_comando : PALAVRA_CHAVE_PRINT ABRE_PARENTESES expressao FECHA_PARENTESES FIM_COMANDO'''
    t[0] = f"PRINT({t[3]});"

# Regra para expressoes (junta tudo)
def p_expressao(t):
    '''
    expressao : expressao OPERADOR_ARITMETICO expressao
              | expressao OPERADOR_RELACIONAL expressao
              | ABRE_PARENTESES expressao FECHA_PARENTESES
              | CONSTANTE_INTEIRA
              | CONSTANTE_FLUTUANTE
              | IDENTIFICADOR
    '''
    if len(t) == 2:  # Valor simples
        if t.slice[1].type == 'IDENTIFICADOR':
            info_da_variavel = checa_variavel_declarada(t[1], t.lineno(1))
            t[0] = t[1] # Retorna o nome do identificador
        else:
            t[0] = t[1] # Retorna o valor da constante
    elif t[1] == '(':  # Parênteses
        t[0] = t[2]
    else:  # Operação
        t[0] = f"({t[1]} {t[2]} {t[3]})" # Retorna a representação da operação

# Funcao de erro e a que inicia o parser
def p_error(t):
    if t:
        print(f"Erro sintatico: Caractere inesperado '{t.value}' do tipo '{t.type}' na linha {t.lineno}.")
    else:
        print("Erro sintatico: Fim de arquivo inesperado.")
    sys.exit(1)

def rodar_parser(nome_arquivo_fonte):
    lexer = cria_lexer(nome_arquivo_fonte)
    parser = yacc.yacc(debug=False, write_tables=False)
    with open(nome_arquivo_fonte, 'r') as f:
        conteudo = f.read()
    print(f"--- Iniciando Analise Sintatica de '{nome_arquivo_fonte}' ---")
    try:
        resultado_analise = parser.parse(conteudo, lexer=lexer)
        print("\nAnalise Concluida.")
        print("\n--- Tabela de Simbolos Final ---")
        if tabela_simbolos:
            for nome, info in tabela_simbolos.items():
                print(f"  '{nome}': Tipo='{info['tipo']}', Valor='{info.get('valor', 'nao inicializado')}'")
        else:
            print("  Tabela de simbolos vazia.")
        print("---------------------------------")
        return resultado_analise
    except SystemExit:
        print("\nAnalise Abortada Devido a Erros Sintaticos ou Semanticos.")
        return None