import math
from matGen import matGen
class parGen:

    def __init__(self, sz=3.6*math.pow(10,-6), gpu=1, matFile="material.mat", fileName="test.par",dim=120,defDim=120,outFile="out.gwy"):
        self.sz = sz
        self.matFile = matFile
        self.name = fileName
        self.gpu = gpu
        self.dim = float(dim)
        self.defDim = float(defDim)
        self.outFile = outFile
    
    def getName(self):
        return self.name
    
    def genMat(self,nx=1,ny=1,nz=1):
        mat = matGen(self.dim,self.defDim,self.matFile,nx,ny,nz)
        mat.generate()

    def generate(self,nx=1,ny=1,nz=1):
        
        self.genMat(nx,ny,nz)

        f = open(self.name,"w")
        f.write("POOL\n"+(str(self.dim) +" ")*3+(str(self.sz/self.dim)+" ")*3+"\n\n")

        f.write("COMP\n1200\n\n")

        f.write("VERBOSE\n1\n\n")

        f.write("THREADS\n-1\n\n")

        f.write("GPU\n"+str(self.gpu)+"\n\n")

        f.write("UGPU\n0\n\n")

        f.write("SOURCE_TSF\n"+ (str(5/self.defDim*self.dim)+" ") * 2 + str(105/self.defDim*self.dim) + " " +(str(115/self.defDim*self.dim)+" ")*3 + "0 0 0 2 5e-07 100 1\n\n")

        f.write("TSF_SKIP\ni0\n\n")

        f.write("TSF_SKIP\nin\n\n")

        f.write("TSF_SKIP\nj0\n\n")

        f.write("TSF_SKIP\njn\n\n")

        f.write("BOUNDARY_ALL\nliao\n\n")

        f.write("MBOUNDARY_X0\nperiodic "+str(10/self.defDim*self.dim)+"\n\n")

        f.write("MBOUNDARY_XN\nperiodic "+str(110/self.defDim*self.dim)+"\n\n")

        f.write("MBOUNDARY_Y0\nperiodic "+str(10/self.defDim*self.dim)+"\n\n")

        f.write("MBOUNDARY_YN\nperiodic "+str(110/self.defDim*self.dim)+"\n\n")

        f.write("MEDIUM_VECTOR\n"+self.matFile+"\n\n")

        f.write("OUT_FILE\n"+self.outFile+"\n\n")

        f.write("OUT_IMAGE\nEy 200 -1 "+str(60/self.defDim*self.dim)+" -1 ey_xz\n\n")

        f.write("OUT_PLANE\nEy 10 60 250 0 -1 " +str(60/self.defDim*self.dim)+" -1 movieOut\n\n") 

        f.write("PERIODIC_NFFF\n "+(str(10/self.defDim*self.dim)+" ")*3 + (str(110/self.defDim*self.dim) + " ") * 3 +"-1 -1 2 2\n\n")

        f.write("PERIODIC_NFFF_SPHERICAL_AREA\n"+str(60/self.defDim*self.dim)+" "+ str(74/self.defDim*self.dim) + " " + str(10000/self.defDim*self.dim)+" 0 0 1.5708 6.28319 0")
