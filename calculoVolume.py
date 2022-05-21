#!/usr/bin/env python
# coding: utf-8

# In[6]:



print('Insira as dimensões a seguir, separando as casas decimais por ponto. Exemplo: 3.52.')
print('Para bases circulares, insira o valor zero(0) para profundidade.')

profundidade = float(input('Digite o valor da profundidade do sólido: '))
largura = float(input('Digite o valor da largura do sólido: '))
altura = float(input('Digite o valor da altura do sólido: '))

print('Responda "1" para prisma retangular, "2" para prisma triangular, "3" para cone, "4" para cilindro e 5 para pirâmide.'
     )
solido = int(input('Qual é o tipo de sólido? '))
if solido == 1:
    volume = profundidade * largura * altura
    solido = 'um prisma de base retangular,'
elif solido == 2:
    volume = (((profundidade * largura)/2) * altura)
    solido = 'um prisma de base triangular,'
elif solido == 3:
    volume = (3.14 * ((largura/2)*(largura/2))) * (altura/3)
    solido = 'um cone,'
elif solido == 4:
    volume = (3.14 * ((largura/2)*(largura/2))) * altura
    solido = ' um cilindro,'
else:
    volume = (profundidade * largura * altura)/6
    solido = 'uma pirâmide,'
    
print('O sólido é', solido, 'e o volume é: {:.2f}'.format(volume), 'unidades cúbicas.')

