import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2
def g(x):
    return np.sin(x)
def t(x):
    return np.cos(x)
def r(x):
    return np.log(x)
x = np.linspace(1, 10, 100)
y = f(x) # Note that it all gets transformed by the function f
y1 = g(x)
y2 = t(x)
y3 = r(x)

# Graphing a plot without setting a figure object.
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('test')

# plt.show()

a = np.arange(0,10)
b = a * 2
# Graphing using a figure object:
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x, y)
axes.set_title('x and y axis')
axes.set_xlabel('x')
axes.set_ylabel('y = x^2')
# Show x and y axes
axes.axhline(0, color='black', linewidth=0.5, linestyle='--')  # x-axis
axes.axvline(0, color='black', linewidth=0.5, linestyle='--')  # y-axis

# Optionally set limits for better visibility
axes.set_xlim(min(a) - 1, max(a) + 1)
axes.set_ylim(min(b) - 1, max(b) + 1)

# Showing the ticks of x and y axis
axes.set_xticks(np.arange(min(a), max(a) + 1, 1))
axes.set_yticks(np.arange(min(b), max(b) + 1, 1))
axes.fill_between(x, y, color='lightblue', alpha=0.5)
# axes.legend()
# plt.show()

# Saving the figure, using bound box to make sure the axis are visible.
fig.savefig('new_graph.png', bbox_inches='tight')

fig_sub, axes = plt.subplots(2,2)

fig_sub.suptitle('4 Basic Graphs')

axes[0][0].plot(x, y)

axes[1][0].plot(x, y1)

axes[0][1].plot(x, y2)

axes[1][1].plot(x, y3)

fig_sub.savefig('subplot.png', bbox_inches = 'tight')


# Plotting a 3-d Graph
a = np.arange(-5, 5, 0.25)
b = a
a, b = np.meshgrid(a, b)
z = np.sqrt(a**2 + b**2)

fig3_d, axes = plt.subplots(subplot_kw={"projection": "3d"})

axes.plot_surface(a, b, z)

fig3_d.savefig('3d_surface.png', bbox_inches = 'tight')

