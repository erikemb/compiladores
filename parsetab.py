
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABREBLOCO AND ARROBA ASPAS_DUPLAS ASPAS_SIMPLES BARRA BARRA_INVERTIDA BOOL CASE CHAR CIRCUNFLEXO COMENTARIO CRASE DEFAULT DIFERENTE DIV DOIS_PONTOS DOIS_PONTOS_DUPLO DOLLAR ECOMERCIAL ELSE EQUALS ESTRELA EXCLAMACAO FECHABLOCO FLOAT HASHTAG ID IF IGUAL IN INT INTERROGACAO LCHAVE LCOLCHETE LET LPAREN MAIOR MAIOR_IGUAL MENOR MENOR_IGUAL MINUS MULT NOT NOVA_LINHA OF OR PERCENT PIPE PLUS PONTO PONTO_VIRGULA RCHAVE RCOLCHETE RPAREN SETAS SETAS_DUPLO SETAS_ESQUERDA STRING TABULACAO THEN TIL VARSYM WHEREexpressao : expressao PLUS termo\n                 | expressao MINUS termoexpressao : termotermo : termo MULT fator\n             | termo DIV fatortermo : fatorfator : INT\n             | FLOATfator : LPAREN expressao RPARENfator : LCHAVE expressao RCHAVEexpressao : expressao AND termo\n                 | expressao OR termotermo : NOT fatorexpressao : expressao IGUAL termo\n                 | expressao DIFERENTE termo\n                 | expressao MENOR termo\n                 | expressao MAIOR termo\n                 | expressao MENOR_IGUAL termo\n                 | expressao MAIOR_IGUAL termo'
    
_lr_action_items = {'NOT':([0,7,8,9,10,11,12,13,14,15,16,17,18,],[4,4,4,4,4,4,4,4,4,4,4,4,4,]),'INT':([0,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'FLOAT':([0,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'LPAREN':([0,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'LCHAVE':([0,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,2,3,5,6,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[0,-3,-6,-7,-8,-13,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'PLUS':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[9,-3,-6,-7,-8,-13,9,9,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'MINUS':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[10,-3,-6,-7,-8,-13,10,10,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'AND':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[11,-3,-6,-7,-8,-13,11,11,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'OR':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[12,-3,-6,-7,-8,-13,12,12,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'IGUAL':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[13,-3,-6,-7,-8,-13,13,13,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'DIFERENTE':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[14,-3,-6,-7,-8,-13,14,14,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'MENOR':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[15,-3,-6,-7,-8,-13,15,15,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'MAIOR':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[16,-3,-6,-7,-8,-13,16,16,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'MENOR_IGUAL':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[17,-3,-6,-7,-8,-13,17,17,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'MAIOR_IGUAL':([1,2,3,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[18,-3,-6,-7,-8,-13,18,18,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'RPAREN':([2,3,5,6,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[-3,-6,-7,-8,-13,36,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'RCHAVE':([2,3,5,6,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[-3,-6,-7,-8,-13,37,-1,-2,-11,-12,-14,-15,-16,-17,-18,-19,-4,-5,-9,-10,]),'MULT':([2,3,5,6,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[19,-6,-7,-8,-13,19,19,19,19,19,19,19,19,19,19,-4,-5,-9,-10,]),'DIV':([2,3,5,6,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[20,-6,-7,-8,-13,20,20,20,20,20,20,20,20,20,20,-4,-5,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressao':([0,7,8,],[1,22,23,]),'termo':([0,7,8,9,10,11,12,13,14,15,16,17,18,],[2,2,2,24,25,26,27,28,29,30,31,32,33,]),'fator':([0,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[3,21,3,3,3,3,3,3,3,3,3,3,3,3,34,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressao","S'",1,None,None,None),
  ('expressao -> expressao PLUS termo','expressao',3,'p_expressao_binaria','sintaticHaskell.py',63),
  ('expressao -> expressao MINUS termo','expressao',3,'p_expressao_binaria','sintaticHaskell.py',64),
  ('expressao -> termo','expressao',1,'p_expressao_termo','sintaticHaskell.py',68),
  ('termo -> termo MULT fator','termo',3,'p_termo_binario','sintaticHaskell.py',72),
  ('termo -> termo DIV fator','termo',3,'p_termo_binario','sintaticHaskell.py',73),
  ('termo -> fator','termo',1,'p_termo_fator','sintaticHaskell.py',77),
  ('fator -> INT','fator',1,'p_fator_numero','sintaticHaskell.py',81),
  ('fator -> FLOAT','fator',1,'p_fator_numero','sintaticHaskell.py',82),
  ('fator -> LPAREN expressao RPAREN','fator',3,'p_fator_parenteses','sintaticHaskell.py',86),
  ('fator -> LCHAVE expressao RCHAVE','fator',3,'p_fator_chaves','sintaticHaskell.py',90),
  ('expressao -> expressao AND termo','expressao',3,'p_expressao_booleana_binaria','sintaticHaskell.py',94),
  ('expressao -> expressao OR termo','expressao',3,'p_expressao_booleana_binaria','sintaticHaskell.py',95),
  ('termo -> NOT fator','termo',2,'p_termo_booleana_unario','sintaticHaskell.py',99),
  ('expressao -> expressao IGUAL termo','expressao',3,'p_expressao_relacional','sintaticHaskell.py',103),
  ('expressao -> expressao DIFERENTE termo','expressao',3,'p_expressao_relacional','sintaticHaskell.py',104),
  ('expressao -> expressao MENOR termo','expressao',3,'p_expressao_relacional','sintaticHaskell.py',105),
  ('expressao -> expressao MAIOR termo','expressao',3,'p_expressao_relacional','sintaticHaskell.py',106),
  ('expressao -> expressao MENOR_IGUAL termo','expressao',3,'p_expressao_relacional','sintaticHaskell.py',107),
  ('expressao -> expressao MAIOR_IGUAL termo','expressao',3,'p_expressao_relacional','sintaticHaskell.py',108),
]
