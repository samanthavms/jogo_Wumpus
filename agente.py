def inicializar_agente():
    return{
        "posicao": [0,0],
        "vivo": True ,
        "tem_ouro": False,
        "flecha": 1,
        "pontos":100
    }

def mover(agente, direcao):
    linha=agente["posicao"] [0]
    coluna=agente["posicao"] [1] 
    #PARA NORTE O AGENTE SOBE (DIMINUI A LINHA )
    if direcao == "N" and linha > 0: # Garantir que o agente não saia do mapa 0
        agente["posicao"] [0] -=1
    #PARA SUL O AGENTE DESCE (AUMENTA A LINHA)
    elif direcao == "S" and linha < 3:
        agente["posicao"] [0] +=1
    #PARA LESTE O AGENTE VAI PARA DIREITA (AUEMENTA A COLUNA)
    elif direcao == "L" and coluna < 3:
        agente["posicao"] [1] +=1
    #PARA OESTE O AGENTE VAI PARA ESQUERDA (DIMINUI A COLUNA)
    elif direcao == "O" and coluna > 0:
        agente["posicao"] [1] +=1
    else:
        print("Você bateu na parede da caverna ")

def pegar_ouro(agente, percepcoes):
    if Brilho in percepcoes:
        agente["ouro"] = True
        print("Você capturou o ouro! Agora retorne para a entrada da caverna")
    else:
        print("Aqui não possui ouro")

def atirar_flechas(agente):
    if agente["flecha"] > 0:
        agente["flecha"] -=1
        print("Você disparou a sua flecha.")
        return True
    else:
        print("Você não possui mais flecha.")
        return False