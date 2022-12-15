#fazendo os imports necessarios
from turtle import Turtle

#lista flag auxiliar no momento de colocar a cobra inicial
posicoesIniciais = [(0,0),(-20,0),(-40,0)]

#variavel auxiliar para controlar a distancia de movimento da cobrinha
DIST_MOVIMENTO = 20

class Snake():
    def __init__(self):
        #lista flag para auxiliar na movimentacao da cobra
        self.segmentosCobra = []
        self.criarCobra()

    def criarCobra(self):

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
            self.segmentosCobra.append(cobra)    


    def moverCobra(self):
        #percorre as partes do corpo da cobra, do ultimo ao primeiro
        for num_parte in range(len(self.segmentosCobra) - 1,0,-1):
            #armazena os valores de X e Y da parte que esta depois da que o loop se encontra
            novoX = self.segmentosCobra[num_parte-1].xcor()
            novoY = self.segmentosCobra[num_parte-1].ycor()

            #manda o segmento atual ir para a posicao do proximo
            self.segmentosCobra[num_parte].goto(novoX,novoY)
        self.segmentosCobra[0].forward(DIST_MOVIMENTO)
