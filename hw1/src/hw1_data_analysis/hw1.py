import pandas as pd
import matplotlib.pyplot as plt

#1
bicycle = pd.read_csv('bicycle_data.csv')

#2
print(bicycle.dtypes)
# Cols: Date (datetime), Fremont Bridge Sidewalks, south of N 34th St Total (int), Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk (int), Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk (int). The count fields represent the total bicycles detected during the specified one hour period. 
west = "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"
east = "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"
total = "Fremont Bridge Sidewalks, south of N 34th St Total"
bicycle = bicycle.astype({'Date': 'datetime64[us]', total: 'Int64', west: 'Int64', east: 'Int64'})
print(bicycle.dtypes)

#3
bicycle[total] = bicycle[west] + bicycle[east]
bicycle['hour'] = bicycle['Date'].dt.hour
bicycle['year'] = bicycle['Date'].dt.year
bicycle.head()

#4
bicycle2016 = bicycle[bicycle['year'] == 2016].copy()

#5
miss = bicycle2016[[total, west, east]].isna().any(axis=1)
print("Number of missing data points:", miss.sum())
# there is 1 point of missing data
bicycle2016_no_missing = bicycle2016[~miss].copy()

#6
hourly_counts = bicycle2016_no_missing.groupby('hour')[total].sum()
plt.figure(figsize=(10, 6))
plt.plot(hourly_counts.index, hourly_counts.values, label='Total')
plt.xlabel('Hour of the Day')
plt.ylabel('Bicycle Count')
plt.title('Total Bicycle Counts on Fremont Bridge in 2016 by Hour of the Day')
plt.savefig('counts_by_hour.png')

#7
mean_hourly_counts = bicycle2016_no_missing.groupby('hour')[total].mean()
busiest = mean_hourly_counts.idxmax()
print("The busiest hour of the day on Fremont Bridge in 2016 is:", busiest)
# the busiest hour of the day on Fremont Bridge in 2016 is 17
