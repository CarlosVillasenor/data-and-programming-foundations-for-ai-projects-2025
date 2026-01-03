# This project will analyse the following:
# * Find out the average age of the patients in the dataset. done
# * Analyze where a majority of the individuals are from. done
# * Look at the different costs between smokers vs. non-smokers. done
# * Figure out what the average age is for someone who has at least one child in this dataset. done

import csv

patiens_total_age = 0
patiens_total_age_with_children = 0
patiens_region = []
patiens_costs_smokers = 0
patiens_costs_non_smokers = 0
patiens_count = 0
patiens_with_children_count = 0

# Open the insurance.csv file and store it using csv.reader
try:
    with open('insurance.csv', newline='') as csvfile:
        insurance_csv = csv.DictReader(csvfile)
        for row in insurance_csv:
            patiens_count += 1
            # print(', '.join(row))
            # print(row)
            patiens_total_age += int(row["age"])
            patiens_region.append(row["region"])
            if (row["smoker"] == "yes"):
                patiens_costs_smokers += float(row["charges"])
            else:
                patiens_costs_non_smokers += float(row["charges"])
            if int(row["children"]) > 0:
                patiens_total_age_with_children += int(row["age"])
                patiens_with_children_count += 1
except:
    print("The file insurance.csv does not exist.")

# Get where a majority of the individuals are from.
patiens_region_count = {}
highest_region_count = 0
highest_region_name = ""

for region in patiens_region:
    if not region in patiens_region_count:
        patiens_region_count[region] = 1
    else:
        patiens_region_count[region] += 1
        if patiens_region_count[region] > highest_region_count:
            highest_region_count = patiens_region_count[region]
            highest_region_name = region

# Average age of the patients
patiens_average_age = patiens_total_age / patiens_count
print("The average patient age is: " + str(patiens_average_age))

print("The total number of patiens: " + str(patiens_count))
# print("highest_region_count: " + str(highest_region_count))
# print("patiens_region_count: " + str(patiens_region_count))
print("Region where a majority of the individuals are from: " + highest_region_name)

# Different costs between smokers vs. non-smokers.
print("Costs for patiens that smoke: " + str(patiens_costs_smokers))
print("Costs for patiens that don't smoke: " + str(patiens_costs_non_smokers))
difference_price_smokers_and_non_smokers = abs(patiens_costs_smokers - patiens_costs_non_smokers)
print("Difference in price of smokers compared with non smokers: " + str(difference_price_smokers_and_non_smokers))

# Average age is for someone who has at least one child in this dataset.
average_age_patiens_with_children = patiens_total_age_with_children / patiens_with_children_count
print("Average age of patiens with children: " + str(average_age_patiens_with_children))
