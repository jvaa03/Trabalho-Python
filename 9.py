temperaturas = []
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
for i in range(12):
    while True:
        try:
            temperatura = float(input(f"Digite a temperatura média de {meses[i]}:"))
            temperaturas.append(temperatura)
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número")
media_anual = sum(temperaturas) / len(temperaturas)
print(f"Média anual das temperaturas: {media_anual}°C")
print("Temperaturas acima da média anual:")
for i, temperatura in enumerate(temperaturas):
    if temperatura > media_anual:
        print(f"{meses[i]}: {temperatura}°C")