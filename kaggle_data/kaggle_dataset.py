from multiprocessing.reduction import duplicate

import pandas as pd
df = pd.read_csv('avgIQpercountry.csv')

# print(df.info())


first_rows = df.head()
# print(first_rows)

country_data = df['Country']
# print(country_data)


subset = df[['Country', 'Average IQ']]


# print(subset)

filtered_df = subset[subset['Average IQ'] > 100]
print(filtered_df)


null_mask = df.isnull()

null_count = null_mask.sum()
print("\nCount of null values in each column")
# print(null_count)

df.dropna(inplace=True)
print("\nDataSet information after removing null values:")
print(df.info)

duplicated_count = df.duplicated().sum()
print("\ncount of duplicated rows:")
print(duplicated_count)


avg_iq_per_countinent = df.groupby('Countinent')['Average IQ'].mean()
print(avg_iq_per_countinent)

sorted_avg_iq_per_countinent = avg_iq_per_countinent.sort_values(ac)
print(avg_iq_per_countinent)
