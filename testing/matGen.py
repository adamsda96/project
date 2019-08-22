

f = open("material.mat","w")

f.write("8 5 5 55 115 115 65 10\n")

startx = 30
starty = 30
startz = 50

endx = 90
endy = 90
endz = 70

n = 2

props = ["5 1 0 2.0598e+16 2.2876e+14 5.2306 -0.51202 2.2694e+15 3.2867e+14 5.2704 0.42503 2.4668e+15 1.7731e+15","1 1 1 0 0"]
for i in range(n):
    xpos1 = str(startx + i*(endx - startx)/n)
    xpos2 = str(startx + (i+1)*(endx - startx)/n)
    for t in range(n):
        ypos1 = str(starty + t*(endy - starty)/n)
        ypos2 = str(starty + (t+1)*(endy - starty)/n)
       
        prop = props[(i+t)%len(props)]

        f.write("8 " + xpos1 + " " + ypos1 +" " + str(startz) + " " + xpos2 + " " + ypos2 + " "  + str(endz) + " " + prop + "\n")
