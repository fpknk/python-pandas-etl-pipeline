import pandas as pd

#Step 1 - extract data from csv file

#read sales data from csv file
sales_df = pd.read_csv('data/LA_Retail_Sales.csv')


#display first 5 rows
print("FIRST 5 ROWS:")
print(sales_df.head())