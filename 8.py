medias = []
soma_notas = 0
for i in range(1, 11):
    print(f"Aluno{i}:")
    for j in range(1, 5):
        nota = float(input(f"Digite a nota {j}: "))
        soma_notas += nota
    media = soma_notas / 4
    medias.append(media)
    aprovados = 0
for media in medias:
    if media >= 7.0:
        aprovados += 1
print(f"Número de alunos com média maior ou igual a 7.0:{aprovados}")