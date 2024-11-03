import ply.yacc as yacc
from LEXHaskell import tokens  # Importar os tokens do analisador léxico

variaveis = {}
body = []

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
        # if self.tipo == 'numero':
        #     return self.valor
        
        
        
        
        if self.tipo == 'Operacao':
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
            elif self.valor == '^':
                return left ^ right
        elif self.tipo == 'OperacaoBooleana':
            left = self.filhos[0].avaliar()
            right = self.filhos[1].avaliar()
            if self.valor == 'and':
                return left and right
            elif self.valor == 'or':
                return left or right
            elif self.valor == 'DIFERENTE':
                return left != right
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

# Definição das regras de gramar haskell

def p_body(p):
    '''body ::= topdecls NEWLINE'''
    # Armazena a AST na lista body e reseta
    body.append(p[1])  # Adiciona a árvore à lista body
    p[0] = None  # Limpa a árvore atual


def p_topdecls(p):
    '''topdecls ::= topdecl PONTO_VIRGULA topdecls
                  | topdecl'''
    if len(p) == 4:  # topdecl PONTO_VIRGULA topdecls
        p[0] = Node(tipo='topdecls', valor=[p[1], p[3]])  # Armazena uma lista de declarações
    else:  # Apenas uma topdecl
        p[0] = Node(tipo='topdecls', valor=[p[1]])

def p_decls(p):
    '''decls ::= LCHAVE decls RCHAVE
                | decl PONTO_VIRGULA decls
                | decl decls
                | empty'''
    if len(p) == 4:  # LCHAVE decls RCHAVE
        p[0] = Node(tipo='decls', valor=p[2])
    elif len(p) == 3:  # decl PONTO_VIRGULA decls
        p[0] = Node(tipo='decls', valor=[p[1], p[3]])
    elif len(p) == 2:  # decl decls
        p[0] = Node(tipo='decls', valor=[p[1]] + p[2].valor)  # Concatena decls
    else:  # RCHAVE
        p[0] = Node(tipo='decls', valor=[])

def p_declslist(p):
    '''declslist ::= decl PONTO_VIRGULA declslist
                   | decl'''
    if len(p) == 4:  # decl PONTO_VIRGULA declslist
        p[0] = Node(tipo='declslist', valor=[p[1]] + p[3].valor)
    else:  # decl
        p[0] = Node(tipo='declslist', valor=[p[1]])

def p_decl(p):
    '''decl ::= gendecl
               | funlhs rhs
               | pat rhs'''
    p[0] = Node(tipo='decl', valor=p[1])

def p_gendecl(p):
    '''gendecl ::= vars DOIS_PONTOS_DUPLO type'''
    p[0] = Node(tipo='gendecl', valor=p[1])

def p_vars(p):
    '''vars ::= var
               | var VIRGULA vars'''
    if len(p) == 2:  # var
        p[0] = Node(tipo='vars', valor=[p[1]])
    else:  # var VIRGULA vars
        p[0] = Node(tipo='vars', valor=[p[1]] + p[3].valor)

def p_type(p):
    '''type ::= btype
               | btype SETAS type'''
    if len(p) == 2:  # btype
        p[0] = Node(tipo='type', valor=p[1])
    else:  # btype SETAS type
        p[0] = Node(tipo='type', valor=(p[1], p[3]))

def p_btype(p):
    '''btype ::= btype atype
               | atype'''
    if len(p) == 3:  # btype atype
        p[0] = Node(tipo='btype', valor=(p[1], p[2]))
    else:  # atype
        p[0] = Node(tipo='btype', valor=p[1])

def p_atype(p):
    '''atype ::= INT
               | FLOAT
               | BOOL
               | CHAR
               | STRING
               | LPAREN type RPAREN
               | LPAREN typetuple RPAREN
               | LCOLCHETE type RCOLCHETE'''
    p[0] = Node(tipo='atype', valor=p[1])

