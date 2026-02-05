import agente
import mundo
import util

def iniciar():
    # Inicializa o jogador e o mundo
    player = agente.inicializar_agente()
    mapa = mundo.criar_mundo()
    
    while player["vivo"]:
        util.limpar_tela()
        
        # 1. PEGAR AS PERCEPÇÕES (Brisa, Fedor, Brilho)
        # Importante: passamos o mapa e a lista da posição [linha, coluna]
        percepcoes = mundo.percepcoes_sentidos(mapa, player["posicao"])
        
        # 2. MOSTRAR O STATUS
        util.mostrar_status(player, percepcoes)
        
        # 3. RECEBER O COMANDO
        comando = util.exibir_menu()
        
        # 4. EXECUTAR A AÇÃO
        if comando == 'E':
            print("Saindo do jogo... Até logo!")
            break
        elif comando in ['N', 'S', 'L', 'O']:
            agente.mover(player, comando)
        elif comando == 'P':
            agente.pegar_ouro(player, percepcoes)
        elif comando == 'A':
            agente.atirar_flechas(player)
            
        # 5. VERIFICAR SE O JOGADOR MORREU (Lógica futura para Wumpus/Poço)
        if not player["vivo"]:
            print("\nGAME OVER! Você não sobreviveu à caverna.")

if __name__ == "__main__":
    iniciar()