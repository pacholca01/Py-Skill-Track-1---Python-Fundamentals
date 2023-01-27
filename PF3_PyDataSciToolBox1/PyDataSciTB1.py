# Buit in functions
x = str(5)
print(x)

# Defining a function
def square(value) :                         # Function Header
    """Retrun the square of a value"""      # this is the docstring for the newly defined function
    new_value = value ** 2                  # function body
    return new_value

num = square(5)
print(num)

# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    # In the function body, concatenate the string, 'congratulations' with another string, '!!!'. Assign the result to shout_word.

    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()

# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)

# Defining a function with multiple variables
def raiseToThePower(value0, value1) :                         # Function Header
    """Retrun the square of a value"""      # this is the docstring for the newly defined function
    new_value = value0 ** value1                  # function body
    return new_value

num = raiseToThePower(5,5)
print(num)

# Tuples
# Essentially immutable lists, they are initiallized using parenthases instead of brackets
evenNumTuple = (2,4,6,8)
print(type(evenNumTuple))
a, b, c, d, = evenNumTuple
print(a)
print(b)
print(c)
d = evenNumTuple[3]
print(d)

def raise_both(value0, value1) :
    """ Raise to the power of the value and vice versa"""
    new_value0 = value0 ** value1
    new_value1 = value1 ** value0

    new_tuple = (new_value0, new_value1)

    return new_tuple

returnedVar = raise_both(2,3)

print(returnedVar)


# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'

    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'

    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout


# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)

"""
# Unpack nums into num1, num2, and num3
num1, num2, num3, = nums

# Construct even_nums
even_nums = (2, 4, 6)
"""

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'

    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'

    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words


# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)

import pandas as pd
"""

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)


# Define the function count_entries(), which has two parameters. The first parameter is df for the DataFrame and the second is col_name for the column name.
# Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.
# Return the langs_count dictionary from inside the count_entries() function.
# Call the count_entries() function by passing to it tweets_df and the name of the column, 'lang'. Assign the result of the call to the variable result.

# Define count_entries()
def count_entries(df, col_name):
    ""Return a dictionary with counts of occurrences as value for each key.""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for i in col:

        # If the language is in langs_count, add 1
        if i in langs_count.keys():
            langs_count[i] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[i] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)
"""


# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    # Change the value of team in the global scope to the string "justice league". Assign the result to team.
    team = 'justice league'

# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

"""
Nested Functions II
Great job, you've just nested a function within another function. One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution.

Let's move forward then! In this exercise, you will complete the definition of the inner function inner_echo() and then call echo() a couple of times, each with a different argument. Complete the exercise and see what the output will be!

Instructions
100 XP
Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
Complete the function echo() so that it returns inner_echo.
We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
Hit Submit to call twice() and thrice() and print the results.
"""


# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))


"""
The keyword nonlocal and nested functions
Let's once again work further on your mastery of scope! In this exercise, you will use the keyword nonlocal within a nested function to alter the value of a variable defined in the enclosing scope.

Instructions
100 XP
Assign to echo_word the string word, concatenated with itself.
Use the keyword nonlocal to alter the value of echo_word in the enclosing scope.
Alter echo_word to echo_word concatenated with '!!!'.
Call the function echo_shout(), passing it a single argument 'hello'.
"""

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""

    # Concatenate word with itself: echo_word
    echo_word = word * 2

    # Print echo_word
    print(echo_word)

    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        # Use echo_word in nonlocal scope
        nonlocal echo_word

        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'

    # Call function shout()
    shout()

    # Print echo_word
    print(echo_word)


# Call function echo_shout() with argument 'hello'
echo_shout('hello')

"""Default & Flexible Arguments"""
"""Default Arguments"""

def power(num, pow=1) :
    """Raise the number to the power of pow"""
    newValue = num ** pow
    return newValue

print(power(9,2))
print(power(9))

"""Flexible Arguments"""
def addAll(*args) :
    """Sum all arguments"""
    sum = 0
    for i in args :
        sum += i
    return sum

print(addAll(5,4,46,2))

""" **Kwargs (Keyword Arguments similar to a dictionary)"""

def printAll(**kwargs) :
    """Print out all arguments and their keys"""
    for k, v in kwargs.items() :
        print(k + ': ' + v)

printAll(number='4', yes='no')

"""Functions with One Default Arg"""

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey", echo=5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

"""Functions with multiple default arguments"""

# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", echo=5, intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)

# Print with_big_echo and big_no_echo
print(with_big_echo)
print(big_no_echo)


"""Functions with variable-length arguments (*args)"""
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge = ""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string "luke": one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)



"""Functions with variable-length keyword arguments (**kwargs)"""

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for k, v in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(k + ": " + v)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")