def p_typetuple(p):
    '''typetuple ::= type VIRGULA typetuple
                   | type'''
    if len(p) == 4:  # type VIRGULA typetuple
        p[0] = Node(tipo='typetuple', valor=[p[1]] + p[3].valor)
    else:  # type
        p[0] = Node(tipo='typetuple', valor=[p[1]])

def p_funlhs(p):
    '''funlhs ::= var apatlist
                | patop
                | LPAREN funlhs RPAREN apatlist'''
    p[0] = Node(tipo='funlhs', valor=p[1])

def p_apatlist(p):
    '''apatlist ::= apat apatlist
                  | apat'''
    if len(p) == 3:  # apat apatlist
        p[0] = Node(tipo='apatlist', valor=[p[1]] + p[2].valor)
    else:  # apat
        p[0] = Node(tipo='apatlist', valor=[p[1]])

def p_apat(p):
    '''apat ::= var
              | var ARROBA apat 
              | qcon LCHAVE fpatlist RCHAVE    
              | INT
              | FLOAT
              | CHAR
              | STRING
              | TRUE
              | FALSE
              | gcon
              | UNDERLINE	    
              | LPAREN pat RPAREN
              | LPAREN pattuple RPAREN 
              | LCOLCHETE patlist RCOLCHETE'''
    p[0] = Node(tipo='apat', valor=p[1])

def p_fpatlist(p):
    '''fpatlist ::= fpat VIRGULA fpatlist
                  | fpat'''
    if len(p) == 4:  # fpat VIRGULA fpatlist
        p[0] = Node(tipo='fpatlist', valor=[p[1]] + p[3].valor)
    else:  # fpat
        p[0] = Node(tipo='fpatlist', valor=[p[1]])

def p_fpat(p):
    '''fpat ::= var EQUAL pat '''
    p[0] = Node(tipo='fpat', valor=(p[1], p[3]))

def p_patlist(p):
    '''patlist ::= pat VIRGULA patlist
                 | pat'''
    if len(p) == 4:  # pat VIRGULA patlist
        p[0] = Node(tipo='patlist', valor=[p[1]] + p[3].valor)
    else:  # pat
        p[0] = Node(tipo='patlist', valor=[p[1]])

def p_pattuple(p):
    '''pattuple ::= pat VIRGULA pattuple
                  | pat VIRGULA pat'''
    if len(p) == 4:  # pat VIRGULA pattuple
        p[0] = Node(tipo='pattuple', valor=[p[1]] + p[3].valor)
    else:  # pat VIRGULA pat
        p[0] = Node(tipo='pattuple', valor=[p[1], p[3]])

def p_patop(p):
    '''patop ::= pat varop pat
               | pat PLUS pat
               | pat MINUS pat
               | pat MULT pat
               | pat BARRA pat
               | pat CIRCUNFLEXO pat
               | pat MAIOR_IGUAL pat
               | pat MENOR_IGUAL pat
               | pat MAIOR pat
               | pat MENOR pat
               | pat IGUAL pat
               | pat DIFERENTE pat
               | pat OR pat
               | pat NOT pat
               | pat AND pat'''
    p[0] = Node(tipo='patop', valor=[p[1], p[2], p[3]])

def p_pat(p):
    '''pat ::= lpat DOIS_PONTOS pat
             | lpat'''
    if len(p) == 4:  # lpat DOIS_PONTOS pat
        p[0] = Node(tipo='pat', valor=(p[1], p[3]))
    else:  # lpat
        p[0] = Node(tipo='pat', valor=p[1])

def p_lpat(p):
    '''lpat ::= apat
               | MINUS lpattype
               | gcon apatlist'''
    if len(p) == 2:  # apat
        p[0] = Node(tipo='lpat', valor=p[1])
    elif len(p) == 3:  # MINUS lpattype
        p[0] = Node(tipo='lpat', valor=('UMINUS', p[2]))  # Representa o unário
    else:  # gcon apatlist
        p[0] = Node(tipo='lpat', valor=(p[1], p[2]))

