#fazendo os imports necessarios
from turtle import Turtle
import random

#Faz a classe Food ter heranca da classe Turtle
class Food(Turtle):
    
    #define o metodo construtor
    def __init__(self):
        #faz a chamada do metodo construtor da classe super (Turtle)
        super().__init__()
        #metodo da classe super, shape define o formato visual do objeto
        self.shape('circle')
        #metodo da classe super, penup serve para que o objeto nao desenhe na tela quando se move
        self.penup()
        #metodo da classe super para diminuirmos o tamanho visual do objeto
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        #metodo da classe super para mudarmos a cor
        self.color('red')
        #metodo da classe super para definirmos a velocidade da tartaruga para o maximo
        self.speed('fastest')
        self.resetar()

    #metodo auxiliar para jogar a comida para uma posicao toda vez que for chamado
    def resetar(self):            
        #variaveis auxiliares para definir as coordenadas em que a fruta vai aparecer
        #a tela eh de 600x600, ou seja, o eixo X e Y vao de -300 ate 300, nesse sentido, por fins de melhor
        #experiencia do usuario, vamos diminuir o tamanho para que a comida nao apareca tanto nas bordas da tela
        xFood = random.randint(-280,280)
        yFood = random.randint(-280,280)
        #metodo para mover a comida para tal posicao
        self.goto(xFood,yFood)