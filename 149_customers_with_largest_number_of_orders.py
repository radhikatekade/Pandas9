# Count the number of orders for every customer, sort the values in descending order. Return the
# topmost customer number.

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Approach 1
    # orders['count'] = orders.groupby('customer_number')['customer_number'].transform('count')
    # return orders.sort_values(by='count', ascending=False).head(1)[['customer_number']]
    
    # Approach 2
    # df = orders.groupby('customer_number').nunique().reset_index()
    # OR
    df = orders.groupby('customer_number').size().reset_index(name= 'count')
    df.sort_values(by=['count'], ascending=False, inplace=True)
    return df.head(1)[['customer_number']]