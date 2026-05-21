import matplotlib.pyplot as plt

# Create canvas
plt.figure(figsize=(10, 6))

# Background color
plt.gca().set_facecolor("#1e1e2f")

# Title
plt.text(
    0.5, 0.6,
    "Student Management System",
    fontsize=32,
    color="white",
    ha="center",
    va="center",
    weight="bold"
)

# Subtitle
plt.text(
    0.5, 0.45,
    "Python Console Application",
    fontsize=16,
    color="#cfcfcf",
    ha="center"
)

# Footer
plt.text(
    0.5, 0.15,
    "Developed by Group X",
    fontsize=12,
    color="#aaaaaa",
    ha="center"
)

# Remove axes
plt.axis("off")

# Save image
plt.savefig("project_background.png", dpi=300, bbox_inches="tight")
plt.show()
