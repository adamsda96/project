import os

class matGen:
    def __init__(self, dim = 120,defDim = 120, matFile="material.mat",nx=1,ny=1,nz=1):
        self.dim = float(dim)
        self.defDim = float(defDim)
        self.matFile = matFile
        self.nx = nx
        self.ny = ny
        self.nz = nz

    def generate(self):
        f = open(self.matFile,"w")

        f.write("8  " + str(0/self.defDim*self.dim) +" " +str(0/self.defDim*self.dim) + " " +str(18/self.defDim*self.dim) + " " + (str(120/self.defDim*self.dim) + " ")*2 +str(102/self.defDim*self.dim) +" 10\n")

        startx = 45/self.defDim*self.dim
        starty = 58.75/self.defDim*self.dim
        startz = 45/self.defDim*self.dim

        endx = 75/self.defDim*self.dim
        endy = 61.2/self.defDim*self.dim
        endz = 75/self.defDim*self.dim

        props = ["1 1 1 0 0","1 1 1 0 0","1 1 1 0 0","1 1 1 0 0","99 Si_100"]
        
        nx = self.nx
        ny = self.ny
        nz = self.nz

        for i in range(nx):
            xpos1 = str(startx + i*(endx - startx)/nx)
            xpos2 = str(startx + (i+1)*(endx - startx)/nx)
            for t in range(ny):
                ypos1 = str(starty + t*(endy - starty)/ny)
                ypos2 = str(starty + (t+1)*(endy - starty)/ny)
                
                for j in range(nz):
                    zpos1 = str(startz + j*(endz - startz)/nz)
                    zpos2 = str(startz + (j+1)*(endz - startz)/nz)
       
                    prop = props[(i+t+j)%len(props)]

                    f.write("8 " + xpos1 + " " + ypos1 +" " + zpos1 + " " + xpos2 + " " + ypos2 + " "  + zpos2 + " " + prop + "\n")
        
        f.write("8 " + str(59.9/self.defDim*self.dim) + " " + str(58.8/self.defDim*self.dim) + " "  + str(75/self.defDim*self.dim) + " " + str(61.1/self.defDim*self.dim) + " " + str(62.2/self.defDim*self.dim) + " " + str(105/self.defDim*self.dim) + " 1 1 1 0 0\n")

        f.write("8 " + str(59.9/self.defDim*self.dim) + " " + str(58.8/self.defDim*self.dim) + " "  + str(15/self.defDim*self.dim) + " " + str(61.1/self.defDim*self.dim) + " " + str(62.2/self.defDim*self.dim) + " " + str(45/self.defDim*self.dim) + " 1 1 1 0 0")   

        f.close()

