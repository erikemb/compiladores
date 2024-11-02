import ply.lex as lex

DEBUGLEX = True
BLOCO = False   # erro de implementação
TOKENSLEX = False


pilha_indentacao = [0]  # Definição de pilha de indentação
TAB_TAMANHO = 8  # Defina o tamanho da tabulação como 8 espaços


# Variável global para controlar o início de linha e a detecção do primeiro token
inicio_linha = True
primeiro_token_detectado = False

# Definição dos tokens
tokens = (
    'INT', 'FLOAT', 'BOOL', 'CHAR', 'STRING',  
    'PLUS', 'MINUS', 'MULT', 'DIV',            
    'EQUALS', 'LPAREN', 'RPAREN', 'DOIS_PONTOS_DUPLO', 'SETAS', 'COMENTARIO',  
    'ID', 'IF', 'CASE', 'LET', 'ELSE', 'THEN', 'WHERE',
    'MAIOR', 'MAIOR_IGUAL', 'IGUAL', 'DIFERENTE', 'MENOR_IGUAL', 'MENOR',      
    'AND', 'OR', 'NOT',                         
    'TABULACAO', 'NOVA_LINHA', 'ASPAS_SIMPLES', 'ASPAS_DUPLAS', 'BARRA', 'PIPE',
    'ABREBLOCO', 'FECHABLOCO', 
    'EXCLAMACAO', 'HASHTAG', 'DOLLAR', 'PERCENT', 'ECOMERCIAL', 
    'ESTRELA', 'PONTO',
    'INTERROGACAO', 'ARROBA', 'CIRCUNFLEXO', 'TIL', 'DOIS_PONTOS',
    'DEFAULT', 'OF', 'IN', 'BARRA_INVERTIDA', "PONTO_VIRGULA","LCOLCHETE","RCOLCHETE","CRASE","LCHAVE","RCHAVE",
    'SETAS_ESQUERDA', 'SETAS_DUPLO', 'TIPO',
    
    'NEWLINE',
    'VARSYM'
)

# Palavras reservadas
reservadas = {
    'let': 'LET',
    'else': 'ELSE',
    'then': 'THEN',
    'If': 'IF',
    'Case': 'CASE',
    'not': 'NOT',
    'of': 'OF',
    'Int': 'INT',
    'Char': 'CHAR',
    'String': 'STRING',
    'Float': 'FLOAT',
    'Bool': 'BOOL',
    'default': 'DEFAULT',
    'in': 'IN',
    'where': 'WHERE',
    'and' : 'AND',
    'or':'OR'
}

# tokens = ['LPAREN','RPAREN',...,'ID'] + list(reservadas.values())

# Função para lidar com indentação no início de linhas
def t_ESPACOS(t):
    r'[ \t]+'
    global inicio_linha, primeiro_token_detectado
    if BLOCO:
        if inicio_linha:  # Apenas no início da linha
            nivel_indentacao = 0
            for char in t.value:
                if char == '\t':
                    nivel_indentacao += TAB_TAMANHO
                else:
                    nivel_indentacao += 1

            if primeiro_token_detectado:
                if nivel_indentacao > pilha_indentacao[-1]:
                    pilha_indentacao.append(nivel_indentacao)
                    t.type = 'ABREBLOCO'
                    return t
                elif nivel_indentacao < pilha_indentacao[-1]:
                    pilha_indentacao.pop()
                    t.type = 'FECHABLOCO'
                    return t
            else:
                primeiro_token_detectado = True
        t.lexer.lineno += len(t.value.splitlines())
        inicio_linha = False  # Após processar a indentação, não estamos mais no início da linha



# Definição de tokens para identificadores e palavras-chave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Verifica se é uma palavra reservada
    return t


# Definição de tokens para comentários
def t_COMENTARIO(t):
    r'\-\-.*'
    if DEBUGLEX:
        print("Comentário:" + t.value)
    pass  # Ignora o resto da linha

# Definição de tokens para strings (entre aspas duplas)
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remove as aspas duplas
    return t




