from turtle import Turtle
import random


class Food(Turtle):


    def __init__(self):
        super().__init__()
        # turtle tak jak red i fastest
        self.shape("turtle")
        self.penup()
        self.shapesize(0.7, 0.7)
        #red i fastest dodaj do zmiennych dla klasy, bo to są opcje konfiguracjyne
        self.color("red") 
        self.speed("fastest")
        # do usunięcia - używasz niżej refresh_food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        # 
        self.refresh_food()

        # zamiast refresh to lepsza chyba init bo za 1 razem nie odświeżasz tylko tworzysz
    def refresh_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
