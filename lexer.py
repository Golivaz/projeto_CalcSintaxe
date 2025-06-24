"""
Professor Renato
Matéria : Teoria da computação e Compiladores

Guilherme de Oliveira Rodrigues RA: 105926 
Marcos Roberto Pinto Ribeiro Junior RA:109243
Leonardo Milani Pigatti RA:110542

"""
import ply.lex as lex

# Palavras reservadas da nossa linguagem
palavras_reservadas = {
   'if' : 'PALAVRA_CHAVE_IF',
   'else' : 'PALAVRA_CHAVE_ELSE',
   'while' : 'PALAVRA_CHAVE_WHILE',
   'print' : 'PALAVRA_CHAVE_PRINT',
   'int' : 'TIPO_DADO',
   'float' : 'TIPO_DADO',
   'char' : 'TIPO_DADO',
   'double' : 'TIPO_DADO',
}

# Tokens da linguagem
lista_tokens_base = [
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
]

# Lista final de tokens
tokens = lista_tokens_base + list(set(palavras_reservadas.values()))

# Regras dos tokens com expressoes regulares
t_OPERADOR_ARITMETICO = r"\+|\-|\*|\/"
t_OPERADOR_ATRIBUICAO = r"\="
t_OPERADOR_RELACIONAL = r"==|!=|<=|>=|>|<"
t_FIM_COMANDO = r"\;"
t_SEPARADOR = r"\,"
t_ABRE_PARENTESES = r"\("
t_FECHA_PARENTESES = r"\)"
t_ABRE_CHAVES = r"\{"
t_FECHA_CHAVES = r"\}"
t_CONSTANTE_INTEIRA = r"\d+"
t_CONSTANTE_FLUTUANTE = r"\d+\.\d+"

# Ignora espacos e tabs
t_ignore = " \t"

# Regra pra pegar identificadores e palavras-chave
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Ve se o valor encontrado eh uma palavra reservada
    t.type = palavras_reservadas.get(t.value, 'IDENTIFICADOR')
    return t

# Conta as linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignora comentario de linha
def t_COMMENT_LINE(t):
    r'//.*'
    pass

# Ignora comentario de bloco
def t_COMMENT_BLOCK(t):
    r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    t.lexer.lineno += t.value.count('\n')
    pass

# Ignora diretivas tipo #include
def t_PREPROCESSOR_DIRECTIVE(t):
    r'\#.*'
    pass

# Tratamento de erro lexico
def t_error(t):
    print(f"Erro lexico: Caractere zuado '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Funcao que cria e retorna o analisador lexico
def cria_lexer(nome_do_arquivo):
    with open(nome_do_arquivo, 'r') as arquivo:
        dados_do_arquivo = arquivo.read()
    
    lexer = lex.lex()
    lexer.input(dados_do_arquivo)
    return lexer