def p_lpattype(p):
    '''lpattype ::= INT
                  | FLOAT'''
    p[0] = Node(tipo='lpattype', valor=p[1])  # Armazena o tipo

def p_rhs(p):
    '''rhs ::= EQUAL exp WHERE decls
              | gdrhs WHERE decls'''
    if len(p) == 5:  # EQUAL exp WHERE decls
        p[0] = Node(tipo='rhs', valor=(p[1], p[2], p[4]))  # Armazena o EQUAL, exp e decls
    else:  # gdrhs WHERE decls
        p[0] = Node(tipo='rhs', valor=(p[1], p[3]))  # Armazena gdrhs e decls

def p_gdrhs(p):
    '''gdrhs ::= guards EQUAL exp
               | guards EQUAL exp gdrhs'''
    if len(p) == 4:  # guards EQUAL exp
        p[0] = Node(tipo='gdrhs', valor=(p[1], p[2], p[3]))  # Armazena guards, EQUAL e exp
    else:  # guards EQUAL exp gdrhs
        p[0] = Node(tipo='gdrhs', valor=(p[1], p[2], p[3], p[4]))  # Armazena todos os elementos

def p_guards(p):
    '''guards ::= PIPE guardslist'''
    p[0] = Node(tipo='guards', valor=p[2])  # Armazena a lista de guards

def p_guardslist(p):
    '''guardslist ::= guard VIRGULA guardslist
                    | guard'''
    if len(p) == 4:  # guard VIRGULA guardslist
        p[0] = Node(tipo='guardslist', valor=[p[1]] + p[3].valor)  # Concatena guard e guardslist
    else:  # guard
        p[0] = Node(tipo='guardslist', valor=[p[1]])

def p_guard(p):
    '''guard ::= pat SETAS infixexp
                | LET decls
                | infixexp'''
    if len(p) == 4:  # pat SETAS infixexp
        p[0] = Node(tipo='guard', valor=(p[1], p[2], p[3]))  # Armazena o padrão, SETAS e a expressão
    elif len(p) == 3:  # LET decls
        p[0] = Node(tipo='guard', valor=(p[1], p[2]))  # Armazena LET e decls
    else:  # infixexp
        p[0] = Node(tipo='guard', valor=p[1])  # Armazena a expressão

def p_aexp(p):
    '''aexp ::= var
               | INT
               | FLOAT
               | CHAR
               | STRING
               | TRUE
               | FALSE
               | LPAREN exptuple RPAREN
               | LCOLCHETE explist RCOLCHETE
               | LPAREN exp RPAREN   
               | LCOLCHETE exp PIPE quallist RCOLCHETE
               | LPAREN infixexp qop RPAREN
               | LPAREN qop infixexp RPAREN'''
    p[0] = Node(tipo='aexp', valor=p[1])  # Armazena a expressão

def p_exptuple(p):
    '''exptuple ::= exp VIRGULA exptuple
                  | exp VIRGULA exp'''
    if len(p) == 4:  # exp VIRGULA exptuple
        p[0] = Node(tipo='exptuple', valor=[p[1]] + p[3].valor)  # Concatena exp e exptuple
    else:  # exp VIRGULA exp
        p[0] = Node(tipo='exptuple', valor=[p[1], p[3]])  # Armazena as duas expressões

def p_explist(p):
    '''explist ::= exp VIRGULA explist
                 | exp'''
    if len(p) == 4:  # exp VIRGULA explist
        p[0] = Node(tipo='explist', valor=[p[1]] + p[3].valor)  # Concatena exp e explist
    else:  # exp
        p[0] = Node(tipo='explist', valor=[p[1]])

