#fazendo os imports necessarios
from turtle import Screen
from snake import Snake
import time

#instancia um objeto da classe Screen
screen = Screen()

#configura o tamanho da tela
screen.setup(width=600,height=600)

#coloca a cor preta para o fundo da tela
screen.bgcolor('black')

#coloca um titulo para a tela
screen.title("Jogo da cobrinha")

#desliga as animacoes da cobrinha
screen.tracer(0)

#instancia um objeto da classe Snake
cobra = Snake()

#variavel flag para controlar o status do jogo
jogoAtivo = True

#loop while para manter o jogo ativo
while jogoAtivo:
    #liga as animacoes da cobrinha para atualizar a tela
    screen.update()

    #time.sleep faz o programa ter uma lentidao
    time.sleep(0.1)

    #usa o metodo para mover a cobrinha
    cobra.moverCobra()

    
#faz com que a tela desapareca ao clicar
screen.exitonclick()