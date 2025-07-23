# Import the matplotlib pyplot library for plotting
import matplotlib.pyplot as plt

# Define lists for x and y data points
x = [1, 2, 3, 4, 5, 6, 7, 8]  # List of x-axis values
y = [2, 7, 9, 1, 5, 10, 3, 4]  # List of corresponding y-axis values

# Create a scatter plot with these data points
plt.scatter(x, y)  # Plots each data point as a circle on the specified coordinates

# Add labels to the x and y axes for clarity
plt.xlabel('x-axis')  # Label for the horizontal axis
plt.ylabel('y-axis')  # Label for the vertical axis

# Add a descriptive title to the plot
plt.title('Scattered Graph')  # Identifies the purpose of the plot

# Display the plot for user interaction
plt.show()  # Makes the plot visible
