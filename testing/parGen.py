class parGen:

    def __init__(self, sz, gpu, matFile, fileName):
        self.sz = sz
        self.matFile = matFile
        self.name = fileName
        self.gpu = gpu
    
    def getName(self):
        return self.name

    def generate(self):


        f = open(self.name,"w")
        f.write("POOL\n120 120 120 "+self.sz+"\n\n")

        f.write("COMP\n1200\n\n")

        f.write("VERBOSE\n1\n\n")

        f.write("THREADS\n-1\n\n")

        f.write("GPU\n"+self.gpu+"\n\n")

        f.write("UGPU\n0\n\n")

        f.write("SOURCE_TSF\n5 5 5 115 115 115 0 0 0 2 5e-07 100 1\n\n")

        f.write("TSF_SKIP\ni0\n\n")

        f.write("TSF_SKIP\nin\n\n")

        f.write("TSF_SKIP\nj0\n\n")

        f.write("TSF_SKIP\njn\n\n")

        f.write("BOUNDARY_ALL\nliao\n\n")

        f.write("MBOUNDARY_X0\nperiodic 10\n\n")

        f.write("MBOUNDARY_XN\nperiodic 110\n\n")

        f.write("MBOUNDARY_Y0\nperiodic 10\n\n")

        f.write("MBOUNDARY_YN\nperiodic 110\n\n")

        f.write("MEDIUM_VECTOR\n"+self.matFile+"\n\n")

        f.write("OUT_FILE\nout.gwy\n\n")

        f.write("OUT_IMAGE\nEy 200 60 -1 -1 ey_yz\n\n")

        f.write("OUT_IMAGE\nEy 200 -1 60 -1 ey_xz\n\n")

        f.write("OUT_IMAGE\nEy 200 -1 -1 60 ey_xy\n\n")

        f.write("OUT_IMAGE\nEy 200 -1 -1 80 ey_xy_2\n\n")

        f.write("PERIODIC_NFFF\n10 10 10 110 110 110 -1 -1 2 2\n\n")

        f.write("PERIODIC_NFFF_SPHERICAL_AREA\n60 74 10000 0 0 1.5708 6.28319 0")
