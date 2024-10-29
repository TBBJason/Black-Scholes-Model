import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

x, y = np.meshgrid(x,y)

# print(x)
# print(y)
def func(x, y):
    return np.sin(np.sqrt((x**2 + y**2)))
z = func(x,y)

fig, axes = plt.subplots(subplot_kw={"projection" : "3d"})
axes.plot_surface(x, y, z, cmap='plasma')
plt.show()

xlist = []
ylist = []
zlist = []

# Saving an animation as a gif using the PillowWriter object

metadata = dict(title='Movie', artist='codinglikemad')
writer = PillowWriter(fps=15, metadata=metadata)

# Since we're working with a 3-d graph, updating the z-value is different:
def update(frame):
    axes.clear() # Clears the previous graph that was the previous frame
    z = func(x + frame * 0.1,y + frame * 0.1) # update z based on frame
    surf = axes.plot_surface(x, y, z, cmap = 'plasma')
    axes.set_zlim(-1,1) # Maintain z limit

# The function that saves the gif
with writer.saving(fig,"Finance Learning/Graphs and Gifs/3d-Animation.gif", 100):
    for xval in range(30):
        update(xval)

        writer.grab_frame()

plt.show()