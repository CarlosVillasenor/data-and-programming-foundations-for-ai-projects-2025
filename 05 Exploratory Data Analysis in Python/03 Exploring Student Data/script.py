# Exploring Student Data
# Imagine that you work for a school district and have collected some data on local students and their parents. You’ve been tasked with answering some important questions:
# * How are students performing in their math classes?
# * What do students’ parents do for work?
# * How often are students absent from school?
# In this project, you’ll explore and summarize some student data in order to answer these questions.


# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head(10))

# Print summary statistics for all columns
print(students.describe(include = 'all'))

# Calculate mean
stds_math_grade_mean = students.math_grade.mean()
print("Mean: " + str(stds_math_grade_mean))

# Calculate median
stds_math_grade_median = students.math_grade.median()
print("Median: " + str(stds_math_grade_median))
print('The mean is higher than the median, suggesting a right-skewed distribution.')

# Calculate mode
stds_math_grade_mode = students.math_grade.mode()
print("Mode: " + str(stds_math_grade_mode[0]))

print("* Spread Values *")

# Calculate range
stds_math_grade_range = students.math_grade.max() - students.math_grade.min()
print("Range: " + str(stds_math_grade_range))

# Calculate standard deviation
stds_math_grade_std = students.math_grade.std()
print("STD: " + str(stds_math_grade_std))

# Calculate MAD
stds_math_grade_mad = students.math_grade.mad()
print("MAD: " + str(stds_math_grade_mad))

# Create a histogram of math grades
sns.histplot(x='math_grade', data = students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data = students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
print(students.Mjob.value_counts())

# Calculate proportion of students with mothers in each job category
print((students.Mjob.value_counts() / len(students.Mjob)) * 100)

# Create bar chart of Mjob
sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()
plt.clf()

# Example for 'address' column
print(students.address.value_counts())
sns.countplot(x='address', data=students)
plt.show()
plt.clf()
