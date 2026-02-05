def criar_mundo():
# Toda tupla tem que ter Wunpus, Poço, Brisa Fedor e Ouro
    mapa= [
        [(False,False,False,False,False),(False,False,True,False,False),(False,True,False,False,False),(False,False,True,False,False)],
        [(False, False, False,True,False ),(False,False,False,False,False),(False,False,True,False,False),(False,False,False,False,False)],
        [(True,False,False,False,False),(False,False,False,True,False),(False,False,False,False,False),(False,False,True,False,False)],
        [(False,False,False,True,False),(False,False,False,False,False),(False,False,True,False,False),(False,False,False,False,True)]

    ]
return mapa 

def percepcoes_sentidos(mapa, posicao):
    linha=posicao[0]
    coluna=posicao[1]
    celula=mapa[linha][coluna]
    percepcoes=[]

    if celula[2] == True:
        percepcoes.append("Brisa")
    if celula[3] == True:
        percepcoes.append("Fedor")
    if celula[4] == True:
        percepcoes.append("Brilho")
    return percepcoes

