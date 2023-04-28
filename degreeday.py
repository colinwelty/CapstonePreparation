import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Prompt user for stid in lowercase
stid = input("Enter the Mesonet station ID in lowercase: ")

# Prompting user for start and end dates
start_date_str = input("Enter start date (yyyy-mm-dd): ")
end_date_str = input("Enter end date (yyyy-mm-dd): ")

# Converting start and end date strings to datetime objects
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

df_list = []
current_date = start_date
while current_date <= end_date:
    # Generating URL for file to download
    url = "https://www.mesonet.org/data/public/mesonet/summaries/monthly/mts/" + current_date.strftime("%Y/%m/%Y%m") + stid + ".mts"
    # Reading file into dataframe
    df = pd.read_csv(url, skiprows=(0,1), header=None, delimiter=r"\s+")

    df_list.append(df)
    # Incrementing current date by one month
    current_date += relativedelta(months=1)

# Concatenating dataframes into a single dataframe
final_df = pd.concat(df_list)
# Filtering the dataset based on the user input
filtered_df = final_df[(final_df.index >= 1) & (final_df.index <= (end_date - start_date).days+1)]

# Generating list of dates between start and end dates
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

cumulative_degree_days = 0.00

# Iterating over each day in the date range
for date in date_range:
    # Perform your analysis or other operations for each day
    # You can access the rows of the dataframe corresponding to this date using .iloc[]:
    row_index = (date - start_date).days + 1
    df_for_this_day = filtered_df.iloc[row_index - 1]
    # Do whatever you need to do with this subset of the dataframe
    #if float(df_for_this_day[3]) > 90.00:
    #         df_for_this_day[3] = "90.00"
            
    
    degree_day = ((float(df_for_this_day[4]) + float(df_for_this_day[3])) / 2) - 38
    if degree_day > 0:
        print(date, degree_day)
        cumulative_degree_days += degree_day

# Calculating cumulative degree day heat unit for the filtered data and storing it in a variable
#cumulative_degree_days = (((pd.to_numeric(filtered_df[4]) + pd.to_numeric(filtered_df[3])) / 2) - 38).clip(0, None).sum()
print("Cumulative degree day heat unit: ", cumulative_degree_days)
