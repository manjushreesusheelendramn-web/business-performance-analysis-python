import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

months = pd.date_range(start="2023-01-01", periods=24, freq="M")

sales = [45000,47000,50000,52000,55000,58000,
         60000,62000,65000,68000,70000,72000,
         75000,78000,80000,83000,85000,87000,
         90000,93000,95000,98000,100000,105000]

expenses = [30000,31000,32000,34000,35000,36000,
            38000,39000,40000,42000,43000,45000,
            46000,47000,49000,50000,51000,52000,
            54000,55000,56000,58000,59000,60000]

df = pd.DataFrame({
    "Month": months,
    "Sales": sales,
    "Expenses": expenses
})

df["Profit"] = df["Sales"] - df["Expenses"]

print(df.head())
print(df.tail())

df["Sales Growth %"] = df["Sales"].pct_change() * 100

print("\nAverage Monthly Growth")
print(df["Sales Growth %"].mean())

print("\nTotal Profit")
print(df["Profit"].sum())

print("\nMaximum Profit")
print(df["Profit"].max())

plt.figure(figsize=(10,5))

plt.plot(df["Month"], df["Sales"], label="Sales")
plt.plot(df["Month"], df["Expenses"], label="Expenses")
plt.plot(df["Month"], df["Profit"], label="Profit")

plt.title("Business Performance Analysis")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid()

plt.show()