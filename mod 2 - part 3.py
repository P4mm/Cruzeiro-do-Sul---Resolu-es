a=1
b=5
frequencia = 80

if (frequencia > 75):
    soma = a+b
    if(soma > 6):
         print("Aluno aprovado")
    elif(soma > 2):
        print("Aluno pode realizar prova de recuperação")
    else:
        print("Aluno reprovado")
else:
    print("Aluno reprovado direto")
