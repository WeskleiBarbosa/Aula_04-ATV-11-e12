total = 0

for i in range(5):
    preco = float(input(f"Digite o preço do produto {i + 1}: "))
    total += preco
    if total > 100:
        print("Total ultrapassou 100. Interrompendo o loop.")
        break

if total > 100:
    desconto = total * 0.10
    total -= desconto
    print(f"Desconto de 10% aplicado. Total após desconto: R${total:.2f}")
else:
    print(f"Total sem desconto: R${total:.2f}")