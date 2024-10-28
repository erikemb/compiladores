/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Copyright (C) 2000 Gerwin Klein <lsf@jflex.de>                          *
 * All rights reserved.                                                    *
 *                                                                         *
 * Thanks to Larry Bell and Bob Jamison for suggestions and comments.      *
 *                                                                         *
 * License: BSD                                                            *
 *                                                                         *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */


%%

%debug

%type Object
%class Lexer
%line
%column




//%byaccj
%{

int numeroDeComentariosAbertos = 0;

private int checarComentariosAbertos(){
    return numeroDeComentariosAbertos;
}

private void mudarEstadoPorQuantidadeDeComentarios(){
    if (checarComentariosAbertos()>0){
        yybegin(COMMENT);
    }
    else{
       yybegin(YYINITIAL);
    }
}

enum sym{
    OPERACAO_SUM, 
    OPERACAO_SUB,
    OPERACAO_MULT,
    OPERACAO_DIV,
    OPERACAO_POW,
    PARENTESE_ESQUERDA,
    PARENTESE_DIREITA,
    OPERACAO_EQUAL,
    OPERACAO_MAIOR_IGUAL,
    OPERACAO_MENOR_IGUAL,
    BARRA,
    VIRGULA,
    PONTO_VIRGULA,
    CRASE;
}

class Token {
    public final int codigo; 
    public Object valor;
    Token (int c, Object v) {
        codigo=c; 
        valor=v;}
    Token (int c) {
        this(c, null); }
 }


private void imprimir(String descricao, String lexema) {
    System.out.println(lexema + " - " + descricao);
}

%}

%state COMMENT

