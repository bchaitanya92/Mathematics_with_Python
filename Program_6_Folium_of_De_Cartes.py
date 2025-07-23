from sympy import plot_implicit, symbols, Eq

# Define symbolic variables
x, y = symbols('x, y')

# Define the parameter for the equation
a = 3

# Create the implicit equation using sympy's Eq class and addition
# x^3 + y^3 = 3axy

p1 = plot_implicit(
    Eq(x**3 + y**3, 3 * a * x * y),  # Equation to plot
    (x, -5, 5),  # Range for x-axis (-5 to 5)
    (y, -5, 5),  # Range for y-axis (-5 to 5)
    title='folium of De cartes:$x^3+y^3=3axy$',  # Title with the equation and name ("folium of De cartes")
)

# Display the plot
p1.show()