def p_exp(p):
    '''exp ::= infixexp DOISPONTOSDUPLO type
              | infixexp'''
    if len(p) == 4:  # infixexp DOISPONTOSDUPLO type
        p[0] = Node(tipo='exp', valor=(p[1], p[2], p[3]))  # Armazena a infixexp e o tipo
    else:  # infixexp
        p[0] = Node(tipo='exp', valor=p[1])  # Armazena apenas a infixexp

def p_infixexp(p):
    '''infixexp ::= expop
                  | MINUS infixexp
                  | lexp'''
    if len(p) == 2:  # expop
        p[0] = Node(tipo='infixexp', valor=p[1])
    elif len(p) == 3:  # MINUS infixexp
        p[0] = Node(tipo='infixexp', valor=('UMINUS', p[2]))  # Representa a operação unária
    else:  # lexp
        p[0] = Node(tipo='infixexp', valor=p[1])

def p_expop(p):
    '''expop ::= infixexp varop infixexp
               | infixexp PLUS infixexp
               | infixexp MINUS infixexp
               | infixexp MULT infixexp
               | infixexp DIV infixexp
               | infixexp CIRCUNFLEXO infixexp
               | infixexp MAIOR_IGUAL infixexp
               | infixexp MENOR_IGUAL infixexp
               | infixexp MAIOR infixexp
               | infixexp MENOR infixexp
               | infixexp IGUAL infixexp
               | infixexp DIFERENTE infixexp
               | infixexp OR infixexp
               | infixexp NOT infixexp
               | infixexp AND infixexp'''
    # Aqui, podemos considerar que estamos criando um nó para cada operação
    p[0] = Node(tipo='expop', valor=(p[1], p[2], p[3]))  # Armazena a operação

def p_lexp(p):
    '''lexp ::= BARRA_INVERTIDA apatlist SETAS exp
              | LET decls IN exp
              | IF exp THEN exp ELSE exp
              | CASE exp OF LCHAVE alts RCHAVE
              | fexp'''
    if len(p) == 5:  # BARRA_INVERTIDA apatlist SETAS exp
        p[0] = Node(tipo='lexp', valor=(p[1], p[2], p[3], p[4]))  # Armazena todos os componentes
    elif len(p) == 6:  # LET decls IN exp
        p[0] = Node(tipo='lexp', valor=(p[1], p[2], p[3]))  # Armazena LET, decls e exp
    elif len(p) == 7:  # IF exp THEN exp ELSE exp
        p[0] = Node(tipo='lexp', valor=(p[1], p[2], p[3], p[4]))  # Armazena IF, exp, THEN e ELSE
    elif len(p) == 6:  # CASE exp OF LCHAVE alts RCHAVE
        p[0] = Node(tipo='lexp', valor=(p[1], p[2], p[3], p[4]))  # Armazena CASE, exp e alts
    else:  # fexp
        p[0] = Node(tipo='lexp', valor=p[1])  # Armazena o fexp

def p_fexp(p):
    '''fexp ::= aexp aexp
               | aexp fexp'''
    if len(p) == 3:  # aexp aexp
        p[0] = Node(tipo='fexp', valor=(p[1], p[2]))  # Armazena aexp e aexp
    else:  # aexp fexp
        p[0] = Node(tipo='fexp', valor=(p[1], p[2]))  # Armazena aexp e fexp

def p_quallist(p):
    '''quallist ::= qual VIRGULA quallist
                  | qual'''
    if len(p) == 4:  # qual VIRGULA quallist
        p[0] = Node(tipo='quallist', valor=[p[1]] + p[3].valor)  # Concatena qual e quallist
    else:  # qual
        p[0] = Node(tipo='quallist', valor=[p[1]])

def p_qual(p):
    '''qual ::= pat SETAS exp
               | LET decls
               | exp'''
    if len(p) == 4:  # pat SETAS exp
        p[0] = Node(tipo='qual', valor=(p[1], p[2], p[3]))  # Armazena pat, SETAS e exp
    elif len(p) == 3:  # LET decls
        p[0] = Node(tipo='qual', valor=(p[1], p[2]))  # Armazena LET e decls
    else:  # exp
        p[0] = Node(tipo='qual', valor=p[1])  # Armazena a expressão

