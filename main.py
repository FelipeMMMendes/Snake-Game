#fazendo os imports necessarios
from turtle import Turtle, Screen
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

#lista flag auxiliar no momento de colocar a cobra inicial
posicoesIniciais = [(0,0),(-20,0),(-40,0)]

#lista flag para auxiliar na movimentacao da cobra
segmentosCobra = []

#loop para instanciar o resto da cobra
for pos in posicoesIniciais:
    #instancia um objeto do tipo turtle
    cobra = Turtle(shape='square')
    #faz com que a cobra não deixe uma linha ao se mover
    cobra.penup()

    #muda a cor dela
    cobra.color('green')

    #estende o corpo da cobra
    cobra.setposition(pos)

    #adiciona o pedaco do corpo na lista
    segmentosCobra.append(cobra)

#variavel flag para controlar o status do jogo
jogoAtivo = True

#loop while para manter o jogo ativo
while jogoAtivo:
    #liga as animacoes da cobrinha para atualizar a tela
    screen.update()

    #time.sleep faz o programa ter uma lentidao
    time.sleep(0.1)

    #percorre as partes do corpo da cobra, do ultimo ao primeiro
    for num_parte in range(len(segmentosCobra) - 1,0,-1):
        #armazena os valores de X e Y da parte que esta depois da que o loop se encontra
        novoX = segmentosCobra[num_parte-1].xcor()
        novoY = segmentosCobra[num_parte-1].ycor()

        #manda o segmento atual ir para a posicao do proximo
        segmentosCobra[num_parte].goto(novoX,novoY)
    segmentosCobra[0].forward(20)
    segmentosCobra[0].left(90)


#faz com que a tela desapareca ao clicar
screen.exitonclick()