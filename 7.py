
precos = {
    1: 10.00,
    2: 15.50,
    3: 5.00,
    4: 20.00,
    5: 7.50
}
total_geral = 0
print("Tabela de preços dos itens:")
for codigo, preco in precos.items():
    print(f"Código: {codigo}, Preço: R$ {preco}")
while True:
    try:
        codigo_item = int(input("\nDigite o código do item (ou 0 para encerrar o pedido): "))
        if codigo_item == 0:
            break
        if codigo_item not in precos:
            print("Código inválido. Por favor, insira um código válido.")
            continue
        
        quantidade = int(input("Digite a quantidade desejada: "))
        if quantidade <= 0:
            print("Quantidade inválida. Deve ser um número positivo.")
            continue

        valor_item = precos[codigo_item] * quantidade
        total_geral += valor_item
        print(f"Valor a ser pago pelo item {codigo_item}: R$ {valor_item}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

print(f"Total geral do pedido: R$ {total_geral}")
