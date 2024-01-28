import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def function1(n):
    return 10 * n**4 + 7 * n**2 + 3 * n

def function2(n):
    return 20 * n**4

# Generate n values
n_values = np.linspace(0, 10, 100)  # Adjust the range and number of points as needed

# Calculate function values
y_values1 = function1(n_values)
y_values2 = function2(n_values)

# Plot the functions
plt.plot(n_values, y_values1, label=r'$10n^4 + 7n^2 + 3n$')
plt.plot(n_values, y_values2, label=r'$20n^4$')

# Add labels and title
plt.xlabel('n')
plt.ylabel('Function Value')
plt.title('Plot of $10n^4 + 7n^2 + 3n$ and $20n^4$')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()