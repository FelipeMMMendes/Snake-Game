#fazendo os imports necessarios
from turtle import Turtle

#a classe Placar herda da Turtle
class ScoreBoard(Turtle):
    #define o metodo construtor
    def __init__(self):
        #chama o metodo construtor da superclasse quando o construtor dessa classe for chamado
        super().__init__()
        self.placar = Turtle()
        self.placar.hideturtle()
        self.placar.penup()
        self.placar.color('white')
        self.escrever()
        

    def escrever(self):
        self.placar.goto(0,285)
        self.placar.write("Score: ",True,align='center')    
