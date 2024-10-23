while True:
    try:
        divida = float(input("Digite o valor da dívida: "))
        if divida < 0:
            print("Valor inválido. A dívida deve ser um valor positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

print("Tabela de Parcelamento:")
print(f"{'Parcelas':<10}{'Juros (%)':<12}{'Valor da Dívida':<20}{'Valor dos Juros':<18}{'Valor da Parcela':<20}")
for parcelas in range(1, 11):
    if parcelas == 1:
        juros = 0
    elif parcelas == 2:
        juros = 5
    elif parcelas == 3:
        juros = 10
    elif parcelas == 4:
        juros = 15
    else:
        juros = 20
    
valor_juros = (divida * juros) / 100
valor_total = divida + valor_juros
valor_parcela = valor_total / parcelas
print(f"{parcelas:<10}{juros:<12}{divida:<20.2f}{valor_juros:<18.2f}{valor_parcela:<20.2f}")
