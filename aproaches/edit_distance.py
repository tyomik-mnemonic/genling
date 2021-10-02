import numpy as np

class JaroDist:

    def __init__(w1:str, w2:str):
        self.w1 = w1
        self.w2 = w2
        self.m:list = None
        self.t:int = None

    def compare(self):
        for w,wo in zip(w1,w2):
            self.m.append(1) if w == wo else self.m.append(0)

        self.t = sum(self.m)/2

        #dj = 1/3*(sum(self.m)/max(w1,w2) + sum(self.m)/max(w1,w2) + (sum(self.m) - self.t)/m if sum(self.m)/2>0 else: 0