# Define uma regra para contar saltos de linha
def t_NEWLINE(t):
    r'\n+'
    
    t.lexer.lineno += len(t.value)
    global inicio_linha
    inicio_linha = True  # Sinaliza que estamos no início de uma nova linha
    # print()
    
    return t  # Retorna o token NEWLINE para ser processado
    
# Definição de tokens para números de ponto flutuante
def t_FLOAT(t):
    r'\d+\.\d+(?=[^\w]|$)'
    t.value = float(t.value)
    return t

# Definição de tokens para números inteiros
def t_INT(t):
    r'\d+(?=[^\w]|$)'
    t.value = int(t.value)
    return t

# Definição de tokens para char
def t_CHAR(t):
    r'\'\s*(?:\\.|[^\'\\])\s*\''
    t.value = t.value[1:-1]  # Remove as aspas simples
    return t



# Definição de tokens para operadores e símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOIS_PONTOS_DUPLO = r'::'
t_SETAS = r'->'
t_EXCLAMACAO = r'\!'     
t_HASHTAG = r'\#'           
t_DOLLAR = r'\$'         
t_PERCENT = r'%'         
t_ECOMERCIAL = r'\&'     
t_ESTRELA = r'\⋆'        
t_PONTO = r'\.'                    
t_INTERROGACAO = r'\?'   
t_ARROBA = r'\@'         
t_BARRA_INVERTIDA = r'\\'  
t_CIRCUNFLEXO = r'\^'    
t_TIL = r'\~'            
t_DOIS_PONTOS = r'\:'    
t_SETAS_ESQUERDA = r'<-'
t_SETAS_DUPLO = r'=>'
t_PONTO_VIRGULA = r';'
t_LCOLCHETE = r'\['
t_RCOLCHETE = r'\]'
t_CRASE = r'`'
t_LCHAVE = r'\{'
t_RCHAVE = r'\}'

# Definição de tokens para operadores de comparação
t_MAIOR = r'>'
t_MAIOR_IGUAL = r'>='
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MENOR_IGUAL = r'<='
t_MENOR = r'<'

# Definição de tokens para operadores lógicos
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'not'

# Definição de tokens para caracteres especiais
t_TABULACAO = r'\t'
t_NOVA_LINHA = r'\n'

t_ASPAS_SIMPLES = r'\''  # Correção de aspas simples
t_ASPAS_DUPLAS = r'\"'
t_BARRA = r'\\'
t_PIPE = r'\|'  # Definindo o token PIPE para o símbolo '|'

# Definição de VARSYM (symbol⟨:⟩ {symbol})⟨reservedop | dashes⟩
# t_VARSYM = r'[!#\$%&⋆\+\./<=>\?@\\\^\|\-~:]+(?:::|==|<=|>=|->|<-|=>|@|~|\\|\||:|=|--|\.\.)'


# ARRUMAR O VARSYN PQ TA ZOADO




# Função para tratar erros léxicos
def t_error(t):
    print(f"Erro léxico na linha {t.lineno}, caractere '{t.value[0]}'")
    t.lexer.skip(1)  # Pula o caractere desconhecido

def calcular_coluna(lexpos, codigo):
    ultima_nova_linha = codigo.rfind('\n', 0, lexpos)
    if ultima_nova_linha < 0:
        return lexpos + 1
    else:
        return lexpos - ultima_nova_linha

# Criar o analisador léxico
analisador = lex.lex()

# Leitura do código de um arquivo
arquivo = 'teste.hs'
with open(arquivo, 'r') as file:
    codigo_teste = file.read()

# Configurar o analisador
analisador.input(codigo_teste)

# Impressão dos tokens gerados
if (TOKENSLEX == True):
    for token in analisador:
        coluna = calcular_coluna(token.lexpos, codigo_teste)
        if (token.type == 'NEWLINE' ):
            token.value = 'FIM DE LINHA'
            print()

        print(f"Tipo: {token.type}, Valor: {token.value}, Linha: {token.lineno}, Posição: {coluna}")
