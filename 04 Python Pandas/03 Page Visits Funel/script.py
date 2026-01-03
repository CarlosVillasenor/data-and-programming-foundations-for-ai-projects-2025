# Page Visits Funnel
# Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.
# In this case, our funnel is going to describe the following process:
# 1-A user visits CoolTShirts.com
# 2-A user adds a t-shirt to their cart
# 3-A user clicks “checkout”
# 4-A user actually purchases a t-shirt


import pandas as pd

# Load the data
visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

# Display the first five rows of each DataFrame
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# Merge visits and cart data
visits_cart = pd.merge(visits, cart, how="left")
print(visits_cart.head())

# Get the total number of visits
total_visits = len(visits_cart)
print(total_visits)

# Filter visits where cart_time is null (i.e., no items were added to the cart)
visits_no_cart = visits_cart[visits_cart.cart_time.isnull()]
# Get the total number of visits with no items added to the cart
total_visits_no_cart = len(visits_no_cart)
print(total_visits_no_cart)

# Get the percentage of users who visited Cool T-Shirts Inc that ended up not placing a t-shirt in their cart
percent_no_cart = (100 * float(total_visits_no_cart))/total_visits
print(percent_no_cart)

# Merge cart and checkout data
cart_checkout = pd.merge(cart, checkout, how="left")
print(cart_checkout)

# Filter cart data where checkout_time is null (i.e., did not proceed to checkout)
cart_no_checkout = cart_checkout[cart_checkout.checkout_time.isnull()]
total_cart_no_checkout = len(cart_no_checkout)
# Get the percentage of users put items in their cart, but did not proceed to checkout
percent_no_checkout = (100 * float(total_cart_no_checkout))/len(cart_checkout)
print(percent_no_checkout)

# Merge all data together
all_data = visits.merge(cart, how='left').merge(checkout , how='left').merge(purchase, how='left')
print(all_data.head())

# Filter all data where checkout_time is not null
all_data_checkout = all_data[~all_data.checkout_time.isnull()]
print(all_data_checkout.head())

# Filter all data where purchase_time is not null
all_data_purchase = all_data[~all_data.purchase_time.isnull()]
print(all_data_purchase.head())

# Get the percentage of users proceeded to checkout, but did not purchase a t-shirt
all_data_user_not_purchase = len(all_data_checkout) - len(all_data_purchase)
print(all_data_user_not_purchase)

percentage_checkout_no_purchase = (all_data_user_not_purchase * 100) / len(all_data_checkout)
print(percentage_checkout_no_purchase)

# Find the lowest percentage in the funnel
funnel_percentages = [percent_no_cart, percent_no_checkout, percentage_checkout_no_purchase]
# Get the lowest percentage
lowest_funnel = min(funnel_percentages)
print(lowest_funnel)

# Calculate the time spent from visit to purchase
all_data["time_spend_on_purchase"] = all_data.purchase_time - all_data.visit_time
print(all_data.head(30))

# Get & show the average time spent from visit to purchase
print(all_data.time_spend_on_purchase.mean())
print(cart_checkout.head())
