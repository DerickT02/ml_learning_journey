import csv
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

# Read the data
with open('Car_Price_Prediction.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            year = int(row['Year'])
            price = float(row['Price'])
            if 2001 <= year <= 2021:  # Filter years between 2001–2021
                x.append(year)
                y.append(price)
        except:
            continue  # Skip rows with bad data

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=5, alpha=0.3)  # Scatter plot with small dots and transparency
plt.xlabel("Year")
plt.ylabel("Price")
plt.title("Relationship Between Car Year and Price")
plt.xticks(np.arange(2001, 2022, 2))  # Ticks every 2 years

plt.show()