salario_fixo = float(input("Salário Fixo: "))
valor_vendas = float(input("Valor Vendas: "))

salario_final = salario_fixo

if valor_vendas <= 1500:
    salario_final += 0.05 * valor_vendas
else:
    diferenca = valor_vendas - 1500
    salario_final += 0.05 * 1500 + diferenca*0.07

print(f"Salario Final: {salario_final}")