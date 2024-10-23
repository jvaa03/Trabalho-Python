while True: 
    nome=str(input("Digite seu nome(Precisa ter 3 letras):"))
    if len(nome)>3:
        print("Nome válido")
        break 
    else: 
        print("Nome invalido")
while True: 
    idade=int(input("Digite sua idade(Precisa ser maior que 0 e menor 151):"))
    if 0 < idade <= 151:
        print("Idade válida")
        break
    else: 
        print("Idade inválida")
while True: 
    salario=int(input("Digite seu salário(Precisa ser maior que 0):"))
    if 0 < salario:
        print("Salário válido")
        break
    else: 
        print("Salário inválido")
while True: 
    sexo=str(input("Digite seu sexo f(Feminino) ou m(Masculino):"))
    if sexo in 'fm':
        print("Sexo válido")
        break
    else: 
        print("Sexo inválido")
while True: 
    estado_civil=str(input("Digite seu Estado Civil s(Solteiro(a)) c(Casado(a)) v(Viúvo(a)) d(Divorciado(a)):"))
    if estado_civil in 'scvd':
        print("Estado Civil válido")
        break
    else: 
        print("Estado Civil inválido")
print('--------------------')
print("Nome:",nome)
print("Idade:",idade)
print("Salario:",salario)
print("Sexo:",sexo)
print("Estado Civil:",estado_civil)
