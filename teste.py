import ply.lex as lex

# Lista de tokens
tokens = (
    'NEWLINE',
    'TEXT',
)

# Definindo as expressões regulares para os tokens
t_NEWLINE = r'\n+'
t_TEXT = r'[^\n]+'

# Ignorar espaços em branco
t_ignore = ' \t'

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construindo o lexer
lexer = lex.lex()

# Testando o lexer
data = """Hello World
This is a test
Another line here
"""

lexer.input(data)

for tok in lexer:
    print(tok)
