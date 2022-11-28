import numpy as np
import mesa
import random
import matplotlib
import pandas as pd
import json


#Coche carril superior a la derecha
class CarAgent1(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "purple"
        self.moverStatus = None
    

    def verificaSemaforo(self):
        self.moverStatus = None
        celdasAlrededor = self.model.grid.get_neighborhood(self.pos, moore = True, include_center = False, radius = 2)

        for i in celdasAlrededor:
            contenidoCelda = self.model.grid.get_cell_list_contents(i)
            if(isinstance(contenidoCelda,SemaforoAgent1)):
                if(contenidoCelda.color == "red"):
                    moverStatus = False
                    break
                elif(contenidoCelda.color == "yellow" or contenidoCelda.color == "green"):
                    moverStatus = True
                    break
            else:
                moverStatus = True
        if moverStatus == True:
                self.move()
#Coche carril inferior a la izquierda
    def move(self):
        x,y = self.pos
        self.newPos = (x + 1 , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def step(self):
        self.move()

#Coche se dirige izquierda
class CarAgent2(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "orange"
    def move(self):
        x,y = self.pos
        self.newPos = (x - 1, y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def step(self):
        self.move()


#Coche se dirige arriba
class CarAgent3(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "blue"
    def move(self):
        x,y = self.pos
        self.newPos = (x, y + 1)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def step(self):
        self.move()

#Se dirige abajo carril derecho
class CarAgent4(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "black"
    def move(self):
        x,y = self.pos
        self.newPos = (x, y-1)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def step(self):
        self.move()

class SemaforoAgent1(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "green"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
    def step(self):
        self.change()

class SemaforoAgent2(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "green"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
    def step(self):
        self.change()

class SemaforoAgent3(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "red"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
    def step(self):
        self.change()

class SemaforoAgent4(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "red"
        self.tiempo = 13
    def change(self):
        self.tiempo -= 1
        if (self.tiempo == 3 and self.color == "green"):
            self.color = "yellow"
        elif(self.tiempo == 0 and self.color == "red"):
            self.color = "green"
            self.tiempo = 10
        elif(self.tiempo == 0 and self.color == "yellow"):
            self.color = "red"
            self.tiempo = 10
    def step(self):
        self.change()

class entornoAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "black"
    def step(self):
        pass