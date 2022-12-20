#fazendo os imports necessarios
from turtle import Turtle

#lista flag auxiliar no momento de colocar a cobra inicial
posicoesIniciais = [(0,0),(-20,0),(-40,0)]

#variavel auxiliar para controlar a distancia de movimento da cobrinha
DIST_MOVIMENTO = 20

#variaveis para auxiliar na movimentacao correta da cobra
CIMA = 90
BAIXO = 270
ESQUERDA = 180
DIREITA = 0

class Snake():
    def __init__(self):
        #lista flag para auxiliar na movimentacao da cobra
        self.segmentosCobra = []
        #chama a funcao de criar a cobra assim que instanciar o objeto
        self.criarCobra()
        #variavel auxiliar para guardar a cabeca da cobra
        self.cabeca = self.segmentosCobra[0] 

    def criarCobra(self):
        #loop para instanciar o resto da cobra
        for pos in posicoesIniciais:
            self.adicionarSegmento(pos)

    #funcao para adicionar um segmento na cobra
    def adicionarSegmento(self,pos):
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
            
    #funcao para aumentar o tamanho da cobra
    def extenderCobra(self):
        #pega a posicao do ultimo segmento e acrescenta mais uma parte a partir dele
        self.adicionarSegmento(self.segmentosCobra[-1].position())




    def moverCobraFrente(self):
        #percorre as partes do corpo da cobra, do ultimo ao primeiro
        for num_parte in range(len(self.segmentosCobra) - 1,0,-1):
            #armazena os valores de X e Y da parte que esta depois da que o loop se encontra
            novoX = self.segmentosCobra[num_parte-1].xcor()
            novoY = self.segmentosCobra[num_parte-1].ycor()

            #manda o segmento atual ir para a posicao do proximo
            self.segmentosCobra[num_parte].goto(novoX,novoY)
        #move o primeiro segmento    
        self.cabeca.forward(DIST_MOVIMENTO)

    def cima(self):
        #checa a direcao que a cabeca esta indo para ver se o movimento eh permitido
        if self.cabeca.heading() != BAIXO:
            #acessa a cabeca da cobra e muda a direcao dela para cima
            self.cabeca.setheading(CIMA)

    def baixo(self):
        #checa a direcao que a cabeca esta indo para ver se o movimento eh permitido
        if self.cabeca.heading() != CIMA:
            #acessa a cabeca da cobra e muda a direcao dela para baixo
            self.cabeca.setheading(BAIXO)

    def esquerda(self):
        #checa a direcao que a cabeca esta indo para ver se o movimento eh permitido
        if self.cabeca.heading() != DIREITA:
            #acessa a cabeca da cobra e muda a direcao dela para esquerda
            self.cabeca.setheading(ESQUERDA)

    def direita(self):
        #checa a direcao que a cabeca esta indo para ver se o movimento eh permitido
        if self.cabeca.heading() != ESQUERDA:
            #acessa a cabeca da cobra e muda a direcao dela para direita
            self.cabeca.setheading(DIREITA)                   

