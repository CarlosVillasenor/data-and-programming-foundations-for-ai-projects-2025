import pandas as pd

# Load the ad clicks data
ad_clicks = pd.read_csv('ad_clicks.csv')

# Count the number of views from each utm_source
views_count = ad_clicks.groupby(['utm_source'])['user_id'].count()
print(views_count)

# If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.
ad_clicks['is_click'] = ~ad_clicks['ad_click_timestamp'].isnull()
print(ad_clicks.head())

# Group by utm_source and is_click to count the number of clicks per source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

# Pivot the clicks_by_source table
clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id'
).reset_index()

# Calculate the percent of users who clicked on the ad from each utm_source
clicks_pivot['percent_clicked'] = clicks_pivot.apply(lambda row: row[True] / (row[True] + row[False]) * 100, axis=1)
print(clicks_pivot)

# Count the number of users in each experimental group
ads_a_b = ad_clicks.groupby(['experimental_group']).user_id.count()
print(ads_a_b)

# Calculate the percentage of users who clicked on ads in each experimental group
ads_a_b_percentage = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(ads_a_b_percentage)

# Pivot the ads_a_b_percentage table
ads_a_b_percentage_pivot = ads_a_b_percentage.pivot(
  columns='is_click',
  index='experimental_group',
  values='user_id'
)

# Calculate the percent of users who clicked on the ad in each experimental group
ads_a_b_percentage_pivot['percent_clicked'] = ads_a_b_percentage_pivot.apply(lambda row: row[True] / (row[True] + row[False]) * 100, axis=1)
print(ads_a_b_percentage_pivot)

# Analyze the performance of Ad A and Ad B over time
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
# Group by day and is_click to count the number of clicks for Ad A
a_clicks_is_click = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
# Pivot the a_clicks_is_click table
a_clicks_is_click_pivot = a_clicks_is_click.pivot(
  columns='is_click',
  index='day',
  values='user_id'
)

# Calculate the percent of users who clicked on Ad A each day
a_clicks_is_click_pivot['percent_clicked'] = a_clicks_is_click_pivot.apply(lambda row: row[True] / (row[True] + row[False]) * 100, axis=1)
print(a_clicks_is_click_pivot)
# Repeat the same analysis for Ad B
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
# Group by day and is_click to count the number of clicks for Ad B
b_clicks_is_click = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
# Pivot the b_clicks_is_click table
b_clicks_is_click_pivot = b_clicks_is_click.pivot(
  columns='is_click',
  index='day',
  values='user_id'
)

# Calculate the percent of users who clicked on Ad B each day
b_clicks_is_click_pivot['percent_clicked'] = b_clicks_is_click_pivot.apply(lambda row: row[True] / (row[True] + row[False]) * 100, axis=1)

print(b_clicks_is_click_pivot)

# Observation: Based on the percent_clicked values above, Ad A appears to perform better overall. I recommend using Ad A.
