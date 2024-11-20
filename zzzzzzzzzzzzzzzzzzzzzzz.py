import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regras de expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Regra para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Definição da gramática e construção da AST
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('-', p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('*', p[1], p[3])

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = ('num', p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Tratamento de erros
def p_error(p):
    print("Erro de sintaxe!")

# Construção do parser
parser = yacc.yacc()

def print_ast(node, level=0):
    if isinstance(node, tuple):
        print('  ' * level + str(node[0]))
        for child in node[1:]:
            print_ast(child, level + 1)
    else:
        print('  ' * level + str(node))

# Exemplo de uso com a AST gerada anteriormente
result = parser.parse("3 + 4 * (2 - 1)")
print_ast(result)
