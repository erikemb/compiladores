import ply.yacc as yacc
from LEXHaskell import tokens  # Importar os tokens do analisador léxico

variaveis = {}

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
    # Verifica o tipo do nó e realiza a operação correspondente
        if self.tipo == 'Numero':
            return self.valor
        # elif self.tipo == 'Bool':
        #     return self.valor  # Retorna o valor booleano diretamente
        elif self.tipo == 'Variavel':
            return variaveis.get(self.valor, 0)
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
        elif self.tipo == 'OperacaoBooleana':
            left = self.filhos[0].avaliar()
            right = self.filhos[1].avaliar()
            if self.valor == 'and':
                return left and right
            elif self.valor == 'or':
                return left or right
        elif self.tipo == 'OperacaoUnaria':
            return not self.filhos[0].avaliar()
        elif self.tipo == 'OperacaoRelacional':
            left = self.filhos[0].avaliar()
            right = self.filhos[1].avaliar()
            if self.valor == '==':
                return left == right
            elif self.valor == '!=':
                return left != right
            elif self.valor == '<':
                return left < right
            elif self.valor == '>':
                return left > right
            elif self.valor == '<=':
                return left <= right
            elif self.valor == '>=':
                return left >= right

        

################################################################################3

# Definição das regras de produção

# Regras da gramática
def p_expressao_binaria(p):
    '''expressao : expressao PLUS termo
                 | expressao MINUS termo'''
    p[0] = Node(tipo='Operacao', valor=p[2], filhos=[p[1], p[3]])

def p_expressao_termo(p):
    '''expressao : termo'''
    p[0] = p[1]

def p_termo_binario(p):
    '''termo : termo MULT fator
             | termo DIV fator'''
    p[0] = Node(tipo='Operacao', valor=p[2], filhos=[p[1], p[3]])

def p_termo_fator(p):
    '''termo : fator'''
    p[0] = p[1]

def p_fator_numero(p):
    '''fator : INT
             | FLOAT'''
    p[0] = Node(tipo='Numero', valor=p[1])


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

# def p_fator_booleano(p):
#     '''fator : TRUE
#              | FALSE'''
#     # Converta `TRUE` e `FALSE` para valores booleanos em Python
#     valor = True if p[1] == 'True' else False
#     p[0] = Node(tipo='Booleano', valor=valor)







def p_error(p):
    if p:
        print(f"Erro de sintaxe no token {p.type} na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")


##################################



##################################

# Construa o analisador sintático
parser = yacc.yacc()

# Leitura do código de um arquivo
arquivo = 'teste.hs'
with open(arquivo, 'r') as file:
    codigo_teste = file.read()

# # Teste de exemplo
# entrada = codigo_teste
# resultado = parser.parse(entrada)
# print("Resultado:", resultado)


# Leitura do código de um arquivo
arquivo = 'teste.hs'
with open(arquivo, 'r') as file:
    codigo_teste = file.read()

# Analisa o código e gera a AST
ast = parser.parse(codigo_teste)

# Exibe a AST gerada
print("Árvore de Sintaxe Abstrata (AST):")
print(ast)

# Avalia a expressão
resultado = ast.avaliar()
print("Resultado da Expressão:", resultado)