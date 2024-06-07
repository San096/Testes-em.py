import itertools

def combinaçoes_possiveis(numeros, tamanho_combinacao):
    todas_combinacoes = set(itertools.combinations(numeros,tamanho_combinacao))
    
    return todas_combinacoes

numeros = [1,2,3,4,5,6,7,8,9,]

tamanho_combinacao = 6

todas_combinacoes = combinaçoes_possiveis(numeros,tamanho_combinacao)

print("todas as conbinaçoes possiveis de {tamanho_combinaçoes}numeros")

for com in todas_combinacoes:
    print(com)

print(f"combinaçoes possiveis de :{len(todas_combinacoes)}")
print(f"                 voce vai gastar : R${len(todas_combinacoes)*5:,.2f}")

    
