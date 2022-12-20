#fazendo os imports necessarios
from turtle import Turtle
#a classe Placar herda da Turtle
class ScoreBoard(Turtle):
    
    #define o metodo construtor
    def __init__(self):
        #chama o metodo construtor da superclasse quando o construtor dessa classe for chamado
        super().__init__()
        self.placar = Turtle()
        #esconde a tartaruga
        self.placar.hideturtle()
        #faz com que a tartaruga nao deixe uma linha ao se mover
        self.placar.penup()
        #coloca a cor para branco
        self.placar.color('white')
        #variavel auxiliar para armazenar o score
        self.pontuacao = 0
        #chama o metodo para colocar na tela a pontuacao
        self.escrever()
        
    def escrever(self):
        #joga a cobra para a posicao correta para escrever o score
        self.placar.goto(0,285)
        #escreve na tela a pontuacao
        self.placar.write(f"Pontuacao: {self.pontuacao} ",True,align='center',font=('bahnschrift', 10, 'normal'))

    def aumentarPontuacao(self):
        self.placar.clear()
        self.pontuacao += 1        
