import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)

print(x)

print(type(x))

# Plot the data
plt.plot([1,2,4], [1,2,4], label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()