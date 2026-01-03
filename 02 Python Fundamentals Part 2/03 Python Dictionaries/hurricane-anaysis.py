# Hurricane Analysis
# Project Goals
# You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.


from collections import defaultdict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# mortality scale
mortality_scale = { 0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000 }

# 1
# Update Recorded Damages
conversion = {
  "M": 1000000,
  "B": 1000000000
}

# Function to convert damage values from "Prefix-B/M" format to float values in USD
def convert_prefix_bm_to_float(damages_cost_list):
  modified_damages_list = []

  for damage_cost in damages_cost_list:
    if ("M" in damage_cost or "B" in damage_cost):
      prefix = damage_cost[-1:]
      modified_damage_cost = 0
      modified_damage_cost = damage_cost[0:-1]
      modified_damage_cost = float(modified_damage_cost)
      modified_damage_cost = modified_damage_cost * conversion[prefix]
      modified_damage_cost = int(modified_damage_cost)
      modified_damage_cost = str(modified_damage_cost)
      modified_damages_list.append(modified_damage_cost)
    else:
      modified_damages_list.append(damage_cost)

  return modified_damages_list

# test function by updating damages
modified_damages = convert_prefix_bm_to_float(damages)

# 2 
# Create a Table
def create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, deaths, damages):
  hurricanes = {}
  for index in range(len(names)):
    name = names[index]
    hurricanes[name] = {}
    # Fill each hurricane
    hurricane = hurricanes[name]
    hurricane['Name'] = name
    hurricane['Month'] = months[index]
    hurricane['Year'] = years[index]
    hurricane['Max Sustained Wind'] = max_sustained_winds[index]
    hurricane['Areas Affected'] = areas_affected[index]
    hurricane['Damage'] = damages[index]
    hurricane['Death'] = deaths[index]

  return hurricanes

# Create and view the hurricanes dictionary
hurricanes = create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, deaths, modified_damages)
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def organize_hurricanes_by_year(hurricanes):
  hurricanes_organized_by_year = {}

  for hurricane in hurricanes:
    # print(f"Key: {hurricane}, Value: {hurricanes[hurricane]}")
    # Get Year
    hurricane_year = hurricanes[hurricane]['Year']
    # Set year
    if hurricane_year not in hurricanes_organized_by_year:
      hurricanes_organized_by_year[hurricane_year] = []
    # Fill year
    for hurricane in hurricanes:
      if hurricane_year == hurricanes[hurricane]['Year']:
        hurricanes_organized_by_year[hurricane_year].append(hurricanes[hurricane])

  return hurricanes_organized_by_year

hurricanes_organized_by_year = organize_hurricanes_by_year(hurricanes)

# 4
# Counting Damaged Areas
def count_damaged_areas(hurricanes):
  # print(hurricanes)
  damaged_areas = defaultdict(int)
  for hurricane in hurricanes:
    areas_affected = hurricanes[hurricane]['Areas Affected']
    # loop throught 'Areas Affected'
    for area in areas_affected:
      if not damaged_areas[area]:
        damaged_areas[area] = 1
      elif (damaged_areas[area]):
        damaged_areas[area] += 1

  return damaged_areas
# create dictionary of areas to store the number of hurricanes involved in
affected_areas = count_damaged_areas(hurricanes)
# 5 
# Calculating Maximum Hurricane Count
def calc_max_hurricane_count_for_area(affected_areas):
  max_area = ''
  max_area_count = 0

  for area in affected_areas:
    affected_count = affected_areas[area]
    if (affected_count > max_area_count):
      max_area_count = affected_count
      max_area = area

  return max_area, max_area_count
# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = calc_max_hurricane_count_for_area(affected_areas)
# 6
# Calculating the Deadliest Hurricane
def calc_deadliest_hurricane(hurricanes):
  deadliest_hurricane = None
  max_deaths = 0

  for hurricane_name, hurricane_data in hurricanes.items():
    deaths = hurricane_data["Death"]
    if (deaths > max_deaths):
      max_deaths = deaths
      deadliest_hurricane = hurricane_name

  return deadliest_hurricane, max_deaths

# find highest mortality hurricane and the number of deaths
deadliest_hurricane, deaths_number = calc_deadliest_hurricane(hurricanes)

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def rate_hurricanes_by_mortality(hurricanes):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes:
    deaths_count = hurricanes[hurricane]['Death']

    # using a nested loop to iterate over the mortality scale
    for rating, upper_bound in mortality_scale.items():
      print(rating, upper_bound)
      if deaths_count <= upper_bound:
        hurricanes_by_mortality[rating].append(hurricanes[hurricane])
        break

  return hurricanes_by_mortality

hurricanes_rated_by_mortality = rate_hurricanes_by_mortality(hurricanes)
print(hurricanes_rated_by_mortality)
# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def find_highest_damage_hurricane(hurricanes):
  highest_damage_hurricane = None
  max_damage_cost = 0

  for hurricane in hurricanes:
    hurricane = hurricanes[hurricane]["Name"]
    damage_cost = hurricanes[hurricane]["Damage"]
    
    if (not damage_cost == "Damages not recorded"):
      damage_cost_int = int(damage_cost)
      if (damage_cost_int > max_damage_cost):
        max_damage_cost = damage_cost_int
        highest_damage_hurricane = hurricane

  return highest_damage_hurricane, max_damage_cost

highest_damaging_hurricane = find_highest_damage_hurricane(hurricanes)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
def rate_hurricanes_by_damage(hurricanes):
  hurricanes_rated_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes:
    damage_count = hurricanes[hurricane]['Damage']
    if (damage_count == "Damages not recorded" or damage_count == 0):
      hurricanes_rated_by_damage[0].append(hurricanes[hurricane])
    else:
      damage_count = int(damage_count)
      if (damage_count > 0 and damage_count <= damage_scale[1]):
        hurricanes_rated_by_damage[1].append(hurricanes[hurricane])
      elif (damage_count > damage_scale[1] and damage_count <= damage_scale[2]):
        hurricanes_rated_by_damage[2].append(hurricanes[hurricane])
      elif (damage_count > damage_scale[2] and damage_count <= damage_scale[3]):
        hurricanes_rated_by_damage[3].append(hurricanes[hurricane])
      elif (damage_count > damage_scale[3] and damage_count <= damage_scale[4]):
        hurricanes_rated_by_damage[4].append(hurricanes[hurricane])
      elif (damage_count > damage_scale[4]):
        hurricanes_rated_by_damage[5].append(hurricanes[hurricane])

  return hurricanes_rated_by_damage

hurricanes_rated_by_damage = rate_hurricanes_by_damage(hurricanes)