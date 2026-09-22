import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

summary = df.groupby("Category")["Amount"].sum()

print(summary)

summary.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()