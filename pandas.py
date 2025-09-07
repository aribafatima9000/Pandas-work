import pandas as pd

# =======================
# Step 1: Sample Data
# =======================
data = {
    "Name": ["Ali", "Sara", "Ayesha", "Bilal", "Usman"],
    "Math": [78, 55, 89, 92, 40],
    "Science": [88, 72, 95, 60, 50],
    "English": [90, 65, 85, 70, 45],
    "Computer": [95, 80, 90, 75, 60]
}

df = pd.DataFrame(data)
print("📌 Original Data:")
print(df)

# =======================
# Step 2: Total & Average
# =======================
df["Total"] = df[["Math", "Science", "English", "Computer"]].sum(axis=1)
df["Average"] = df[["Math", "Science", "English", "Computer"]].mean(axis=1)

# =======================
# Step 3: Highest & Lowest Marks
# =======================
df["Highest"] = df[["Math", "Science", "English", "Computer"]].max(axis=1)
df["Lowest"] = df[["Math", "Science", "English", "Computer"]].min(axis=1)

# =======================
# Step 4: Class Topper
# =======================
topper = df.loc[df["Total"].idxmax()]
print("\n🏆 Class Topper:")
print(topper)

# =======================
# Step 5: Subject-Wise Analysis
# =======================
print("\n📊 Subject-wise Average Marks:")
print(df[["Math", "Science", "English", "Computer"]].mean())

print("\n📊 Pass/Fail Analysis (Pass = 40+):")
for subject in ["Math", "Science", "English", "Computer"]:
    passed = (df[subject] >= 40).sum()
    failed = (df[subject] < 40).sum()
    print(f"{subject}: ✅ Passed = {passed}, ❌ Failed = {failed}")

# =======================
# Step 6: Save Results to CSV
# =======================
df.to_csv("student_results.csv", index=False)
print("\n💾 Results saved to 'student_results.csv'")
