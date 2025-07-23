from sympy import plot_implicit, symbols, Eq

# Define symbolic variables
x, y = symbols('x, y')

# Define the parameter for the equation
a = 3

# Define the implicit equation using sympy's Eq class and multiplication
# y^2(a-x) = x^2(a+x)

p1 = plot_implicit(
    Eq((y**2)*(a-x), (x**2)*(a+x)),  # Equation to plot
    (x, -5, 5),  # Range for x-axis (-5 to 5)
    (y, -5, 5),  # Range for y-axis (-5 to 5)
    title='strophoid:$y^2(a-x)=x^2(a+x)$'  # Title with the equation and its name
)

# Display the plot
p1.show()
