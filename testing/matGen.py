

f = open("material.mat","w")

f.write("8 5 5 55 115 115 65 10\n")

startx = 30
starty = 30
startz = 50

endx = 90
endy = 90
endz = 70

n = 1

props = ["8 30 30 50 90 90 70 1 1 1 0 0"]
for i in range(n):
    xpos1 = str(startx + i*(endx - startx)/n)
    xpos2 = str(startx + (i+1)*(endx - startx)/n)
    for t in range(n):
        ypos1 = str(starty + t*(endy - starty)/n)
        ypos2 = str(starty + (t+1)*(endy - starty)/n)
       
        prop = props[(i+t)%len(props)]

        f.write("8 " + xpos1 + " " + ypos1 +" " + str(startz) + " " + xpos2 + " " + ypos2 + " "  + str(endz) + " " + prop + "\n")

f.close()

f = open("test.par","w")
f.write("POOL\n120 120 120 3e-08 3e-08 3e-08 3-08\n\n")

f.write("COMP\n1200\n\n")

f.write("VERBOSE\n1\n\n")

f.write("GPU\n1\n\n")

f.write("UGPU\n0\n\n")

f.write("SOURCE_TSF\n5 5 5 115 115 0 0 0 2 5e-07 100 1\n\n")

f.write("TSF_SKIP\ni0\n\n")

f.write("TSF_SKIP\nin\n\n")

f.write("TSF_SKIP\nj0\n\n")

f.write("BOUNDARY_ALL\nliao\n\n")

f.write("MBOUNDARY_X0\nperiodic 10\n\n")

f.write("MBOUNDARY_XN\nperiadic 110\n\n")

f.write("MBOUNDARY_Y0\nperiodic 10\n\n")

f.write("MBOUNDARY_YN\nperiodic 110\n\n")

f.write("MEDIUM_VECTOR\nmaterial.mat\n\n")

f.write("OUT_FILE\nout.gwy\n\n")

f.write("OUT_IMAGE\nEy 200 -1 -1 ey_yz\n\n")

f.write("OUT_IMAGE\nEy 200 -1 60 -1 ey_xz\n\n")

f.write("OUT_IMAGE\nEY 200 -1 -1 60 ey_xy\n\n")

f.write("OUT_IMAGE\n Ey 200 -1 -1 80 ey_xy_2\n\n")

f.write("PERIODIC_NFFF\n10 10 10 110 110 110 -1 -1 2 2\n\n")

f.write("PERIODIC_NFFF_SPHERICAL_AREA\n60 74 10000 0 0 1.5708 6.28319 0")
