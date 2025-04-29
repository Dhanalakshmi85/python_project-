# Ask the user for the mass in medieval units
talents = float(input("Enter the mass in talents : "))
pounds = float(input("Enter the mass in pounds : "))
lots = float(input("Enter the mass in lots : "))

# Conversion constants
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3

# Convert the medieval units to grams
total_lots = (talents * pounds_per_talent * lots_per_pound) + (pounds * lots_per_pound) + lots
total_grams = total_lots * grams_per_lot

# Convert grams to kilograms and grams
kilograms = total_grams // 1000
grams = total_grams % 1000

# Print the result in kilograms and grams
print(f"The mass is: {int(kilograms)} kilograms and {int(grams)} grams.")
