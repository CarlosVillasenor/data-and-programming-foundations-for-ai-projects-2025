# Python Functions: Medical Insurance Project
# You are curious about how certain factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.
# Note: while insurance companies do use BMI in their calculations, and that is reflected in this project, BMI is not necessarily an accurate predictor of health. As data scientists, we should always be skeptical of quantitative measures like BMI that reduce complex phenomena to a single number.
# You will apply your new knowledge of Python functions to write a useful function that calculates medical insurance costs.


# Create "calculate_insurance_cost()" function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  # Calculate estimated insurance cost, using the following formula: 
  # 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  # Print the estimated insurance cost with the name variable included
  txt = "The estimated insurance cost for {name} is {estimated_cost} dollars."
  print(txt.format(estimated_cost=estimated_cost, name=name))
  # Return the estimated cost
  return txt.format(estimated_cost=estimated_cost, name=name), estimated_cost

# Estimate Maria's insurance cost
insurance_cost_1 = calculate_insurance_cost(age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0, name="Maria")

# Estimate Omar's insurance cost 
insurance_cost_2 = calculate_insurance_cost(age=35, sex=1, bmi=22.2, num_of_children=0, smoker=1, name="Omar")

# Estimate my own insurance cost
insurance_cost_3 = calculate_insurance_cost(age=34, sex=1, bmi=21, num_of_children=0, smoker=0, name="Carlos")

# Create calculate_cost_difference() function below:
def calculate_cost_difference(cost1, cost2):
  # Calculate the difference between the two costs
  difference = abs(cost1 - cost2)
  print(f'The difference in insurance cost is {difference} dollars.')

# Call calculate_cost_difference() function below:
calculate_cost_difference(insurance_cost_1[1], insurance_cost_2[1])
