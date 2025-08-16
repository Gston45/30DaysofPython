#Exercices
import pandas as pd
#1 Read the hacker_news.csv file 

df = pd.read_csv('hacker_news.csv')

#2 Get the first five rows

print(df.head())

#3 Get the last five rows

print(df.tail())

# 4. Get the title column as pandas series

titles = df['title']
print("\nTitle column:\n", titles.head())

# 5. Count the number of rows and columns
print("\nShape (rows, columns):", df.shape)

# Filter the titles which contain 'python'
python_titles = df[titles.str.contains("python", case=False, na=False)]
print("\nTitles containing 'python':\n", python_titles['title'])

# Filter the titles which contain 'JavaScript'
js_titles = df[titles.str.contains("javascript", case=False, na=False)]
print("\nTitles containing 'JavaScript':\n", js_titles['title'])

# 6. Explore and make sense of the data
print("\n--- Exploration ---")
print("Number of Python-related posts:", len(python_titles))
print("Number of JavaScript-related posts:", len(js_titles))
print("Most common words in titles:\n", titles.str.lower().str.split(expand=True).stack().value_counts().head(20))
