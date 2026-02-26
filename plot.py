import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
print("Loading CSV... (this might take a moment for large files)")
try:
    df = pd.read_csv("centrifuge_data.csv")
except FileNotFoundError:
    print("Error: 'centrifuge_data.csv' not found. Run the Rust program first!")
    exit()

# Filter out rows where ratio is 0 to make the graph cleaner
# (Ratio 0 means the number is a prime power or has < 2 distinct factors)
df_filtered = df[df['ratio'] > 0]

print(f"Loaded {len(df)} records. Plotting {len(df_filtered)} non-zero records...")

# 2. Setup the Plot
plt.style.use('dark_background') # Looks better for dense mathematical scatter plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# --- PLOT 1: The Ratio (The "Ghost" Pattern) ---
# This shows Asymmetric / Total Valid. 
# You should see horizontal bands corresponding to specific prime factor families.
ax1.scatter(
    df_filtered['n'], 
    df_filtered['ratio'], 
    s=0.5,          # Pixel size (keep small!)
    c='cyan',       # Color
    alpha=0.1,      # Transparency (0.1 = 10% opaque). Essential for 1M points.
    linewidths=0    # No border on dots
)
ax1.set_ylabel("Asymmetry Ratio")
ax1.set_title(f"Centrifuge Problem: Asymmetry Ratio (N={df['n'].max()})")
ax1.grid(True, which='both', linestyle='--', linewidth=0.3, alpha=0.3)

# --- PLOT 2: Raw Asymmetric Count ---
# This shows the raw number of 'surprise' solutions.
# You will likely see parabolic shapes or linear growth trends.
ax2.scatter(
    df_filtered['n'], 
    df_filtered['asymmetric'], 
    s=0.5, 
    c='lime', 
    alpha=0.1,
    linewidths=0
)
ax2.set_xlabel("N (Number of Slots)")
ax2.set_ylabel("Count of Asymmetric Solutions")
ax2.grid(True, which='both', linestyle='--', linewidth=0.3, alpha=0.3)

# 3. Save and Show
plt.tight_layout()
output_filename = "centrifuge_analysis.png"
plt.savefig(output_filename, dpi=300)
print(f"Plot saved to {output_filename}")
plt.show()
