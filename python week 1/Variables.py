# Subject scores
math_score = 100
scie_score = 80
social_score = 73

# Calculate average
average_score = (math_score + scie_score + social_score) / 3

# Print individual scores
print("Mathematics mark:", math_score)
print("Science mark:", scie_score)
print("Social mark:", social_score)

# Print average
print("Average Score:", average_score)

# Determine grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
else:
    grade = "F"

# Print grade
print("Grade:", grade)