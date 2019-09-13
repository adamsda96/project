from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

f = open("yz_plane_0200","r")

lines = f.readlines()

y = range(0,len(lines))

x= range(0,len(lines))

z = []
for l in lines:
    string = l.strip().split()
    floats = [float(i) for i in string]
    print(floats)
    z.append(floats)

print(len(z))
print(len(z[0]))
print(len(y))
print(len(x))
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(y,x,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('voltage')

plt.show()
