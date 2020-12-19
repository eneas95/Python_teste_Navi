import math

v = []

#alimentar o vetor
for i in range(0,10):
    if(i % 2 == 0):
        X = 3**i + 7*math.factorial(i)
    else:
        X = 2**i + 4*math.log(i)
    
    v.append(X)

#encontrar a posição do maior número
maior_num = 0
indice = 0
for j in range(0, 10):
    if(v[j]>maior_num):
        maior_num = v[j]
        indice = j
print("Esta é a posição do maior elemento do vetor: ",indice)

#encontrar a média dos elementos contidos no vetor e arredondar para 2 casas decimais
media_float = sum(v)/len(v)
media = round(media_float, 2)
print("Esta é a média dos elementos contidos no vetor: ", media)