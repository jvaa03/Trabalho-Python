notas=[]
quantidade_notas=int(input("digite a quantidade de notas:"))
for i in range(quantidade_notas):
    nota=float(input(f"digite sua nota{i+1}:"))
    notas.append(nota)
media = sum(notas)/len(notas)
print("sua media foi de:",media)