while True:
    print("Insira sua compra:")
    total = 0
    while True:
        preco = float(input("Digite o valor do seu produto (digite 0 quando terminar de inserir os produtos): "))
        if preco == 0:
            break
        total += preco
        print(f"Valor total da compra: R${total}")
    while True:
        dinheiro = float(input("Insira o valor para pagar a conta: R$"))
        if dinheiro >= total:
            troco = dinheiro - total
            print(f"Troco: R${troco}")
            break
        else:
            print("O valor inserido não é suficiente para pagar a compra, insira outro valor.")
    compra = input("Você deseja realizar uma nova compra (sim ou não)? ")
    if compra == 'não':
        print("Caixa encerrado")
        break