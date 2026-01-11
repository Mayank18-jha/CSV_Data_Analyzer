import os
import pandas as pd

df = pd.read_csv(r"C:\Users\MAYANK\Desktop\GitHub_Projects\Assets\Book1.csv")

print("Original Data")
print(df)

print("\nDataset Info")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

df.drop_duplicates(inplace=True)

print("\nSummary Statistics")
print(df.describe())


output_path = r"C:\Users\MAYANK\Desktop\GitHub_Projects\Outputs"

if not os.path.exists(output_path):
    os.makedirs(output_path)

df.to_csv(f"{output_path}/cleaned_data.csv", index=False)

print("\n✅ Cleaned data saved successfully!")
