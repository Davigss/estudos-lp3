# Função

# quero somar uma lista de números
# usar funcao sum()

# quero calcular média de notas dos alunos
# 1. tem no python?
# 2. alguém ja programou (copiar ou adicionar dependencia)
# 3. declarar 

# 1 - Declaração

# def nome_funcao(parametro1, paramentro2):
#   return valor

# 2 - Chamada
print("Olá")
sum([1,2,3])
#nome_funcao("dad", 1)

# Função sem retorno e sem argumentos
def imprimir_mensagem():
    print("Fúriaaaaaaaa!")


imprimir_mensagem()
imprimir_mensagem()


#  Função sem retorno  com argumentos
# parametro vs argumentos
def saudacoes(nome):
    print(f"Bom dia {nome}!")

# argumento para parametro nome "Davi"
saudacoes("Davi")

# argumento para parametro nome
nome_completo = "Davi Gomes"
saudacoes(nome_completo)


#  Função com retorno  sem argumentos
def obter_mensagem():
    return "Socorro"

mensagem = obter_mensagem()
print(mensagem)

print(obter_mensagem())


#  Função com retorno  com argumentos
def gerar_saudacao(nome):
    return f"Vai {nome}"

print(gerar_saudacao("Fallen"))
print(gerar_saudacao("Art"))

# Retorno parâmetros
# não      não
# não      sim
# sim      não
# sim      sim (adequada) (função pura)

def saudacao(nome, frase):
    print(f"{frase},{nome}")

saudacao("Yurihh", "Come casadas = ")

def saudacao(nome, frase):
    return f"{frase},{nome}"

print(saudacao("Yurihh", "Come casadas = "))

# Enviar email saudacao
# Criar uma carta em pdf

# Entrada
notas_alunos = [
    [9.0, 10.0, 8.0],
    [2.0, 5.0, 10.0],
    [0.0, 2.5, 4.0],
]

# saida

def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_media_alunos(notas_alunos):
    medias = []

    for valores in notas_alunos:
        media = calcular_media(valores)
        medias.append(media)

    return medias

medias = calcular_media_alunos(notas_alunos)
print(medias)


# Argumentos nomeados
def saudacao(nome, frase):
    return f"{frase},{nome}"

print(saudacao("Fúria", "joga o fino "))
print(saudacao(nome="Fúria",  frase="joga o fino "))
print(saudacao("Fúria", frase="joga o fino "))

# Argumentação valor (default)
def saudacao(nome, frase="vai")