import agente
import mundo
import util

def iniciar():
    player = agente.inicializar_agente()
    mapa = mundo.criar_mundo()

    while player["vivo"]:
        util.limpar_tela()
        percepcoes = mundo.percepcoes_sentidos (mapa,player["posicao"])
        util.mostrar_status(player, percepcoes)
        
        comando= util.exibir_menu()
        if comando == 'E': break
        agente.mover(player, comando)
if __name__ == "__main__":
    iniciar()