PONTOS = [..]
DOISPONTOS = [:]
DOISPONTOSDUPLO = [::]
IGUALDADE = [=]
BARRAS = ["\|"]+
ATRIBUICAO = [->]
OPENCHAVE = [\{-]
CLOSECHAVE = [-\}]
CRASE = [`]

/* symbol */
ASCISYMBOL = ([\!]|[\#]|[\$]|[\&]|[\⋆]|[\+]|[\.]|[/]|[\<]|[\=]|[\>]|[\?]|[@]|[\\]|[\^]|[\|]|[\-]|[\~]|[\:])

/* TIPOS */
DIGIT = [0-9]
OCTIT = [0-7]
HEXIT = ([0-9]|[A-F]|[a-f])
INT = [0-9]+
FLOAT =[0-9]+("." [0-9]+)
LITERAL = ({INT}|{FLOAT}|{CHAR}|{STRING})
OCTAL = [OCTIT]+
HEXADECIMAL = ({HEXIT})+
EXPONENT = (e|E)[E|-]+(INT)
ESPACO = " "
GRAPHIC = ({MINUSC}|{MAISC}|{ASCISYMBOL}|{INT}|[\"]|[\'])
CHAR = \'({GRAPHIC}|{ESPACO}|{ESCAPE})\'
CHARESC = ([a]|[b]|[f]|[n]|[r]|[t]|[v]|\\|\"|\'|\&)
ESCAPE = \\([CHARESC]|[INT]|\o[OCTAL]|\x[HEXADECIMAL])
TAB = [\t]
SPACE = " "
BRANCO = [\n|{SPACE}|{TAB}|\r]
NOVA_LINHA = \n | \r | \r\n
WHITECHAR = ({NOVA_LINHA}|[\|]|{ESPACO}|{TAB})
GAP = \\({WHITECHAR})+
STRING = ["\""](({GRAPHIC}|{ESPACO}|{ESCAPE}|{GAP})*?)["\""]
MAISC = [A-Z]
MINUSC = [a-z]
any = ({GRAPHIC}|{SPACE}|{TAB})
ANY = ({GRAPHIC}|{WHITECHAR})
RETURN = [\r]
LINEFEED = [\n]
DASHES = [\--]([\-]*)


/* Identificadores */
VARID = ({MINUSC}({MINUSC}|{MAISC}|{INT}|\')*)
VARSYM = ({ASCISYMBOL}&&[^\:]{ASCISYMBOL}*)


%%

<COMMENT> {
    "\*\/" {imprimir("FIM_COMENTARIO",yytext()); numeroDeComentariosAbertos--; mudarEstadoPorQuantidadeDeComentarios();}
    "\/\*" {imprimir("INICIO_COMENTARIO",yytext()); numeroDeComentariosAbertos++; mudarEstadoPorQuantidadeDeComentarios();}
    [^] {}
}

/* operadores */
<YYINITIAL> {

"\/\*" {imprimir("INICIO_COMENTARIO",yytext()); numeroDeComentariosAbertos++; yybegin(COMMENT);}

"+" { imprimir( "OPERACAO_SUM",yytext()); } 
"-" { imprimir( "OPERACAO_SUB",yytext()); }
"*" { imprimir( "OPERACAO_MULT",yytext()); }
"/" { imprimir( "OPERACAO_DIV",yytext()); }
"^" { imprimir( "OPERACAO_POW",yytext()); }
"(" { imprimir( "PARENTESE_ESQUERDA",yytext()); }
")" { imprimir( "PARENTESE_DIREITA",yytext()); }
"=" { imprimir( "OPERACAO_EQUAL",yytext()); }
"=>" { imprimir( "OPERACAO_MAIOR_IGUAL",yytext()); }
"<=" { imprimir( "OPERACAO_MENOR_IGUAL",yytext()); }
"|" { imprimir( "BARRA",yytext()); }
"," {imprimir( "VIRGULA",yytext()); }
";" {imprimir( "PONTO_VIRGULA",yytext()); }
"`" {imprimir( "CRASE",yytext()); }



{BRANCO}  { imprimir("BRANCO",yytext()); }

"if" {imprimir( "Palavra reservada",yytext());}
"then" {imprimir( "Palavra reservada",yytext());}
"else"  {imprimir( "Palavra reservada",yytext());}
"return" {imprimir( "Palavra reservada",yytext());}
"case" {imprimir( "Palavra reservada",yytext());}
"default" {imprimir( "Palavra reservada",yytext());}
"in" {imprimir( "Palavra reservada",yytext());}
"let" {imprimir( "Palavra reservada",yytext());}
"of" {imprimir( "Palavra reservada",yytext());}
"where" {imprimir( "Palavra reservada",yytext());}
"Int" {imprimir( "Palavra reservada",yytext());}
"Float" {imprimir( "Palavra reservada",yytext());}
"Bool" {imprimir( "Palavra reservada",yytext());}
"Char" {imprimir( "Palavra reservada",yytext());}
"True" {imprimir( "Palavra reservada",yytext());}
"False" {imprimir( "Palavra reservada",yytext());}
"_" {imprimir( "Palavra reservada",yytext());}


{INT} {imprimir( "Numero INT",yytext()); }
{FLOAT} {imprimir( "Numero FLOAT",yytext()); }
{STRING} {imprimir( "STRING",yytext()); }
{CHAR} {imprimir( "CHAR",yytext()); }

{PONTOS} {imprimir( "Simbolo reservado",yytext()); }
{DOISPONTOS} {imprimir( "Simbolo reservado ",yytext()); }
{DOISPONTOSDUPLO} {imprimir( "Simbolo reservado ",yytext()); }
{IGUALDADE} {imprimir( "Simbolo reservado ",yytext()); }
{BARRAS} {imprimir( "Simbolo reservado ",yytext()); }
{CRASE} {imprimir( "Simbolo reservado ",yytext());}
{ATRIBUICAO} {imprimir( "Simbolo reservado ",yytext());}
{OPENCHAVE} {imprimir( "Simbolo reservado ",yytext());}
{CLOSECHAVE} {imprimir( "Simbolo reservado ",yytext());}
{DASHES} {imprimir( "Simbolo DASHES ",yytext());}
{NOVA_LINHA} {imprimir("NOVA_LINHA",yytext());}

{VARID} { imprimir("Identificador",yytext()); }
{VARSYM} {System.out.println("> Encontrei o tipo VARSYM '"+yytext()+"'");}

\b     { System.err.println("Sorry, backspace doesn't work"); }

/* error fallback */
[^]    { System.err.println("Error: unexpected character '"+yytext()+"'"+ " line="+ yyline+ " column="+ yycolumn); return -1; }

}