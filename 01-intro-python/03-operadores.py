# Operadores aritméticos
# +, -, *, /, **, ...

nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3

print(media)

# Numero elevado a outro
# e elevado n
# 10 elevado a 2

numero_elevado_5 = nota2 ** 5
print(numero_elevado_5)

# Operadores lógicos
# and, or , not

print(3 + 2) #5
print(True and True)   #True
print(True and False)  #False 
print(False and True)  #False
print(False and False) #False

print(True or True)    #True
print(True or False)   #True
print(False or True)   #True
print(False or False)  #False

print(not True)        #False
print(not False)       #True

# Permitir Entrada
# - O usuario for funcionario E
# - O usuario não estiver bloqueado E
# - Hora atual estiver entre 8h e 18h 

# Permitir Entrada
# - admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

funcionario_ativo = usuario_funcionario and not usuario_bloqueado  
horario_comercial = hora_atual >= 8 and hora_atual <= 18

if usuario_admin or (funcionario_ativo and horario_comercial):
    print("acesso permitido")

# Operadores de Comparação
# ==, !=, >, <, <=, >=
# == comparando valores
# = atribuindo
# != diferente 

# is, is not
# operador de identidade
# comparar se objetos ocupam o mesmo espaço de memória 

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) #True
print(a is b) #False

c = b
print(c is b) #True

# operador in , not in
# verificar se um elementio existe ou não em uma sequência
# str, list, tuple

opcoes = ("sim", "não", "talvez")
opcao = input("digite sua opção: ")
opcao = opcao.lower().strip()

if opcao in opcoes:
    print("ok")
else:
    print("não tem essa opção")





