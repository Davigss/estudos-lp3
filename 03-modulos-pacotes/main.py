# importa tudo de matematica (usar matematica.PI)
# import matematica

# importar apenas o elementos 
from matematica import PI, subtrair, somar
# from matematica import *

# caso confita nome
# from matematica import PI as MAT_PI

print(PI)
print(somar(10, 50))
print(subtrair(10, 50))

# importar a fn media do pacote estatistica e modulo descritiva

from estatistica.descritiva import media
from estatistica.inferencial import valor