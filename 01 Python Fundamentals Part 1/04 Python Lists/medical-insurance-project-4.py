# Python Lists: Medical Insurance Estimation Project
# In this project, you will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.
# Note: while insurance companies do use BMI in their calculations, and that is reflected in this project, BMI is not necessarily an accurate predictor of health. As data scientists, we should always be skeptical of quantitative measures like BMI that reduce complex phenomena to a single number.
# You will apply your new knowledge of Python Lists to store insurance cost data in a list as well as compare estimated insurance costs to actual insurance costs.


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  # Calculate estimated cost using provided formula
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  # Print the estimated insurance cost
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name="Maria", age=31, sex=0, bmi=23.1, num_of_children=1, smoker=0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name="Rohan", age=25, sex=1, bmi=28.5, num_of_children=3, smoker=0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name="Valentina", age=53, sex=0, bmi=31.4, num_of_children=0, smoker=1)

# Create lists of names and their corresponding insurance costs
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_data = list(zip(names, insurance_costs))
print("Here is the actual insurance cost data: " + str(insurance_data))

# Create a list of estimated insurance cost data
estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
# Print the estimated insurance cost data
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))
