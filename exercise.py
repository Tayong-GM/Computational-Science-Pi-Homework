from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP
from mpmath import mp
import matplotlib.pyplot as plt


#Set precision
mp.dps = 120
getcontext().prec = 120


# Get pi from mpmath lib
pi = Decimal(str(mp.pi))


# Decimal places to check

places = [20, 40, 60, 100]
truncated_values = []
rounded_values = []


#Compute truncated and rounded values
for p in places:
    getcontext().rounding = ROUND_DOWN
    truncated = pi.quantize(Decimal(f"1.{'0'*p}"))
    truncated_values.append(float(truncated))

    getcontext().rounding = ROUND_HALF_UP
    rounded = pi.quantize(Decimal(f"1.{'0'*p}"))
    rounded_values.append(float(rounded))

    print(f"\n{p} decimal places")
    print("Truncated:", truncated)
    print("Rounded  :", rounded)
    print("Difference:", abs(rounded - truncated))


# Side-by-side bar chart
import numpy as np

x = np.arange(len(places))
width = 0.35

plt.figure(figsize=(10,6))
plt.bar(x - width/2, truncated_values, width, label='Truncated', color='skyblue')
plt.bar(x + width/2, rounded_values, width, label='Rounded', color='red')

plt.xticks(x, places)
plt.xlabel("Decimal Places")
plt.ylabel("Value of π (approx)")
plt.title("Truncation vs Rounding of π at Different Decimal Places")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show(block=True)
