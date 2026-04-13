import matplotlib.pyplot as plt

# Data points from the user's screenshot
x = [10, 20, 30, 40, 50, 60, 70, 80]
y = [20, 10, 32, 30, 38, 19, 44, 55]

plt.figure(figsize=(10, 7))
plt.scatter(x, y, color='#4472c4', s=100)

# Formatting to match the look of the screenshot (Excel-style)
plt.xlabel('Variable X', fontweight='bold', color='#475569')
plt.ylabel('Variable Y', fontweight='bold', color='#475569')
plt.grid(True, linestyle='-', color='#e2e8f0')
plt.xlim(0, 90)
plt.ylim(0, 60)
plt.xticks(range(0, 91, 10))
plt.yticks(range(0, 61, 10))

# Clean up spines
for spine in plt.gca().spines.values():
    spine.set_color('#cbd5e1')

plt.tight_layout()
plt.savefig('c:/Users/kj anand/Downloads/Quiz DD/correlation_scatter.png', dpi=300)
print("Image saved successfully.")
