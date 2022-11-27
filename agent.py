import numpy as np
import mesa
import random
import matplotlib
import pandas as pd
import json



class CarAgent1(mesa.Agent):
    global vectorPosiciones
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nombre = unique_id
    def move(self):
        x,y = self.pos
        self.newPos = (x + 3 ,y + 5)
        self.model.grid.move_agent(self,(x + 3,y + 5))
        self.velocidadAgente = {
            "x": str(self.newPos[0] - x),
            "y": str(self.newPos[1] - y)
            }

    def step(self):
        self.move()