def p_alts(p):
    '''alts ::= alt PONTO_VIRGULA alts
               | alt'''
    if len(p) == 4:  # alt PONTO_VIRGULA alts
        p[0] = Node(tipo='alts', valor=[p[1]] + p[3].valor)  # Concatena alt e alts
    else:  # alt
        p[0] = Node(tipo='alts', valor=[p[1]])

def p_alt(p):
    '''alt ::= pat SETAS exp optionwhere
              | pat gdpat optionwhere'''
    if len(p) == 5:  # pat SETAS exp optionwhere
        p[0] = Node(tipo='alt', valor=(p[1], p[2], p[3], p[4]))  # Armazena todos os componentes
    else:  # pat gdpat optionwhere
        p[0] = Node(tipo='alt', valor=(p[1], p[2], p[3]))  # Armazena pat, gdpat e optionwhere

def p_optionwhere(p):
    '''optionwhere ::= WHERE decls
                     | '''
    if len(p) == 3:  # WHERE decls
        p[0] = Node(tipo='optionwhere', valor=p[2])  # Armazena decls
    else:  # vazio
        p[0] = Node(tipo='optionwhere', valor=None)  # Representa a ausência de onde

def p_gdpat(p):
    '''gdpat ::= guards SETAS exp
               | guards SETAS exp gdpat'''
    if len(p) == 4:  # guards SETAS exp
        p[0] = Node(tipo='gdpat', valor=(p[1], p[2], p[3]))  # Armazena todos os componentes
    else:  # guards SETAS exp gdpat
        p[0] = Node(tipo='gdpat', valor=(p[1], p[2], p[3], p[4]))  # Armazena todos os elementos

def p_gcon(p):
    '''gcon ::= LPAREN RPAREN
               | LCOLCHETE RCOLCHETE
               | LPAREN virgulalist RPAREN
               | qcon'''
    if len(p) == 3:  # LPAREN RPAREN ou LCOLCHETE RCOLCHETE
        p[0] = Node(tipo='gcon', valor=p[1])  # Armazena o tipo vazio
    elif len(p) == 4:  # LPAREN virgulalist RPAREN
        p[0] = Node(tipo='gcon', valor=(p[1], p[2], p[3]))  # Armazena os elementos
    else:  # qcon
        p[0] = Node(tipo='gcon', valor=p[1])  # Armazena qcon

def p_virgulalist(p):
    '''virgulalist ::= VIRGULA virgulalist
                    | VIRGULA'''
    if len(p) == 3:  # VIRGULA virgulalist
        p[0] = Node(tipo='virgulalist', valor=[p[1]] + p[2].valor)  # Concatena a lista
    else:  # apenas VIRGULA
        p[0] = Node(tipo='virgulalist', valor=[p[1]])  # Armazena uma única vírgula

def p_var(p):
    '''var ::= VARID
              | LPAREN varsym RPAREN'''
    if len(p) == 2:  # VARID
        p[0] = Node(tipo='var', valor=p[1])  # Armazena o identificador
    else:  # LPAREN varsym RPAREN
        p[0] = Node(tipo='var', valor=p[2])  # Armazena o símbolo

def p_qcon(p):
    '''qcon ::= LPAREN DOISPONTOS RPAREN'''
    p[0] = Node(tipo='qcon', valor=(p[1], p[2], p[3]))  # Armazena os componentes

def p_varop(p):
    '''varop ::= VARSYM
                | CRASE VARID CRASE'''
    if len(p) == 2:  # VARSYM
        p[0] = Node(tipo='varop', valor=p[1])  # Armazena o símbolo
    else:  # CRASE VARID CRASE
        p[0] = Node(tipo='varop', valor=p[2])  # Armazena o identificador

