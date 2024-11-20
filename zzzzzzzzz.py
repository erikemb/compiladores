import ply.yacc as yacc
from LEXHaskell import tokens  # Importar os tokens do analisador léxico

variaveis = {}
body = []  # Renomeado de express para body

class Node:
    def __init__(self, tipo, valor=None, filhos=None):
        self.tipo = tipo
        self.valor = valor
        self.filhos = filhos or []

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.tipo) + " : " + repr(self.valor) + "\n"
        for child in self.filhos:
            ret += child.__repr__(level + 1)
        return ret

    def avaliar(self):
        # if self.tipo == 'Variavel':
        #     return variaveis.get(self.valor, 0)
        if self.tipo == 'numero':
            return self.valor
        elif self.tipo == 'Operacao':
            left = self.filhos[0].avaliar()
            right = self.filhos[1].avaliar()
            if self.valor == '+':
                return left + right
            elif self.valor == '-':
                return left - right
            elif self.valor == '*':
                return left * right
            elif self.valor == '/':
                return left / right
        # Adicione outras operações conforme necessário

# Definição das regras de produção
def p_expressao_binaria(p):
    '''expressao : expressao PLUS termo
                 | expressao MINUS termo'''
    p[0] = Node(tipo='Operacao', valor=p[2], filhos=[p[1], p[3]])

def p_expressao_termo(p):
    '''expressao : termo NEWLINE'''
    # Armazena a AST na lista body e reseta
    body.append(p[1])  # Adiciona a árvore à lista body
    p[0] = None  # Limpa a árvore atual

def p_termo_binario(p):
    '''termo : termo MULT fator
             | termo DIV fator'''
    p[0] = Node(tipo='Operacao', valor=p[2], filhos=[p[1], p[3]])

def p_termo_fator(p):
    '''termo : fator'''
    p[0] = p[1]

def p_fator_id(p):
    '''fator : INT
             | FLOAT
             | STRING
             | BOOL
             | CHAR
             '''
    p[0] = Node(tipo='numero', valor=p[1])

def p_fator_parenteses(p):
    '''fator : LPAREN expressao RPAREN'''
    p[0] = p[2]

def p_fator_chaves(p):
    '''fator : LCHAVE expressao RCHAVE'''
    p[0] = p[2]

def p_expressao_booleana_binaria(p):
    '''expressao : expressao AND termo
                 | expressao OR termo'''
    p[0] = Node(tipo='OperacaoBooleana', valor=p[2], filhos=[p[1], p[3]])

def p_termo_booleana_unario(p):
    '''termo : NOT fator'''
    p[0] = Node(tipo='OperacaoUnaria', valor='NOT', filhos=[p[2]])

def p_expressao_relacional(p):
    '''expressao : expressao IGUAL termo
                 | expressao DIFERENTE termo
                 | expressao MENOR termo
                 | expressao MAIOR termo
                 | expressao MENOR_IGUAL termo
                 | expressao MAIOR_IGUAL termo'''
    p[0] = Node(tipo='OperacaoRelacional', valor=p[2], filhos=[p[1], p[3]])

def p_declaracao_valor(p):
    '''
    declaracao_valor : ID IGUAL valor
    '''
    variavel = p[1]
    valor = p[3]
    p[0] = ('declaracao_valor', variavel, valor)

def p_declaracao_tipo(p):
    '''
    declaracao_tipo : ID DOIS_PONTOS_DUPLO TIPO
    '''
    variavel = p[1]
    tipo = p[3]
    p[0] = ('declaracao_tipo', variavel, tipo)

def p_tipo(p):
    '''
    valor : INT
          | FLOAT
          | STRING
          | BOOL
          | CHAR
    '''
    p[0] = p[1]

# Erros
erros = 0
def p_error(p):
    global erros
    if p:
        erros += 1  
        print(f"Erro de sintaxe no token {p.type} na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

# Definir regra para nova linha
def p_newline(p):
    '''expressao : NEWLINE'''
    p[0] = None  # Apenas para limpar a árvore, se necessário

# Construa o analisador sintático
parser = yacc.yacc()

# Leitura do código de um arquivo
arquivo = 'teste.hs'
with open(arquivo, 'r') as file:
    codigo_teste = file.read()

# Analisa o código e gera a AST
parser.parse(codigo_teste)

# Exibe a AST gerada
print("Árvore de Sintaxe Abstrata (AST):")
for ast in body:
    print(ast)

# Exibir a quantidade de erros
print("Quantidade de erros encontrada:", erros)
