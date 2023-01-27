""" Iterators """

employees = ['Nick', 'Lore', 'Jess']
for i in employees :
    print(i)

word = 'Datacamp'
for i in word :
    print(i)

""" Iterate over Range """
for i in range(4) :
    print(i)

"""Iterating Over Iterables Using iter()"""

word = "word"
i = iter(word)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))    # produces stop iteration error

word = "new word"
i = iter(word)
print(*i)           # using the star (*) iterator, aka splat operator
print(*i)           # produces stop iteration error

""" Iterating Over Dictionaries """

pyonistas = {'hugo':'brow-anderson', 'francis':'castro'}
for k, v in pyonistas.items() :
    print(k, v)

""" Iterating Over Txt File Connections """
"""
file = open('txt_file.txt')
i = iter(file)
print(next(i))
print(next(i))
"""


""" Iterators vs. Iterables
The environment has been pre-loaded with the variables flash1 and flash2. Try printing out their values with print() and next() to figure out which is an iterable and which is an iterator.
 """

"""
In [1]:
print(flash1)
['jay garrick', 'barry allen', 'wally west', 'bart allen']
In [2]:
print(flash2)
<list_iterator object at 0x7f8b815f2070>
In [3]:
print(next(flash2))
jay garrick
"""

""" Iterating over iterables (1)
"""

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for i in flash :
    print(i)

# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for i in range(3) :
    print(i)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

""" Iterators as function arguments """
# Create a range object: values
values = range(10,21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)

""" Using Enumerate """

avengers = ['iron man', 'hawk eye', 'scarlet witch', 'black widow']

e = enumerate(avengers)
print(type(e))
e_list = list(e)
print(e_list)

""" Enumerate and Upack a List"""
for i, v in enumerate(avengers) :
    print(i, v)

for i, v in enumerate(avengers, start=10) :
    print(i, v)

""" Using zip() """

names = ['tony stark', 'barton', 'wanda maximoff', 'natasha romanov']
z = zip(avengers, names)    # zips are lists of tuples
print(type(z))
z_list = list(z)
print(z_list)               # print as list of tuples

for z1, z2 in zip(avengers, names) :
    print(z1, z2)           # unpack list in lines

z = zip(avengers, names)    # the zip needed to be re-initialized for some reason
print(*z)                   # use splat operator to print all tuple elements inside of the list

# Create a list of strings: mutants
mutants = ['charles xavier',
            'bobby drake',
            'kurt wagner',
            'max eisenhardt',
            'kitty pryde']

# Create a list of tuples: mutant_list
# Create a list of tuples from mutants and assign the result to mutant_list. Make sure you generate the tuples using enumerate() and turn the result from it into a list using list().

mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for i, v in enumerate(mutants):
    print(i, v)

# Change the start index
for i, v in enumerate(mutants, start=1):
    print(i, v)
"""
# Create a list of tuples: mutant_data
# Using zip() with list(), create a list of tuples from the three lists mutants, aliases, and powers (in that order) and assign the result to mutant_data.
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for v1, v2, v3 in mutant_zip:
    print(v1, v2, v3)

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
# 'Unzip' the tuples in z1 by unpacking them into positional arguments using the * operator in a zip() call. Assign the results to result1 and result2, in that order.
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)
"""
""" Iterating over data in chunks """

