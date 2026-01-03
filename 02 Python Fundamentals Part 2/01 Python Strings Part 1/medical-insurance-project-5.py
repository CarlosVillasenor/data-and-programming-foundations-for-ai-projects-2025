# Python Strings: Medical Insurance Project
# You are a doctor who needs to clean up medical patient records, which are currently stored in one large string.
# In this project, you will use your new knowledge of Python strings to obtain and clean up medical data so that it is easier to read and analyze.

# Set medical data string
medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Replace '#' with '$' and count the number of records
updated_medical_data = medical_data.replace("#", "$")
num_records = 0

# Count the number of medical records in the data
for character in updated_medical_data:
  if (character == "$"): 
    num_records += 1

# Print the number of medical records
print("There are {num_records} medical records in the data.".format(num_records=num_records))

# Split the data into individual records
medical_data_split = updated_medical_data.split(";") 
medical_records = []

# Split each record into its fields and store in a list called medical_records
for medical_record in medical_data_split:
  medical_record_split = medical_record.split(",")
  medical_records.append(medical_record_split)

medical_records_clean = []

# Clean up the whitespace in each record
for record  in medical_records:
  # Empty list that will store each cleaned record
  record_clean = []
  for item in record:
    # Clean the whitespace for each record using item.strip()
    record_clean.append(item.strip())
  # Add the cleaned medical record to the medical_records_clean list
  medical_records_clean.append(record_clean)

print(medical_records_clean)

# store each name, age, BMI, and insurance cost in separate lists
names = []
ages = []
bmis = []
insurance_costs = []

# Print out the names of each individual in the medical record
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

# Print the lists to confirm they were populated correctly
print(names)
print(ages)
print(bmis)
print(insurance_costs)

# Calculate the average BMI across all individuals
total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)
# Print the average BMI
print("Average BMI: {average_bmi}".format(average_bmi=round(average_bmi, 2)))
