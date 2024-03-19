# for
palavra = "Python"
for letra in palavra:
    print(letra)

numeros = [1, 2, 3, 4, 6]
for numero in numeros:
    print(numero)

# range
# range(stop)
# range(5) - 1, 2, 3, 4, 5

# range(start, stop)
# range(4, 10) - 4, 5, 6, 7, 8, 9, 

# range(start, stop, step)
# range(3, 10, 2) - 3, 5, 7, 9, 

for i in range(10):
    print(i)

# while

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break
# break - pula o loop
# encontrar o primeiro numero par

numeros = [1, 3, 4, 7, 10]
for numero in numeros:
    if numero %2 == 0:
        print(numero)
        break 

# continue
# pula interação

for numero in numeros:
    if  numero <= 0:
        continue
    print(numero)

# compreensão de lista
numeros = [1, 3, 4, 2, 6, 8, 16]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)
    print (quadrados)

quadrados = [numero ** 2 for numero in numeros]
print(quadrados)

numeros = [2, 4, 5, 8, 6]
pares= []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)

pares = [numero for numero in numeros if numero % 2 == 0]

palavras = ["ola", "mundo", "teste"]
palavras2 = [palavra.upper() for palavra in palavras]
