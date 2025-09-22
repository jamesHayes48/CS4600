from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

def function(x,y):
    return x**3 + y**3 - 3*x*y

# e. Graphical Estimation
# Graph 3D surface plot of f(x,y)
x_list = np.linspace(-2, 2, 100)
y_list = np.linspace(-2, 2, 100)

X,Y = np.meshgrid(x_list, y_list)
Z = function(X, Y)

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z,)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
