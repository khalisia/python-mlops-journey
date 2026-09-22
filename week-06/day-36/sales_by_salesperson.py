import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

summary = df.groupby("Salesperson")["Amount"].sum()

summary.plot(kind="bar")

plt.title("Sales by Salesperson")
plt.xlabel("Salesperson")
plt.ylabel("Sales")

plt.show()