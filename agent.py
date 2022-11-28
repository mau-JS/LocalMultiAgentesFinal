import numpy as np
import mesa
import random
import matplotlib
import pandas as pd
import json


#Coche se dirige derecha
class CarAgent1(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
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

#Se dirige abajo
class CarAgent3(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
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