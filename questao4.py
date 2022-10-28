ultimo_numero = int(input())
tamanho_sequencia_constante = 1
tamanho_sequencia_crescente = 1
soma_sequencia_crescente = ultimo_numero

maior_tamanho_sequencia_constante = 1
maior_tamanho_sequencia_crescente = 1
maior_soma_sequencia_crescente = ultimo_numero

for i in range(149):
    numero = int(input())

    if numero == ultimo_numero + 1:
        tamanho_sequencia_crescente += 1
        soma_sequencia_crescente += numero
    else:
        if (
            tamanho_sequencia_crescente > maior_tamanho_sequencia_crescente
            or (tamanho_sequencia_crescente == maior_soma_sequencia_crescente and soma_sequencia_crescente > maior_soma_sequencia_crescente)
        ):
            maior_tamanho_sequencia_crescente = tamanho_sequencia_crescente
            maior_soma_sequencia_crescente = soma_sequencia_crescente

        tamanho_sequencia_crescente = 1
        soma_sequencia_crescente = numero

    if numero == ultimo_numero:
        tamanho_sequencia_constante += 1
    else:
        if (
            tamanho_sequencia_constante > maior_tamanho_sequencia_constante
            or (tamanho_sequencia_constante == maior_tamanho_sequencia_constante and numero > ultimo_numero)
        ):
            maior_tamanho_sequencia_constante = tamanho_sequencia_constante

        tamanho_sequencia_constante = 1

    ultimo_numero = numero

print(f"Tamanho da maior sequencia crescente: {maior_tamanho_sequencia_crescente}")
print(f"Tamanho da maior sequencia constante: {maior_tamanho_sequencia_constante}")