#fazendo os imports necessarios
from turtle import Turtle
#a classe Placar herda da Turtle
class ScoreBoard(Turtle):
    
    #define o metodo construtor
    def __init__(self):
        #chama o metodo construtor da superclasse quando o construtor dessa classe for chamado
        super().__init__()
        #esconde a tartaruga
        self.hideturtle()
        #faz com que a tartaruga nao deixe uma linha ao se mover
        self.penup()
        #coloca a cor para branco
        self.color('white')
        #joga a cobra para a posicao correta para escrever o score
        self.goto(0,280)
        #variavel auxiliar para armazenar o score
        self.pontuacao = 0
        #chama o metodo para colocar na tela a pontuacao
        self.escrever()
        
    def escrever(self):
        #escreve na tela a pontuacao
        self.write(f"Pontuacao: {self.pontuacao} ",align='center',font=('bahnschrift', 10, 'normal'))

    def aumentarPontuacao(self):
        #aumenta a pontuacao em 1
        self.pontuacao += 1
        #limpa o que a tartaruga tinha escrito antes
        self.clear()
        #escreve novamente
        self.escrever()      
