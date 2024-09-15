import ply.lex as lex

# Definição dos tokens
tokens = (
    'INT', 'FLOAT', 'BOOL', 'CHAR', 'STRING',  # Tipos de dados
    'PLUS', 'MINUS', 'MULT', 'DIV',            # Operadores
    'EQUALS', 'LPAREN', 'RPAREN', 'DOIS_PONTOS_DUPLO', 'SETAS', 'COMENTARIO', # Operadores e símbolos
    'ID', 'IF', 'CASE', 'LET', 'ELSE', 'THEN',  # Identificadores e palavras-chave
    'MAIOR', 'MAIOR_IGUAL', 'IGUAL', 'DIFERENTE', 'MENOR_IGUAL', 'MENOR',     # Operadores de comparação
    'E', 'OU', 'NAO',                         # Operadores lógicos
    'TABULACAO', 'NOVA_LINHA', 'ASPAS_SIMPLES', 'ASPAS_DUPLAS', 'BARRA',  # Caracteres especiais
)

# Palavras reservadas
reservadas = {
    'let': 'LET',
    'else': 'ELSE',
    'then': 'THEN',
    'If': 'IF',
    'Case': 'CASE',
    'not' : 'NAO',
    'Int' : 'INT',
    'Char' : 'CHAR'
}

# Definição de tokens para comentários
def t_COMENTARIO(t):
    r'\-\-.*'
    pass  # Ignora o resto da linha

# Definição de tokens para números inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Definição de tokens para números de ponto flutuante
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Definição de tokens para operadores
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_EQUALS = r'='

# Definição de tokens para símbolos
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOIS_PONTOS_DUPLO = r'::'
t_SETAS = r'->'

# Definição de tokens para operadores de comparação
t_MAIOR = r'>'
t_MAIOR_IGUAL = r'>='
t_IGUAL = r'=='
t_DIFERENTE = r'/='
t_MENOR_IGUAL = r'<='
t_MENOR = r'<'

# Definição de tokens para operadores lógicos
t_E = r'\&\&'
t_OU = r'\|\|'
t_NAO = r'not'

# Definição de tokens para caracteres especiais
t_TABULACAO = r'\t'
t_NOVA_LINHA = r'\n'
t_ASPAS_SIMPLES = r'\''
t_ASPAS_DUPLAS = r'\"'
t_BARRA = r'\\'

# Definição de tokens para identificadores e palavras-chave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t

# Ignora espaços e tabulações
t_ignore = ' \t'

# Função para tratar erros léxicos
def t_error(t):
    print(f"Erro léxico na linha {t.lineno}, caractere '{t.value[0]}'")
    t.lexer.skip(1)  # Pula o caractere desconhecido

# Criar o analisador léxico
analisador = lex.lex()

# Leitura do código de um arquivo
arquivo = 'teste.hs'
with open(arquivo, 'r') as file:
    codigo_teste = file.read()

# Processar o código lido
analisador.input(codigo_teste)

# Impressão dos tokens gerados
for token in analisador:
    print(f"Tipo: {token.type}, Valor: {token.value}, Linha: {token.lineno}, Posição: {token.lexpos}")
