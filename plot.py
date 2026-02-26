import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")
df = pd.read_csv("centrifuge_data.csv")

# 1. Calculate the exact ratio you asked for
# Symmetric = Total Valid - Asymmetric
df['symmetric'] = df['valid_total'] - df['asymmetric']

# Avoid division by zero (though symmetric count is rarely 0 for N>1)
df = df[df['symmetric'] > 0]

# The Ratio: Asymmetric vs Symmetric
df['ratio'] = df['asymmetric'] / df['symmetric']

print(f"Plotting {len(df)} points...")

# 2. Setup the Plot
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))

# 3. Plot the simple line
# linewidth is set very thin (0.2) because with 1M points, 
# a thick line will just look like a solid block of color.
plt.plot(df['n'], df['ratio'], color='cyan', linewidth=0.2, label='Raw Ratio')

plt.title("Asymmetric vs. Symmetric Solutions (Raw Data)")
plt.xlabel("N (Number of Slots)")
plt.ylabel("Ratio (Asymmetric / Symmetric)")

# Set Y limit to ignore extreme outliers if necessary, 
# but usually this ratio stays below 1.0 for the centrifuge problem.
plt.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig("centrifuge_raw_line.png", dpi=300)
print("Saved to centrifuge_raw_line.png")
plt.show()
