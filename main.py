#fazendo os imports necessarios
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
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

#instancia um objeto da classe ScoreBoard para servir de placar
placar = ScoreBoard()

#instancia um objeto da classe Snake
cobra = Snake()

#instancia um objeto da classe Food
comida = Food()

#metodo para receber inputs do teclado
screen.listen()

#faz a chamada das funcoes que vao agir sobre a cobra dependendo dos inputs
screen.onkey(cobra.cima,'Up')
screen.onkey(cobra.baixo,'Down')
screen.onkey(cobra.esquerda,'Left')
screen.onkey(cobra.direita,'Right')

#variavel flag para controlar o status do jogo
jogoAtivo = True

#loop while para manter o jogo ativo
while jogoAtivo:
    #liga as animacoes da cobrinha para atualizar a tela
    screen.update()
    #time.sleep faz o programa ter uma lentidao
    time.sleep(0.1)
    #usa o metodo para mover a cobrinha
    cobra.moverCobraFrente()

    placar.escrever()

    #detectar colisao com a comida
    #distance checa a distancia entre um objeto turtle e outro
    #se a distancia entre a cabeca da cobra e a comida for menor que 15, certeza que houve colisao
    if cobra.cabeca.distance(comida) < 15:
        comida.resetar()


    
 
   
#faz com que a tela desapareca ao clicar
screen.exitonclick()