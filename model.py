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


        for i in range(self.numAgentsCar):
            a = random.choice(self.clases)("C" + str(i),self)
            self.schedule.add(a)
            x,y = vec[i]
            self.grid.place_agent(a,(x,y))
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}
        )

        s1 = SemaforoAgent1("S" + str(1),self)
        self.schedule.add(s1)
        x1 = 20
        y1 = 29
        self.grid.place_agent(s1,(x1,y1))

    def step(self):
        posicionStep = []
        self.datacollector.collect(self)
        self.schedule.step()
        for i in self.schedule.agents:
            if(isinstance(i,CarAgent1) or isinstance(i,CarAgent2) or isinstance(i,CarAgent3) or isinstance(i,CarAgent4)):
                posicionStep.append(i.velocidadAgente)
        posicionAgent.append(posicionStep)
        json_object = json.dumps(posicionAgent, indent = 4)

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)