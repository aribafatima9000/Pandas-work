import pandas as pd

# ---------------- Project 1: Student Marks Analysis ----------------
print("\n--- Project 1: Student Marks Analysis ---")
data1 = {
    "Name": ["Ali", "Sara", "Usman", "Ayesha"],
    "Math": [80, 95, 70, 60],
    "Science": [85, 90, 75, 65],
    "English": [78, 88, 72, 68]
}
df1 = pd.DataFrame(data1)

df1["Average"] = df1[["Math", "Science", "English"]].mean(axis=1)
print(df1)

print("Highest Scorer:", df1.loc[df1["Average"].idxmax(), "Name"])
print("Lowest Scorer:", df1.loc[df1["Average"].idxmin(), "Name"])
print("Subject-wise Average:\n", df1[["Math", "Science", "English"]].mean())

# ---------------- Project 2: Sales Data Tracker ----------------
print("\n--- Project 2: Sales Data Tracker ---")
data2 = {
    "Product": ["Laptop", "Mobile", "Tablet"],
    "Jan": [120, 200, 150],
    "Feb": [100, 220, 160],
    "Mar": [130, 210, 170]
}
df2 = pd.DataFrame(data2)

df2["Total Sales"] = df2[["Jan", "Feb", "Mar"]].sum(axis=1)
print(df2)

print("Best Selling Product:", df2.loc[df2["Total Sales"].idxmax(), "Product"])
print("Average Monthly Sales:\n", df2[["Jan", "Feb", "Mar"]].mean())

# ---------------- Project 3: Employee Salary Records ----------------
print("\n--- Project 3: Employee Salary Records ---")
data3 = {
    "Name": ["Ali", "Sara", "Ahmed", "Zara", "Usman"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 55000, 60000, 47000]
}
df3 = pd.DataFrame(data3)
print(df3)

print("Average Salary:", df3["Salary"].mean())
print("Employees Above Average Salary:\n", df3[df3["Salary"] > df3["Salary"].mean()])

print("Department-wise Average Salary:\n", df3.groupby("Department")["Salary"].mean())

# ---------------- Project 4: Library Book Records ----------------
print("\n--- Project 4: Library Book Records ---")
data4 = {
    "Book": ["Python Basics", "Data Science 101", "Machine Learning", "AI Intro"],
    "Author": ["Ali", "Sara", "Ahmed", "Zara"],
    "Borrows": [40, 55, 30, 60]
}
df4 = pd.DataFrame(data4)
print(df4)

print("Most Borrowed Book:", df4.loc[df4["Borrows"].idxmax(), "Book"])
print("Total Borrows:", df4["Borrows"].sum())
print("Books Sorted by Popularity:\n", df4.sort_values(by="Borrows", ascending=False))

# ---------------- Project 5: Weather Data ----------------
print("\n--- Project 5: Weather Data ---")
data5 = {
    "City": ["Lahore", "Karachi", "Islamabad"],
    "Day1": [30, 35, 28],
    "Day2": [32, 36, 27],
    "Day3": [31, 38, 26]
}
df5 = pd.DataFrame(data5)

df5["Average Temp"] = df5[["Day1", "Day2", "Day3"]].mean(axis=1)
print(df5)

print("Hottest City:", df5.loc[df5["Average Temp"].idxmax(), "City"])
print("Coldest City:", df5.loc[df5["Average Temp"].idxmin(), "City"])
print("Cities with Extreme Temps:\n", df5[(df5[["Day1","Day2","Day3"]] > 40).any(axis=1) | (df5[["Day1","Day2","Day3"]] < 0).any(axis=1)])