"""Bringing it all together (1)
Recall the Bringing it all together exercise in the previous chapter where you did a simple Twitter analysis by developing a function that counts how many tweets are in certain languages. The output of your function was a dictionary that had the language as the keys and the counts of tweets in that language as the value.
In this exercise, we will generalize the Twitter language analysis that you did in the previous chapter. You will do that by including a default argument that takes a column name.
For your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided.

# Define count_entries()
def count_entries(df, col_name):
    """
"""Return a dictionary with counts of  occurrences as value for each key."""
"""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)


"""
"""
Bringing it all together (2)
Wow, you've just generalized your Twitter language analysis that you did in the previous chapter to include a default argument for the column name. You're now going to generalize this function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!
Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided.
"""
"""
# Define count_entries()
def count_entries(df, *args) :
    """
#    """Return a dictionary with counts of occurrences as value for each key."""
"""

    #Initialize an empty dictionary: cols_count
    cols_count = {}

    # Iterate over column names in args
    for col_name in args :

        # Extract column from DataFrame: col
        col = df[col_name]

        # Iterate over the column in DataFrame
        for i in col :

            # If entry is in cols_count, add 1
            if i in cols_count.keys() :
                cols_count[i] += 1

            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[i] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)
"""



""" Lambda Functions"""

raiseToThePowerV2 = lambda x, y : x ** y
print(raiseToThePowerV2(2,4))

""" Anonymous Functions """

nums = [48, 6, 35, 2]

squareAll = map(lambda nums : num ** 2, nums)

print(squareAll)
print((list(squareAll)))        # Note how the list function must be used here, otherwise it just returns the "map function"


""" Writing a lambda function you already know """

# Define echo_word as a lambda function: echo_word
echo_word = (lambda a, b: a * b)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)

""" Map() and lambda functions """

# Create a list of strings: spells
spells = ['protego', 'accio', 'expecto patronum', 'legilimens']

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda a : a + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
print(shout_spells_list)

""" Filter() and lambda functions """

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda a : len(a) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)

""" Reduce() and lambda functions """

from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda a, b : a + b, stark)

# Print the result
print(result)

""" Introduction to Error Handling """

def sqrt(x) :
    """Returns the square root of a number"""
    try :
        return x ** 0.5
    except :
        print("You must enter a int or float")
print(sqrt(4))
print(sqrt('4'))        # Notice how the exception is handled



"""Except Type Error"""

def sqrt2(x) :
    """Returns the square root of a number"""
    try :
        return x ** 0.5
    except TypeError:
        print("You must enter a int or float")
print(sqrt2(5))
print(sqrt2('5'))        # Notice how the exception is handled

""" If Statements and Exception Handling"""

def sqrt3(x) :
    """Returns the square root of a number"""
    if x < 0 :
        raise ValueError('x must be a positive int or float')
    try :
        return x ** 0.5
    except TypeError:
        print("You must enter a int or float")

# print(sqrt3(-5))        # Notice how the exception is handled

""" Error handling with try-except """

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''

    # Add exception handling with try-except
    try :
        # Concatenate echo copies of word1 using *: echo_word
        echo_word += word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except :
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")

""" Error handling by raising an error """

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)


""" Bringing it all together (1)
This is awesome! You have now learned how to write anonymous functions using lambda, how to pass lambda functions as 
arguments to other functions such as map(), filter(), and reduce(), as well as how to write errors and output custom error 
messages within your functions. You will now put together these learnings to good use by working with a Twitter dataset.
 Before practicing your new error handling skills; in this exercise, you will write a lambda function and use filter()
  to select retweets, that is, tweets that begin with the string 'RT'.
To help you accomplish this, the Twitter data has been imported into the DataFrame, tweets_df. Go for it!"""

"""
# Select retweets from the Twitter DataFrame: result
result = filter(lambda x : x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
"""

""" Bringing it all together (2)
Sometimes, we make mistakes when calling functions - even ones you made yourself. But don't fret! In this exercise, 
you will improve on your previous work with the count_entries() function in the last chapter by adding a try-except 
block to it. This will allow your function to provide a helpful message when the user calls your count_entries() function 
but provides a column name that isn't in the DataFrame.

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided.
"""

"""
# Define count_entries()
def count_entries(df, col_name='lang'):
    """
"""Return a dictionary with counts of
    occurrences as value for each key."""
"""
    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try :
        # Extract column from DataFrame: col
        col = df[col_name]

        # Iterate over the column in DataFrame
        for entry in col:

            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except :
        'The DataFrame does not have a ' + col_name + ' column.'

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)
"""

"""Bringing it all together (3)
In the previous exercise, you built on your function count_entries() to add a try-except block. This was so that users would get helpful messages when calling your count_entries() function and providing a column name that isn't in the DataFrame. In this exercise, you'll instead raise a ValueError in the case that the user provides a column name that isn't in the DataFrame.

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. Parts of the code from your previous work are also provided."""

"""
# Define count_entries()
def count_entries(df, col_name='lang'):
    """
    """Return a dictionary with counts of
    occurrences as value for each key."""
"""
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Print result1
print(result1)"""