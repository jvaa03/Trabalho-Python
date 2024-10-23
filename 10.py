notas = []
while True:
    try:
        nota = float(input("Digite uma nota (-1 para encerrar):"))
        if nota == -1:
            break
        notas.append(nota)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número")

quantidade = len(notas)
print(f"\nQuantidade de valores lidos: {quantidade}")

print("Valores informados: ", end="")
print(*notas)

print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

soma=sum(notas)
media=soma / quantidade if quantidade > 0 else 0
print(f"\nSoma dos valores: {soma}")
print(f"Média dos valores: {media}")

acima_media = sum(1 for nota in notas if nota > media)
print(f"Quantidade de valores acima da média: {acima_media}")

abaixo_media = sum(1 for nota in notas if nota < 7)
print(f"Quantidade de valores abaixo de sete: {abaixo_media}")

print("Programa encerrado.")
