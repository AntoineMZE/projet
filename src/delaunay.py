import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

points = np.random.rand(177, 2)

tri = Delaunay(points)

# Visualize the triangulation
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

