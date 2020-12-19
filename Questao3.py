
dicionario = {}
for i in range(0,5):
    d=i+1
    x = input("Insira o nome do {}º aluno: ".format(d))
    y = float(input("Insira a nota do {}: ".format(x)))
    dicionario[x]=y

print(dicionario)

maior_num = 0
maior_chave = ""
#para cada chave do meu dicionario, ver se o valor associado é maior que maior_num
for chave in dicionario:
    if(dicionario[chave] > maior_num):
        maior_num = dicionario[chave]
        maior_chave = chave

print(maior_chave, "possui a maior nota:", maior_num)