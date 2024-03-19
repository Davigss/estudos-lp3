# Exercicio 3

valor_conta = float(input("Digite o valor da sua compra: "))

faixa_desconto = [(0.01, 9.99, 0.0),
            (10.00, 99.99, 5.0),
            (100.00, 499.99, 10.0),
            (500.00, float("inf"), 15.0)]

desconto = 0.0

for faixa in faixa_desconto:
    limite_inferior, limite_superior, porcentagem = faixa
    if limite_inferior <= valor_conta <= limite_superior:
        desconto = valor_conta * (porcentagem / 100)
        break

valor_final = valor_conta - desconto

print("Desconto aplicado: R$", desconto)
print("O valor final da conta foi; R$", valor_final)

