import kagglehub
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

with open('Car_Price_Prediction.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(row['Engine Size'])
        y.append(row['Mileage'])
print(x)
print(y)

plt.scatter(x, y, s=1)
plt.xlabel("engine size")

x = np.linspace(0, 10000, 10000)
y = np.sin(x / 500)

plt.plot(x, y)

# Set ticks every 1000 units on x-axis
plt.xticks(np.arange(0, 10001, 1000))

# Set ticks every 0.5 units on y-axis
plt.yticks(np.arange(-1, 1.1, 0.5))

plt.ylabel("mileage")
plt.title("Relationship between engine size and mileage")
plt.show()

    

