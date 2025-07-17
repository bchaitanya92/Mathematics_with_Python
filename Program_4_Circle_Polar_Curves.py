# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Set the plot projection to polar coordinates
plt.axes(projection='polar')

# Define the radius and a range of angles
r = 5  # Radius of the circle
rads = np.arange(0, (2 * np.pi), 0.3)  # Angles covering a full circle with spacing of 0.3 radians

# Loop through each angle and plot a green dot at the corresponding radius
for i in rads:
    plt.polar(i, r, 'g.')  # Plots a green dot at each angle and radius

# Display the plot
plt.show()
