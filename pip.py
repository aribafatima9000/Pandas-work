import pandas as pd

data = {
    "OrderID": [101,102,103,104,105],
    "CustomerID": [1,2,1,3,2],
    "Product": ["Laptop","Mobile","Tablet","Laptop","Mobile"],
    "Quantity": [1,2,1,1,3],
    "Price": [800,300,200,900,280],
    "OrderDate": pd.date_range("2024-05-01", periods=5, freq="D")
}

df = pd.DataFrame(data)

# Total Bill per order
df["TotalBill"] = df["Quantity"] * df["Price"]

# Most frequent customer
print(df["CustomerID"].value_counts().idxmax())

# Product with highest revenue
print(df.groupby("Product")["TotalBill"].sum().idxmax())
