# Operador ternário

idade = 20

# maior ou menor

status =" "

if idade >=18:
    status = "maior"
else:
    status = "menor"

status = "maior" if idade >= 18 else "menor"

print(status)

# Match

dia = 3
match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terça")
    case _:
        print("dia invalido")

match dia:
    case 1 | 7:
        print("fim de semana")
    case 2 |3|4|5|6:
        print("dia útil")
    case _:
        print("dia inválido")