def p_qvarop(p):
    '''qvarop ::= VARSYM
                 | CRASE VARID CRASE'''
    if len(p) == 2:  # VARSYM
        p[0] = Node(tipo='qvarop', valor=p[1])  # Armazena o símbolo
    else:  # CRASE VARID CRASE
        p[0] = Node(tipo='qvarop', valor=p[2])  # Armazena o identificador

def p_qop(p):
    '''qop ::= qvarop
              | DOISPONTOS'''
    if len(p) == 2:  # qvarop
        p[0] = Node(tipo='qop', valor=p[1])  # Armazena o qvarop
    else:  # DOISPONTOS
        p[0] = Node(tipo='qop', valor=p[1])  # Armazena os dois pontos




# # Regras da gramática
# def p_expressao_binaria(p):
#     '''expressao : expressao PLUS termo
#                  | expressao MINUS termo'''
#     p[0] = Node(tipo='Operacao', valor=p[2], filhos=[p[1], p[3]])

# def p_expressao_termo(p):
#     '''expressao : termo'''
#     p[0] = p[1]

# def p_termo_binario(p):
#     '''termo : termo MULT fator
#              | termo DIV fator'''
#     p[0] = Node(tipo='Operacao', valor=p[2], filhos=[p[1], p[3]])

# def p_termo_fator(p):
#     '''termo : fator'''
#     p[0] = p[1]

# def p_fator_id(p):
#     '''fator : INT
#              | FLOAT
#              | STRING
#              | BOOL
#              | CHAR
#              '''
#     p[0] = Node(tipo='numero', valor=p[1])


# def p_fator_parenteses(p):
#     '''fator : LPAREN expressao RPAREN'''
#     p[0] = p[2]

# def p_fator_chaves(p):
#     '''fator : LCHAVE expressao RCHAVE'''
#     p[0] = p[2]

# def p_expressao_booleana_binaria(p):
#     '''expressao : expressao AND termo
#                  | expressao OR termo'''
#     p[0] = Node(tipo='OperacaoBooleana', valor=p[2], filhos=[p[1], p[3]])

# def p_termo_booleana_unario(p):
#     '''termo : NOT fator'''
#     p[0] = Node(tipo='OperacaoUnaria', valor='NOT', filhos=[p[2]])

# def p_expressao_relacional(p):
#     '''expressao : expressao IGUAL termo
#                  | expressao DIFERENTE termo
#                  | expressao MENOR termo
#                  | expressao MAIOR termo
#                  | expressao MENOR_IGUAL termo
#                  | expressao MAIOR_IGUAL termo'''
#     p[0] = Node(tipo='OperacaoRelacional', valor=p[2], filhos=[p[1], p[3]])

# # def p_fator_booleano(p):
# #     '''fator : TRUE
# #              | FALSE'''
# #     # Converta `TRUE` e `FALSE` para valores booleanos em Python
# #     valor = True if p[1] == 'True' else False
# #     p[0] = Node(tipo='Booleano', valor=valor)

# def p_declaracao_valor(p):
#     '''
#     declaracao_valor : ID IGUAL valor
#     '''
#     variavel = p[1]
#     valor = p[3]
#     p[0] = ('declaracao_valor', variavel, valor)

# def p_declaracao_tipo(p):
#     '''
#     declaracao_tipo : ID DOIS_PONTOS_DUPLO TIPO
#     '''
#     variavel = p[1]
#     tipo = p[3]
#     p[0] = ('declaracao_tipo', variavel, tipo)



# def p_tipo(p):
#     '''
#     valor : INT
#           | FLOAT
#           | STRING
#           | BOOL
#           | CHAR
#     '''
#     p[0] = p[1]

erros = 0
errossintaticos = []
def p_error(p):
    if p:
        # erros += 1  
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
print("quantidade de erros encontrada é :", erros)