# Identificadores
# letra, número e _
# palavras reservadas: def, if, for...

# case sensitive
nome = "João"
Nome = "João"
# são diferentes 

# Variáveis
# identificador = valor (literal)
# Python: altura = 1.8
# tipagem dinâmica

# java: tipo identificador = valor
# java: float altura = 1.8

altura = 1.8
idade = 22
nome = "Davi Gomes"
emprego = True

# Constantes
# python não tem constante
PI = 3.14
pi = 3.14

# comentario única linha

""" 
comentario
multiplas
linhas
""" 

# docstring
# documentação do codigo
# classes, módulo, etc
def somar(n1, n2):
    """
    Função que soma dois números

    :param n1: primeiro número
    :param n2: segundo número
    :return: a soma dos parâmetros
    """
    return n1 + n2

somar(10.2, 20.5)