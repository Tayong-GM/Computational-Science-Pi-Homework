from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP
from mpmath import mp
import matplotlib.pyplot as plt
import numpy as np


# Precision settings
mp.dps = 120
getcontext().prec = 120


#Get high-precision pi
pi = Decimal(str(mp.pi))


# Sphere radius
r = Decimal(1)  # radius = 1 for simplicity

# True volume using full pi
true_volume = (Decimal(4) / Decimal(3)) * pi * (r ** 3)

# Decimal places to test
places = [20, 40, 60, 100]

truncated_volumes = []
rounded_volumes = []

print("TRUE VOLUME (high precision):")
print(true_volume)
print("-" * 60)


# Main loop
for p in places:
    mask = Decimal(f"1.{'0'*p}")

    # Truncation
    getcontext().rounding = ROUND_DOWN
    pi_trunc = pi.quantize(mask)
    vol_trunc = (Decimal(4) / Decimal(3)) * pi_trunc * (r ** 3)

    # Rounding
    getcontext().rounding = ROUND_HALF_UP
    pi_round = pi.quantize(mask)
    vol_round = (Decimal(4) / Decimal(3)) * pi_round * (r ** 3)

    truncated_volumes.append(float(vol_trunc))
    rounded_volumes.append(float(vol_round))

    print(f"\n{p} DECIMAL PLACES")
    print("π truncated :", pi_trunc)
    print("π rounded   :", pi_round)

    print("Volume (truncated):", vol_trunc)
    print("Volume (rounded)  :", vol_round)
    print("Difference        :", abs(vol_round - vol_trunc))

    print("Are volumes equal?:", vol_trunc == vol_round)

    print("Trunc vs true diff:", abs(true_volume - vol_trunc))
    print("Round vs true diff:", abs(true_volume - vol_round))


# Visualization for graph

x = np.arange(len(places))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, truncated_volumes, width, label="Truncated Volume", color="skyblue")
plt.bar(x + width/2, rounded_volumes, width, label="Rounded Volume", color="red")

plt.xticks(x, places)
plt.xlabel("Decimal Places of π")
plt.ylabel("Sphere Volume (r = 1)")
plt.title("Sphere Volume Using Truncated vs Rounded π")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
