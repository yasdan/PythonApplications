"from turtle import *"
from turtle import Turtle

class TurtleDemos:
    
    def __init__(self):
        pass

    def turtle_square(self):
        tom = Turtle()
        tom.color('orange')
        tom.shape('triangle')

        for i in range(4):
            tom.left(90)
            tom.forward(200)

        tom.screen.title('Turtle Demo')
        tom.screen.bgcolor('#339588')
        tom.screen.mainloop()
        

    

    def turtle_circle(self, radius):
        tircle = Turtle()
        tircle.color('blue')
        tircle.shape('turtle')
        tircle.circle(radius)

        tircle.screen.title('Turtle Demo')
        tircle.screen.bgcolor('#339588')
        tircle.screen.mainloop()


    



