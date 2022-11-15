"""
16. Use the following data (load it as CSV file) for this exercise. Read this file using Pandas or NumPy or using
in-built matplotlib function.
a. Get total profit of all months and show line plot with the following Style properties
Generated line plot must include following Style properties:
    • Line Style dotted and Line-color should be blue
    • Show legend at the lower right location.
    • X label name = Months
    • Y label name = Sold units
    • Line width should be 4
b. Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product)
c. Read chair and table product sales data and show it using the bar chart.
    • The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.
d. Read all product sales data and show it using the stack plot
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("q16.csv")
print(df.head())

# Initializing pyplot with common attributes
fig, axis = plt.subplots(2, 2, sharex=True, sharey=True)
((ax1, ax2), (ax3, ax4)) = axis


fig.suptitle("Q: 16")


# a: Displaying the total profit
ax1.set_axis_off()
parax1 = ax1.twinx().twiny()

# parax1.set(xlabel="Months", ylabel="Sold Units")
parax1.set_ylabel("Sold Units")
parax1.set_xlabel("Months")
parax1.set_title("a: Total Profit")
parax1.plot(df["Months"], df["Total_profit"], "b:", linewidth=4, label="Total Units")
parax1.legend(loc="lower right")

# b: Displaying the number of units sold per month
parax2 = ax2.twinx().twiny()

parax2.set_title("b: Sales of individual products")
parax2.plot(df["Months"], df["Pen"], "b", label="Pen")
parax2.plot(df["Months"], df["Book"], "g", label="Book")
parax2.plot(df["Months"], df["Marker"], "r", label="Marker")
parax2.plot(df["Months"], df["Chair"], "y", label="Chair")
parax2.plot(df["Months"], df["Table"], "m", label="Table")
parax2.plot(df["Months"], df["Pen_stand"], "c", label="Pen Stand")

parax2.legend(loc="upper right")

# c: Showing table and chair sales data using a bar chart
ax3.set_axis_off()

parax3 = ax3.twinx().twiny()
parax3.set_xlabel("Months")
parax3.set_ylabel("Units Sold")
parax3.set_title("c: Sales of table and chairs in bar chart")

parax3.bar(df["Months"]-0.2, df["Chair"], color="blue", label="Chair", width=0.25)
parax3.bar(df["Months"]+0.2, df["Table"], color="red", label="Table", width=0.25)

parax3.legend(loc="upper left")

plt.tight_layout()
plt.show()