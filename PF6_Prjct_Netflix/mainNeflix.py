# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {'years': years, 'durations': durations}

# Print the dictionary
print(movie_dict)
print('\n')

# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame
print(durations_df)

# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt

fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(years, durations)

# Create a title
# Strings
xlab = 'release_years'
ylab = 'durations'
title = 'Netflix Movie Durations 2011-2020'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

# Show the plot
# plt.show()
plt.clf()

"""
# Read in the CSV as a DataFrame
netflix_df = pd.read_csv('datasets/netflix_data.csv')

# Print the first five rows of the DataFrame
print(netflix_df.head())

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type']=='Movie']


# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset.head())

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset[['release_year']],netflix_movies_col_subset[['duration']])

# Create a title
plt.title('Movie Duration by Year of Release')

# Show the plot
plt.show()

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration']<60]

# Print the first 20 rows of short_movies
print(short_movies.head(n=20))

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for i, v in netflix_movies_col_subset.iterrows() :
    if v['genre'] == "Children":
        colors.append("red")
    elif v['genre'] == "Documentaries" :
        colors.append("blue")
    elif v['genre'] == "Stand-Up" :
        colors.append("green")  
    else:
        colors.append("black")

# Inspect the first 10 values in your list        
print(colors[:10]) 

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset[['release_year']], netflix_movies_col_subset[['duration']], c = colors)


# Create a title and axis labels
plt.title('Movie Duration by Year of Release')
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()


are_movies_getting_shorter = "We are not certain movies are getting shorter, as the colored scatter plot indicates that the additions of more documentaries and childrens' shows may be dragging down the average runtime of movies on netflix."

"""
# Published Workspace:
# https://app.datacamp.com/workspace/w/e9df9bf5-eed5-4135-b63f-83fc34c95c0a