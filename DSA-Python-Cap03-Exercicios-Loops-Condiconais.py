##Exercícios - Loops e Condiconais
# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
Dias = {1: 'segunda-feira',2: 'terça-feira',3: 'quarta-feira',4: 'quinta-feira',5: 'sexta-feira',6: 'sábado',7: 'domingo'}
DiaEscolha = int(input('Insira o número referente ao dia da semana: \n1-Segunda-Feira \n2-Terça-Feira \n3-Quarta-Feira \n4-Quinta-Feira \n5-Sexta-Feira \n6-Sábado \n7-Domingo \nResponda: '))
if DiaEscolha in [6,7]:
    print('%r é dia de descanso' %(Dias[DiaEscolha]).capitalize())
elif DiaEscolha in range(1,6):
    print('Hoje é %r, você precisa trabalhar!' %(Dias[DiaEscolha]).capitalize())

# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
lstFruta = ['Abacaxi','Morango','Banana','Maçã','Mamão']
if 'Morango' in lstFruta:
    print('Tem morango na lista')
else: print('Não tem morango na lista')

# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista
tpl1 = (2,4,6,8)
for i in tpl1:
    lst1 = i * 2
    print(lst1)

# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
Seq = range(100,151,2)
for i in Seq:
    s = i
    print(s)

# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35,
# imprima as temperaturas na tela
temperatura = 40
while temperatura > 35:
    print(temperatura)
    break

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
counter = 0
while counter < 100:
    if counter == 23:
        break
    else:
        pass
    print(counter)
    counter += 1

# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20,
# adicione à lista, apenas os valores pares e imprima a lista
list2 = []
vl = 4
while vl <= 20:
    if vl % 2 == 0:
        print(vl)
    vl += 1

# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)
list3 = []
for l in nums:
    list3.append(l)
print(list3)

# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na
# sua instrução de impressão
frase = ('“É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir.” (Machado de Assis)')
contagem = 0
for ctn in frase:
    if ctn == 'r':
        contagem += 1
print('Há %r letras R nesta frase.' %(contagem))