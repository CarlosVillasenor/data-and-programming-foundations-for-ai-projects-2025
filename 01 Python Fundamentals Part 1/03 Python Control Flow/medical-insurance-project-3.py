# Python Control Flow: Medical Insurance Project
# In this project, you will examine how factors such as age, sex, number of children, and smoking status contribute to medical insurance costs.
# You will apply your knowledge of Python control flow to write code that gives people advice on how to lower their medical insurance costs.


# Function to analyze smoking status and provide advice
def analyze_smoker(smoker_status):
  if (smoker_status):
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

# Function to estimate insurance cost based on various factors
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  # Validate inputs
  if not isinstance(age, int) or age < 0:
    return "Invalid age input"
  if not isinstance(num_of_children, int) or num_of_children < 0:
    return "Invalid number of children input"
  # Continue with cost estimation
  estimated_cost = 400 * age - 128 * sex + 425 * num_of_children + 10000 * smoker - 2500
  # Print the estimated insurance cost
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  # Analyze smoking status
  analyze_smoker(smoker)
  # Return the estimated cost
  return estimated_cost

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name='Keanu', age=29, sex=1, num_of_children=3, smoker=1)

# Estimate Carlos's insurance cost
carlos_insurance_cost = estimate_insurance_cost(name='Carlos', age=34, sex=1, num_of_children=0, smoker=0)
