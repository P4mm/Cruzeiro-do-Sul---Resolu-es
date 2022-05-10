valorOrig = 200
qtdParcela = 4
juros = 0

if(qtdParcela == 0 or qtdParcela ==1):
    juros = 0
else:
    if(qtdParcela == 2 or qtdParcela ==3):
        juros = 10
    elif(qtdParcela > 4):
        juros = 20
        
        
valorAtualizado = valorOrig + (valorOrig*juros/100)
prestMensal = valorAtualizado / qtdParcela

print(valorAtualizado)
print(prestMensal)
