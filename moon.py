import pandas as pd
import numpy as np


data = {
    "OrderID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "CustomerName": ["Ali", "Sara", "Ahmed", "Fatima", "John", "Ali", "Sara", "David", "Ahmed", "Fatima"],
    "Product": ["Laptop", "Shirt", "Mobile", "Shoes", "Laptop", "Mobile", "Shirt", "Fridge", "Shoes", "Laptop"],
    "Category": ["Electronics", "Clothes", "Electronics", "Clothes", "Electronics",
                 "Electronics", "Clothes", "Electronics", "Clothes", "Electronics"],
    "Quantity": [1, 2, 1, 1, 2, 1, 3, 1, 2, np.nan],
    "Price": [700, 40, 300, 50, 750, 320, 35, 600, 55, 800],
    "OrderDate": pd.to_datetime([
        "2024-01-10", "2024-01-12", "2024-02-05", "2024-02-15",
        "2024-03-02", "2024-03-18", "2024-04-10", "2024-04-25",
        "2024-05-05", "2024-05-15"
    ]),
    "Region": ["North", "South", "North", "West", "East", "North", "South", "East", "West", "North"]
}

df = pd.DataFrame(data)

print("🔹 Original Data:")
print(df)

df["TotalSale"] = df["Quantity"].fillna(0) * df["Price"]

print("\n🔹 Data with Total Sale:")
print(df[["OrderID", "Product", "Quantity", "Price", "TotalSale"]])


category_sales = df.groupby("Category")["TotalSale"].sum()
print("\n🔹 Category-wise Total Revenue:")
print(category_sales)


product_sales = df.groupby("Product")["TotalSale"].sum().sort_values(ascending=False).head(5)
print("\n🔹 Top 5 Products by Revenue:")
print(product_sales)


region_avg = df.groupby("Region")["TotalSale"].mean()
print("\n🔹 Region-wise Average Order Value:")
print(region_avg)


monthly_sales = df.groupby(df["OrderDate"].dt.to_period("M"))["TotalSale"].sum()
print("\n🔹 Monthly Sales Trend:")
print(monthly_sales)

print("\n🔹 Missing Values Before:")
print(df.isnull().sum())


df.drop_duplicates(subset=["OrderID"], inplace=True)


customer_sales = df.groupby("CustomerName")["TotalSale"].sum().sort_values(ascending=False).head(10)
print("\n🔹 Top Customers by Total Purchase:")
print(customer_sales)


pivot = pd.pivot_table(df, values="TotalSale", index="Category", columns="Region", aggfunc="sum", fill_value=0)
print("\n🔹 Pivot Table (Category vs Region):")
print(pivot)
