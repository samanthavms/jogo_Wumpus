import os #Para conseguir identificar o SO do computador 
def limpar_tela():
    if os.name == 'nt':
        os.system('cls') #COMANDO PARA LIMPAR O TERMINAL DE COMANDO NO WINDOWNS
    else:
        os.system('clear')

def exibir_menu():
    print('\n COMANDOS ')
    print('Aperte [N] para o joagador ir para cima ')
    print('Aperte [S] para o jogador ir para baixo ')
    print('Aperte [L] para o jogador ir para direita  ')
    print('Aperte [O] para o jogador ir para esquerda ')
    print('Aperte [P] para pegar o ouro')
    print('Aperte [A] para atirar a flecha ')
    print('Aperte [E] para sair ')
    print('---'*30)
    
    escolha = input('O que você deseja fazer?').upper() #upper para digitar minuscula, o progrma entender com maiúscula
    return escolha

def mostrar_status(agente,percepcoes):
    print(f"\n Posição atual:{agente['posicao']}")
    print(f"inventário: OURO={agente['tem_ouro']} | Flechas={agente['flecha']}")
    print(f"Pontos:{agente['pontos']}")
    print("---"*30)
    print(f"Percepções:{percepcoes}")
