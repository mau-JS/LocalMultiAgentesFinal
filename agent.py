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
        self.cantidad = 0

    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent1)):
                if(i.color == "red" or i.color == "yellow"):
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True
        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None
#Coche carril inferior a la izquierda
    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x + 1, y)):
            self.newPos = (x + 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
    def stop(self):
        x,y = self.pos
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def step(self):
        self.verificaSemaforo()
        #for i in self.celdasAlrededor:
        #    print(str(self.unique_id) +" "+ str(self.celdasAlrededor))
        #self.move()

#Coche se dirige izquierda
class CarAgent2(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "orange"
        self.moverStatus = None

    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent2)):
                if(i.color == "red" or i.color == "yellow"):
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True

        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None

    def stop(self):
        x,y = self.pos
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x - 1, y)):
            self.newPos = (x - 1 , y)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()

    def step(self):
        self.verificaSemaforo()


#Coche se dirige arriba
class CarAgent3(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "blue"
        self.moverStatus = None

    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent3)):
                if(i.color == "red" or i.color == "yellow"):
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True

        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None
            
    def stop(self):
        x,y = self.pos
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y + 1)):
            self.newPos = (x , y + 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
    def step(self):
        self.verificaSemaforo()

#Se dirige abajo carril derecho
class CarAgent4(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
        self.color = "black"
        self.moverStatus = None

    def verificaSemaforo(self):
        celdasAlrededor = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 2)
        for i in celdasAlrededor:
            if (isinstance(i, SemaforoAgent4)):
                if(i.color == "red" or i.color == "yellow"):
                    self.moverStatus = False
                    break
                elif(i.color == "green"):
                    self.moverStatus = True
                    break
            else: 
                self.moverStatus = True

        if self.moverStatus == True:
            self.move()
            self.moverStatus = None
        elif self.moverStatus == False:
            self.stop()
            self.moverStatus = None
        else:
            self.move()
            self.moverStatus = None
    def stop(self):
        x,y = self.pos
        self.newPos = (x , y)
        self.model.grid.move_agent(self,self.newPos)
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }
    def move(self):
        x,y = self.pos
        if self.model.grid.is_cell_empty((x, y - 1)):
            self.newPos = (x , y - 1)
            self.model.grid.move_agent(self,self.newPos)
            self.velocidadAgente = {
                "x": str(self.newPos[0] - x),
                "y": str(self.newPos[1] - y)
            }
        else:
            self.stop()
    def step(self):
        self.verificaSemaforo()

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