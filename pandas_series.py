from itertools import product

import pandas as pd

products = ['Appels', 'Bananas', 'Oranges', 'Grapes', 'Pineappels']

sales = [150, 200, 180, 90, 60]

sales_series = pd.Series(sales, index=products)

print(sales_series)

print(sales_series['Grapes'])

total_sum = sales_series.sum()
print(total_sum)


