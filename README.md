# Computational-Science-Pi-Homework

This program demonstrates how truncation and rounding affect the numerical value of the mathematical constant π when it is represented with different numbers of decimal places. The code computes truncated and rounded versions of π at 20, 40, 60, and 100 decimal places. It then calculates the difference between these two methods and visualizes the results using a bar graph.
 
GRAPTH OUTPUT:
<img width="1257" height="833" alt="Screenshot 2026-02-09 112940" src="https://github.com/user-attachments/assets/56c33281-eced-4000-9e62-a135c81eb293" />

TERMINAL OUTPUT:
<img width="1073" height="556" alt="Screenshot 2026-02-09 114104" src="https://github.com/user-attachments/assets/0bd6bd05-38e7-4954-8c85-278aea07fc16" />

Summary of Findings

The results show that the difference between truncation and rounding becomes extremely small as the number of decimal places increases. The maximum possible difference at each precision level is equal to 
10^−𝑝, where 𝑝 is the number of decimal places. Because these differences are very close to zero (for example, 1×10^−100), they are not easily visible on the graph. This demonstrates that while truncation and rounding are mathematically different processes, their numerical impact on π becomes negligible at very high precision.
