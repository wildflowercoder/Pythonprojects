#MPH to MPS conversion 

print("Welcome to the MPH to MPS Conversion App")

#gather user input
mph = float(input("What is your speed in miles per hour"))

#convert to mps
mps = mph*0.4474
mps = round(mps, 2)

print("Your speed in meters per second is " + str(mps) + ".")
