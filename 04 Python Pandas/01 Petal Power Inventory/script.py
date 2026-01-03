# Petal Power Inventory
# You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!

import pandas as pd

# Load the inventory data
inventory = pd.read_csv('inventory.csv')
# Display the first 10 rows of the inventory
print(inventory.head(10))
# Select the first 10 rows for Staten Island location
staten_island = inventory.head(10)

# Get the product description for the Staten Island location
product_request = staten_island.product_description
print(product_request)

# Filter inventory for Brooklyn location and seeds product type
seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
print(seed_request)

# Add a new column 'in_stock' to indicate if the quantity is greater than 0
inventory['in_stock'] = inventory.quantity > 0

# Calculate the total value of each inventory item
inventory['total_value'] = inventory.price * inventory.quantity

# Create a full description by combining product type and product description
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

# Apply the lambda function to each row to create the full_description column, axis=1 indicates row-wise operation
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory)
