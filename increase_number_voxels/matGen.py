import os

class matGen:
    def __init__(self, dim = 120,defDim = 120, matFile="material.mat",n=1):
        self.dim = float(dim)
        self.defDim = float(defDim)
        self.matFile = matFile
        self.n = n

    def generate(self):
        f = open(self.matFile,"w")

        f.write("8  " + str(5/self.defDim*self.dim) +" " +str(5/self.defDim*self.dim) + " " +str(55/self.defDim*self.dim) + " " + (str(115/self.defDim*self.dim) + " ")*2 +str(65/self.defDim*self.dim) +" 10\n")

        startx = 30/self.defDim*self.dim
        starty = 30/self.defDim*self.dim
        startz = 50/self.defDim*self.dim

        endx = 90/self.defDim*self.dim
        endy = 90/self.defDim*self.dim
        endz = 70/self.defDim*self.dim

        n = self.n

        props = ["1 1 1 0 0"]
        for i in range(n):
            xpos1 = str(startx + i*(endx - startx)/n)
            xpos2 = str(startx + (i+1)*(endx - startx)/n)
            for t in range(n):
                ypos1 = str(starty + t*(endy - starty)/n)
                ypos2 = str(starty + (t+1)*(endy - starty)/n)
       
                prop = props[(i+t)%len(props)]

                f.write("8 " + xpos1 + " " + ypos1 +" " + str(startz) + " " + xpos2 + " " + ypos2 + " "  + str(endz) + " " + prop + "\n")

        f.close()

