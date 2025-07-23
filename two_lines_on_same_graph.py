# Import the matplotlib.pyplot library for plotting
import matplotlib.pyplot as plt

# Define the x and y values for the first line (line 1)
x1 = [1, 2, 3]
y1 = [2, 4, 1]

# Create a line plot for the first line with a label
plt.plot(x1, y1, label='line 1')

# Define the x and y values for the second line (line 2)
x2 = [1, 2, 3]
y2 = [4, 1, 3]

# Create a line plot for the second line with a different label
plt.plot(x2, y2, label='line 2')

# Add labels for the x and y axes for clarity
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title to the plot for identification
plt.title('Two lines on the same graph')

# Display the legend for distinguishing the lines
plt.legend()

# Display the plot for the user to see
plt.show()
