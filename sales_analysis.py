import pandas as pd
import matplotlib.pyplot as plt

# Excel file load
df = pd.read_excel("data/sales_data.xlsx")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Rows and Columns
print("\nShape:")
print(df.shape)

# Column Names
print("\nColumns:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
print("Before:", df.shape)

df.drop_duplicates(inplace=True)

print("After:", df.shape)
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)
df['Sales'] = df['Quantity'] * df['Price']
print(df.head())
df['Month'] = df['Date'].dt.month_name()
print(df[['Date','Month']].head())
total_revenue = df['Sales'].sum()

print("Total Revenue =", total_revenue)
top_products = (
    df.groupby('Product')['Sales']
      .sum()
      .sort_values(ascending=False)
)

print(top_products)
print(top_products.head(5))
region_sales = (
    df.groupby('Region')['Sales']
      .sum()
)

print(region_sales)
monthly_sales = (
    df.groupby('Month')['Sales']
      .sum()
)

print(monthly_sales)
monthly_sales.plot(
    kind='line',
    marker='o'
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()
plt.savefig("charts/monthly_sales.png")
monthly_sales.plot(
    kind='line',
    marker='o'
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.savefig("charts/monthly_sales.png")

plt.show()
top_products.head(10).plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Revenue")

plt.savefig("charts/top_products.png")

plt.show()
region_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Region Sales Distribution")

plt.savefig("charts/region_sales.png")

plt.show()
with pd.ExcelWriter(
    "output/sales_report.xlsx"
) as writer:

    top_products.to_excel(
        writer,
        sheet_name="Top Products"
    )

    region_sales.to_excel(
        writer,
        sheet_name="Region Sales"
    )

    monthly_sales.to_excel(
        writer,
        sheet_name="Monthly Sales"
    )