idades=[]
quantidade_alunos=int(input("quantos alunos vão fazer a pesquisa:"))
for i in range (quantidade_alunos):
    alunos=int(input("digite sua idade:" ))
    idades.append(alunos)
media = sum(idades)/len(idades)
print("a media da idade da turma é:",media)
if 0 <= media <=25:
    print("sua turma é jovem")
if 26 <= media <= 60:
    print("sua turma é adulta")
if  media > 60:
    print("sua turma é idosa")