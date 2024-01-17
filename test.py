import matplotlib.pyplot as plt
import numpy as np

# Define the strain and stress values
strain = np.linspace(0, 0.2, 100)
stress = 200 * strain

# Define the 0.1% proof stress
proof_stress = 0.001 * 200

# Create the figure and the axes
fig, ax = plt.subplots()

# Plot the stress-strain curve
ax.plot(strain, stress, label='Stress-Strain Curve')

# Plot the 0.1% proof stress
ax.axhline(y=proof_stress, color='r', linestyle='--', label='0.1% Proof Stress')

# Set the labels and the title
ax.set_xlabel('Strain')
ax.set_ylabel('Stress')
ax.set_title('Stress-Strain Diagram')

# Add a legend
ax.legend()

# Show the plot
plt.show()