"""
result = []
for chunk in pd.read_csv('data.csv', chunksize=1000) :
    resultList.append(sum(chunk['columnX']))
total = sum(resultList)
print(total)

# OR

total = 0
for chunk in pd.read_csv('data.csv', chunksize=1000) :
    total += sum(chunk['columnX'])
print(total)
"""

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
import pandas as pd
for chunk in pd.read_csv('tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)



# Extracting information for large amounts of Twitter data
# Define count_entries()
# Define the function count_entries(), which has 3 parameters. The first parameter is csv_file for the filename, the second is c_size for the chunk size, and the last is colname for the column name.
def count_entries(csv_file, c_size, colname) :
    """Return a dictionary with counts of occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file,chunksize=c_size):

        # Iterate over the column in DataFrame
        for i in chunk[colname]:
            if i in counts_dict.keys():
                counts_dict[i] += 1
            else:
                counts_dict[i] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
# Call the count_entries() function by passing to it the filename 'tweets.csv', the size of chunks 10, and the name of the column to count, 'lang'. Assign the result of the call to the variable result_counts.
result_counts = count_entries('/Users/charlespacholski/PycharmProjects/pythonProject/tweets.csv',10,'lang')

# Print result_counts
print(result_counts)

""" Populate a List with Numbers """

nums = [12, 8, 21, 3, 36]
new_nums = []
for i in nums :
    new_nums.append(i + 1)
print(new_nums)

""" Populate a List with List Comprehensions"""
nNums = [i + 1 for i in nums]
print(nNums)

r = [i for i in range(10)]      # range is the iterable, i is the iterator variable, r is the output expression
print(r)

""" Nested For Loops """
pairs1 = []
for num1 in range(0,2) :
    for num2 in range(6,8) :
        pairs1.append((num1,num2))
print(pairs1)

""" Nested loops using a List Comprehesion"""
p2 = [(n1, n2) for n1 in range(0,2) for n2 in range(6,8) ]
print(p2)

# Create list comprehension: squares
# Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.

squares = [i**2 for i in range(0,10)]
print(squares)

# Create a 5 x 5 matrix using a list of lists: matrix
# In the inner list comprehension - that is, the output expression of the nested list comprehension - create a list of values from 0 to 4 using range(). Use col as the iterator variable.
matrix = [[i for i in range(0,5)] for i in range(0,5) ]

""" Nested list comprehensions
 """
# Print the matrix
for row in matrix:
    print(row)

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)

""" List Comprehensions with Conditionals"""

conditionalSquares = [ i**2 for i in range(10) if i % 2 == 0]
print(conditionalSquares)

conditionalSquares2 = [ i**2 if i % 2 == 0 else 0 for i in range(10)]
print(conditionalSquares2)

""" Dictionary Comprehensions """

pos_negDict = {i:-i for i in range(10)}
print(pos_negDict)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
# Use member as the iterator variable in the list comprehension. For the conditional, use len() to evaluate the iterator variable. Note that you only want strings with 7 characters or more.
new_fellowship = [i for i in fellowship if len(i) >= 7]

# Print the new list
print(new_fellowship)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
# In the output expression, keep the string as-is if the number of characters is >= 7, else replace it with an empty string - that is, '' or "".
new_fellowship = [i if len(i) >= 7 else '' for i in fellowship]

# Print the new list
print(new_fellowship)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
# Create a dict comprehension where the key is a string in fellowship and the value is the length of the string. Remember to use the syntax <key> : <value> in the output expression part of the comprehension to create the members of the dictionary. Use member as the iterator variable.
new_fellowship = {i:len(i) for i in fellowship}

# Print the new dictionary
print(new_fellowship)


""" Working with Generator Objects"""

generatorOb = (i for i in range(10*1000000) if i % 10 == 0)
print(next(generatorOb))
print(next(generatorOb))

def sequenceGen (n) :
    """ Generate values 0 to n """
    i = 0
    while i < n :
        yield i
        i += 3

newSeq = sequenceGen(10)
print(next(newSeq))
for i in newSeq :
    print(i)

# Create generator object: result
result = (i for i in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for i in result :
    print(i)

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(i) for i in lannister)

# Iterate over and print the values in lengths
for i in lengths :
    print(i)

"""
# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list) :
    """
"""Generator function that yields the length of the strings in input_list."""
"""
    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister) :
    print(value)
"""
"""
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)

"""


"""
# Zip lists: zipped_lists
zipped_lists = zip(feature_names,row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)

# Define lists2dict()
def lists2dict(list1, list2):
    """
"""Return a dictionary where list1 provides the keys and list2 provides the values."""
"""
    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return  rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])

import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())

"""
# Writing a generator to load data in chunks
# Open a connection to the file
with open('world_ind_pop_data.csv') as file :

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)

# Writing a generator to load data in chunks (2)

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data


# Open a connection to the file
with open('world_ind_pop_data.csv') as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

#  Writing a generator to load data in chunks (3)

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_ind_pop_data.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print
print(counts_dict)



# Writing an iterator to load data in chunks (1)

# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('world_ind_pop_data.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))


# Writing an iterator to load data in chunks (2)

"""# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)

# Writing an iterator to load data in chunks (3)
# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(i[0]*(i[1]*0.01)) for i in pops_list]
print(df_pop_ceb['Total Urban Population'])
# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

Writing an iterator to load data in chunks (4)
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader :

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

# Writing an iterator to load data in chunks (5)
# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn,'CEB' )

# Call plot_pop for country code 'ARB'
plot_pop(fn,'ARB' )


"""