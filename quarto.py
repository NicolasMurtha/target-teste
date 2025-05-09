"""

4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

"""

faturamento = {
    "SP": 67.83643,
    "RJ": 36.67866,
    "MG": 29.22988,
    "ES": 27.16548,
    "Outros": 19.84953
}

faturamento_total = sum(faturamento.values())
print("faturamento total:" , faturamento_total)
print("")
print("faturamento por estado:")

for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")

