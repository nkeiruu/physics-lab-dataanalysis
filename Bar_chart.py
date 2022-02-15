import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

xAxis = ["Malt Vinegar","Dandelion Root", "Baba Root", "White Vinegar"]
yAxis = [0.75, 2,1,1]

plt.bar(xAxis,yAxis, hatch = "*")
plt.title('Amount of time to dissolve in water')
plt.xlabel('Liquid')
plt.ylabel('Time (minutes)')
plt.show()