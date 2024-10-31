import matplotlib.pyplot as plt
import numpy as np


class FunctionPlotter:
    def __init__(self, func, x_range=(-5,5), y_range=(-5,5), step=0.1):
        self.func = func
        self.X, self.Y = np.arange(x_range[0], x_range[1], step),  np.arange(y_range[0],y_range[1], step)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        self.step = step
        self.Z = self.calculate_z()

    def calculate_z(self):
        Z = np.zeros_like(self.X)
        # Avoid division by zero using np.where
        # mask = (self.X != 0) | (self.Y != 0) # mask for x and y not both zero
        Z = self.func(self.X, self.Y)
        return Z
    def plot(self, filename="quickgraph.png"):
        fig, axes = plt.subplots(subplot_kw={"projection":"3d"})
        axes.plot_surface(self.X, self.Y, self.Z, cmap='plasma')

        fig.savefig(f"FinanceLearning/Graphs and Gifs/{filename}", bbox_inches='tight')

def example_function(x,y):
    return (x**2 + y**2)

if __name__ == "__main__":
    plotter = FunctionPlotter(example_function)
    plotter.plot()



    # # Piecewise function with (x,y) = (0,0) = 0

# X = np.arange(-5, 5, 0.1)
# Y = np.arange(-5,5,.1)

# X, Y = np.meshgrid(X,Y)

# def func(x,y):
#     Z = np.zeros_like(x)
#     # Avoid division by zero using np.where
#     mask = (x != 0) | (y != 0) #This is where x and y are both not 0
#     Z[mask] = (x[mask]**3 * y[mask]) / (x[mask]**6 + y[mask]**2)
#     return Z

# Piecewise = func(X,Y)





# # Plotting out the Function
# fig, axes = plt.subplots(subplot_kw={"projection":"3d"})
# axes.plot_surface(X,Y,Piecewise, cmap='plasma')
# fig.savefig("FinanceLearning/Graphs and Gifs/quickgraph.png", bbox_inches='tight')

# # Setting the top down view
# axes.view_init(elev=90,azim=0)
# plt.show()