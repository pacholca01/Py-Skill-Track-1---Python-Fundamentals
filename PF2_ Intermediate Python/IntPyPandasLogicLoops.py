# Pickup Lesson at
# Intermediate Python: 2. Dictionaries & Pandas: Pandas Part 1

import numpy as np
import pandas as pd


dict = pd.read_csv('brics.csv', index_col=0)    # index_col tells pd.csv_read that the first column contains the row labels
# print(dict.head())                # Print Data

brics = pd.DataFrame(dict)
print(brics)                        # Print DataFrame
print(brics.index)

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
myDict = {'country':names, 'drivesRight':dr, 'carsPerCapita':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(myDict)
print("\n")
print(cars)


# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels
print("\n")
print(cars)

cars = pd.read_csv('cars.csv', index_col=0)  # index_col tells pd.csv_read that the first column contains the row labels

# Print out country column as Pandas Series
print("\n")
print(cars["country"])
print(type(cars["country"]))
# Print out country column as Pandas DataFrame
print("\n")
print(cars[["country"]])
print(type(cars[["country"]]))
# Print out DataFrame with country and drives_right columns
print("\n")
print(cars[["country", "drives_right"]])

# Print out first 3 observations
print("\n")
print(cars[0:3])
# Print out fourth, fifth and sixth observation
print("\n")
print(cars[3:6])

# Print out observations for Australia and Egypt
print("\n")
print(cars.loc[['AUS', 'EG']])  # loc uses the row name
print(cars.iloc[[1, 6]])        # iloc uses the index

# Print out drives_right value of Morocco
print("\n")
print(cars.loc['MOR','drives_right'])

# Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
print(cars.loc[["RU","MOR"],["country","drives_right"]])

# Print out drives_right column as Series
print("\n")
print(cars.iloc[:,2])
# Print out drives_right column as DataFrame
print("\n")
print(cars.iloc[:,[2]])
# Print out cars_per_cap and drives_right as DataFrame
print("\n")
print(cars.iloc[:,[0, 2]])
# print(cars.loc[:,['cars_per_cap', 'drives_right']])

# Create numpy arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print("\n")
print(my_house >= 18)
print(my_house[my_house >= 18])             # print np.array using boolean array
# my_house less than your_house
print(my_house < your_house)
print(my_house[my_house < your_house])      # print np.array using boolean array

# my_house greater than 18.5 or smaller than 10
print("\n")
print(np.logical_or(my_house > 18.5, my_house < 10))
# Both my_house and your_house smaller than 11
print("\n")
print(np.logical_and(my_house < 11, your_house < 11))

# Define variables
room = "kit"
area = 14.0

# Examine the if statement that prints out "looking around in the kitchen." if room equals "kit".
# In the script, the if construct for room has been extended with an else statement so that "looking around elsewhere." is printed if the condition room == "kit" evaluates to False.
# It's also possible to have a look around in the bedroom. The sample code contains an elif part that checks if room equals "bed". In that case, "looking around in the bedroom." is printed out.
print("\n")
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

# Write another if statement that prints out "big place!" if area is greater than 15.
# Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.
# Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")


# Filtering Pandas DataFrames
# print pandas dataframe using a boolean array
print("\n")
print(brics[brics['area']>8])
# print pandas dataframe using np.logical
print("\n")
print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)])


# While Loops
# Initialize offset
offset = 8

# Code the while loop
print("\n")
while offset != 0 :
    print("correcting...")
    offset -= 1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
print("\n")
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset -= 1
    else :
      offset += 1
    print(offset)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
print("\n")
for var in areas :
    print(var)

# Change for loop to use enumerate() and update print()
# Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
# Update the print() statement so that on each run, a line of the form "room x: y" should be printed, where x is the index
# of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string,
# with the correct spacing.
print("\n")
for i, var in enumerate(areas) :
    i += 1
    print("room " + str(i) + ": " + str(var))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
print("\n")
for x in house :
    print ("the " + x[0] + " is " + str(x[1]) + " sqm")


# Looping over Dictionaries
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
print("\n")
for k, v in europe.items():
    print("the capital of " + k + " is " + v)

# Loop over NumPy array
# If you're dealing with a 1D NumPy array, looping over all elements can be as simple as:
#
# for x in my_array :
#     ...

# If you're dealing with a 2D NumPy array, it's more complicated. A 2D array is built up of multiple 1D arrays.
# To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:
#
# for x in np.nditer(my_array) :
#     ...

# Two NumPy arrays that you might recognize from the intro course are available in your Python session: np_height,
# a NumPy array containing the heights of Major League Baseball players, and np_baseball, a 2D NumPy array that
# contains both the heights (first column) and weights (second column) of those players.

# Using a for Loop on a DataFrame
print("\n")
for var in brics :
    print(var)              # If you use the for loop like this only the column headers

# Print Row Labels from a DataFrame
print("\n")
for rowlab, row in brics.iterrows() :
    print(rowlab)

# Print Row Labels in a Series from a DataFrame
print("\n")
for rowlab, row in brics.iterrows() :
    print(rowlab)
    print (row)
    print("\n")

# Print RowLabel and Capital using for loop on DataFrame
print("\n")
for k, v in brics.iterrows() :
    print( k + ": " + v['capital'])

# How to Use a For Loop on a DataFrame to write a New Column
print("\n")
for k, v in brics.iterrows() :
    # creating a series on every iteration
    brics.loc[k, "countryNameLen"] = len(v["country"])
print(brics)

# An easier way to use a function to write a new column to a DataFrame
print("\n")
brics['capitalNameLen'] = brics['capital'].apply(len)
print(brics)

# Code for loop that adds COUNTRY column
for k, v in cars.iterrows() :
    cars.loc[k,'COUNTRY'] = v['country'].upper()
print(cars)

# Add a column to a DataFrame by calling a function on another column using .apply(str.upper)
    # We can do a similar thing to call the upper() method on every name in the country column. However, upper() is a
    # method, so we'll need a slightly different approach:
    # Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column
    # COUNTRY should be added to cars, containing an uppercase version of the country names.

cars['COUNTRY_Upper'] = cars['country'].apply(str.upper)
print(cars['COUNTRY_Upper'])

