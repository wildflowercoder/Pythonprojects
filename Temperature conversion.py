#Temperature conversion 
print("Welcome to the Temperature conversion App")

#gather user input 
temp_f = float(input("What is the given temperature in degrees Fahrenheit: "))

#Convert Temps
temp_c = (5/9)*(temp_f - 32)
temp_k = temp_c + 273.15

#round temps
temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)


#summary table
print("\nDegrees Fahreneheit:\t" + str(temp_f))
print("Degrees Celsius:\t" + str(temp_c))

