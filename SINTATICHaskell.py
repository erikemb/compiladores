import ply.yacc as yacc
from LEXHaskell import tokens  # Importar os tokens do analisador léxico


################################################################################3

# Definição das regras de produção
def p_expressao_binaria(p):
    '''expressao : expressao PLUS termo
                 | expressao MINUS termo'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expressao_termo(p):
    '''expressao : termo'''
    p[0] = p[1]

def p_termo_binario(p):
    '''termo : termo MULT fator
             | termo DIV fator'''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_termo_fator(p):
    '''termo : fator'''
    p[0] = p[1]

def p_fator_numero(p):
    '''fator : INT'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Erro de sintaxe no token {p.type} na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")



def p_fator_parenteses(p):
    '''fator : '(' expressao ')' '''
    p[0] = p[2]  # Retorna o valor da expressão dentro dos parênteses

# Definição das regras de produção para expressões booleanas BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

def p_expressao_booleana_binaria(p):
    '''expressao : expressao AND termo
                 | expressao OR termo'''
    # Trata expressões booleanas com operadores AND e OR
    # Se o operador for 'AND', realiza a operação lógica AND entre os dois operandos
    if p[2] == 'AND':
        p[0] = p[1] and p[3]
    # Se o operador for 'OR', realiza a operação lógica OR
    elif p[2] == 'OR':
        p[0] = p[1] or p[3]

def p_termo_booleana_unario(p):
    '''termo : NOT fator'''
    p[0] = not p[2]


##################################

# Construa o analisador sintático
parser = yacc.yacc()

# Leitura do código de um arquivo
arquivo = 'teste.hs'
with open(arquivo, 'r') as file:
    codigo_teste = file.read()

# Teste de exemplo
entrada = codigo_teste
resultado = parser.parse(entrada)
print("Resultado:", resultado)
