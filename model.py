import numpy as np
import mesa
import random
import matplotlib
import pandas as pd
from agent import *

vec = []
posicionAgent = []
posicionStep = []
def compute_gini(model):
    return 5
class CarModel(mesa.Model):
    def __init__(self,N,width,height):
        global vec
        self.numAgentsCar = N
        for i in range (self.numAgentsCar):
            vec.append(random.sample(range(0, 50), 2))

        self.grid = mesa.space.MultiGrid(width,height,True)
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True
        self.clases = (CarAgent1,CarAgent2,CarAgent3)
        
        for i in range(self.numAgentsCar):
            a = random.choice(self.clases)(i,self)
            self.schedule.add(a)
            x,y = vec[i]
            self.grid.place_agent(a,(x,y))

        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}
        )
    def step(self):
        posicionStep = []
        self.datacollector.collect(self)
        self.schedule.step()
        for i in self.schedule.agents:
            posicionStep.append(i.velocidadAgente)
        posicionAgent.append(posicionStep)
        json_object = json.dumps(posicionAgent, indent = 4)

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)