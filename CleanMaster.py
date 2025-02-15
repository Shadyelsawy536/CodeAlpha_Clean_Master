import pandas as pd

# Read the file
df = pd.read_csv("education_career_success.csv")

# Display the first 10 rows of the dataset
print("First 10 rows of the dataset:")
print(df.head(10))

# Calculate the number of missing values in each column
print("\nNumber of missing values in each column:")
print(df.isnull().sum())

# Drop rows with missing values in the 'High_School_GPA' column
df.dropna(subset=['High_School_GPA'], inplace=True)

# Fill all missing values with pd.NA
df.fillna(pd.NA, inplace=True)

# Remove duplicate rows based on the 'Student_ID' column
df.drop_duplicates(subset=['Student_ID'], inplace=True)

# Highlight missing values in yellow
def highlight_missing(s):
    return ['background-color: yellow' if pd.isna(v) else '' for v in s]

# Apply styling to highlight missing values
styled_df = df.style.apply(highlight_missing)

# Save the styled data as an Excel file
styled_df.to_excel("highlighted_education_data.xlsx", index=False, engine='openpyxl')

print("\nData cleaning is complete and saved successfully!")