import pandas as pd
from sqlalchemy import create_engine
import urllib

# Read data from CSV
df = pd.read_csv("Jamesmerce_Raw_Data.csv")

# Check Raw Data Frame
print("\nRaw Data Frame:")
print(df)

# Reformat Date & Convert errors to NaT
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Fill missing values (NaT) for Dates
df["Ship Date"] = df["Ship Date"].fillna(df["Order Date"])

# Rename & Fill missing values
df["Customer Name"] = df["Customer Name"].str.replace(r"[^a-zA-Z\s]", "", regex=True)
df["Customer Name"] = df["Customer Name"].str.title()
df["Customer Name"] = df["Customer Name"].fillna("Unknown Customer")

# Convert Sales/Profit to numeric, set invalid values to None
for col in ["Sales", "Profit"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows with NULL Sales/Profit and Sales <= 0
df = df.dropna(subset=["Sales"])
df = df.dropna(subset=["Profit"])
df = df[df["Sales"] > 0]

# Remove rows containing outliers (>1e6)
df = df[df["Sales"].abs() < 1e6]
df = df[df["Profit"].abs() < 1e6]

# Recalculate Profit Margin
df["Profit Margin"] = df.apply(lambda row:(row["Profit"]/row["Sales"]
                               if (row["Sales"] not in [0, None] and row["Profit"] is not None)
                               else None), axis=1)
df["Profit Margin"] = df["Profit Margin"].round(2)


# # Reformat discount values and replace missing with 0
df["Discount"] = df["Discount"].str.replace("%", "").astype(float) / 100
df["Discount"] = df["Discount"].fillna(0)



# Check Filtered Data
print("\nNew Filtered Data:")
print(df)

#
df.to_csv("Jamesmerce_Clean_Data.csv", index=False)

