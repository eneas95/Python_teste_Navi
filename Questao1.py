contador = 0

for i in range(1,5000001):
    #primeiro verificar se é par
    if(i%2==0):
        #verificar agora se é múltiplo de 49
        if(i%49==0):
            # ver por fim se é múltiplo de 37
            if(i%37==0):
                contador = contador + 1

print(contador)