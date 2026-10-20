import pandas as pd

#Step 1 - extract data from csv file

#Extract sales data
sales_df = pd.read_csv('data/LA_Retail_Sales.csv')


# Extract weather data
weather_df = pd.read_csv("data/LA_Weather_Data.csv.")


#display first 5 rows
# print("FIRST 5 ROWS:")
# print(sales_df.head())

print("\nWEATHER DATA:")
print(weather_df.head())
print("Total weather rows:", len(weather_df))


# #Display data set
# print('DATASET:')
# sales_df.info()