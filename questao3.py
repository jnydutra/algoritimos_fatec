populacao_a = 1500
populacao_b = 45000
anos = 0

while populacao_a <= populacao_b:
    populacao_a *= 0.1
    populacao_b *= 0.05
    anos += 1

print(f"População A ultrapassa População B em {anos} anos")

populacao_a = 1500
populacao_c = 65000
anos = 0

while populacao_a <= populacao_c * 123/100:
    populacao_a *= 0.1
    populacao_c *= 0.025
    anos += 1

print(f"População A ultrapassa População C em 23% em {anos} anos")

