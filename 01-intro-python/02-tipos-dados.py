# Tipos de dados
# int, float
# string, list, tuple, set
# dict
# None

# int
idade = 20

# float
altura = 1.8

#string
nome = "Davi Gomes"
print(nome[0])
print(nome[-1])
print(nome[0:4])

# char? (não existe)
letra = "a"

# nome é um objeto de classe string
# nome tem o que? métodos
print(nome.capitalize())

#interpolação de str e variáveis
nome = "Bongiourno"
idade = 75 
mensagem = f"Olá {nome}, você tem {idade} anos"
print(mensagem)

# list~
# lista de valores
# pode ser alterada
habilidades = []
habilidades = ["java", "c#", "CSS"]
print(habilidades[0])
print(habilidades [-1])

habilidades[0] = "python"
print(habilidades[0])

habilidades.append("html") #add ao final
habilidades.insert(0, "kotlin") #add na posição desejada, reposiciona a lista

# tuple
# 'lista' de valores
# não pode ser alterada (add/remover)
opcoes = ("sim", "não", "talvez")

# set
# não indexado
# não permite elementos duplicados
# digite mensagens
# digite os emails de destino
emails = {"davi@gmail.com", "rocha@gmail.com", "davi@gmail.com"}
emails.add("davi@gmail.com")
print(emails)


#for
for opcao in opcoes:
    print(opcao)

for habilidade in habilidades:
    print(habilidades)

# dict (dicionário)
# chave : valor
# key : value

# site de emprego
empresa = "QuickMotors"
titulo = "Engenheiro Mecânico"
salario = 500000.00
remoto = False

# vaga
vaga = {
    "empresa": "QuickMotors",
    "titulo": "Engenheiro Mecânico",
    "salario": 500000.00,
    "remoto": False
}

print(vaga["salario"])
print(vaga)

# None
nome = None