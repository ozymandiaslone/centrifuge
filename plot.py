import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
print("Loading data...")
df = pd.read_csv("centrifuge_data.csv")

# 2. Calculate the specific ratio you asked for
# The CSV 'ratio' is (Asymmetric / Total). 
# If you specifically want (Asymmetric / Symmetric), we calculate it here:
# Symmetric count = (n + 1) - phi
symmetric_count = (df['n'] + 1) - df['phi']
df['asym_vs_sym_ratio'] = df['asymmetric'] / symmetric_count

# 3. Create a Simple Line (Rolling Average)
# We use a window of 50,000 to smooth out the noise of primes vs composite numbers.
# This reveals the true global trend.
WINDOW_SIZE = 50000 
print(f"Calculating {WINDOW_SIZE}-point rolling average...")

# Option A: Plot Asymmetric / Total (The "Market Share" of asymmetry)
df['trend_total'] = df['ratio'].rolling(window=WINDOW_SIZE).mean()

# Option B: Plot Asymmetric / Symmetric (Your specific request)
df['trend_vs_sym'] = df['asym_vs_sym_ratio'].rolling(window=WINDOW_SIZE).mean()

# 4. Plot
plt.style.use('dark_background')
plt.figure(figsize=(12, 6))

# Plotting Option A (Asymmetric % of Total). 
# Change to 'trend_vs_sym' if you strictly want Asymmetric/Symmetric.
plt.plot(df['n'], df['trend_total'], color='cyan', linewidth=2, label=f'Rolling Average (Window={WINDOW_SIZE})')

plt.title(f"Trend: Ratio of Asymmetric Solutions (N={df['n'].max()})")
plt.xlabel("N (Number of Slots)")
plt.ylabel("Average Ratio (Asymmetric / Total Valid)")
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig("centrifuge_trend.png")
print("Saved simple line plot to 'centrifuge_trend.png'")
plt.show()
