import zipfile
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# -------------------------------------------------------
# STEP 1: DATA PREPARATION
# -------------------------------------------------------

# Unzip the dataset and rename it to Netflix_shows_movies
with zipfile.ZipFile('Netflix_Analysis.zip', 'r') as z:
    z.extract('netflix_data.csv', '.')

if os.path.exists('Netflix_shows_movies.csv'):
    os.remove('Netflix_shows_movies.csv')
os.rename('netflix_data.csv', 'Netflix_shows_movies.csv')

netflix_shows_movies = pd.read_csv('Netflix_shows_movies.csv')

print("Dataset loaded: Netflix_shows_movies.csv")
print(f"Rows: {netflix_shows_movies.shape[0]}, Columns: {netflix_shows_movies.shape[1]}\n")


# -------------------------------------------------------
# STEP 2: DATA CLEANING
# -------------------------------------------------------

print("Missing values before cleaning:")
print(netflix_shows_movies.isnull().sum()[netflix_shows_movies.isnull().sum() > 0])

netflix_shows_movies['director'] = netflix_shows_movies['director'].fillna('Unknown')
netflix_shows_movies['cast'] = netflix_shows_movies['cast'].fillna('Unknown')
netflix_shows_movies['country'] = netflix_shows_movies['country'].fillna('Unknown')
netflix_shows_movies['date_added'] = netflix_shows_movies['date_added'].fillna('Unknown')
netflix_shows_movies['rating'] = netflix_shows_movies['rating'].fillna('Not Rated')

print("\nMissing values after cleaning:")
print(netflix_shows_movies.isnull().sum()[netflix_shows_movies.isnull().sum() > 0])
print("No remaining missing values.\n")


# -------------------------------------------------------
# STEP 3: DATA EXPLORATION
# -------------------------------------------------------

print("=== Dataset Overview ===")
print(netflix_shows_movies.dtypes)

print("\n=== Descriptive Statistics ===")
print(netflix_shows_movies.describe(include='all'))

print("\n=== Content Type Counts ===")
print(netflix_shows_movies['type'].value_counts())

print("\n=== Top 10 Ratings ===")
print(netflix_shows_movies['rating'].value_counts().head(10))

print("\n=== Release Year Summary ===")
print(netflix_shows_movies['release_year'].describe())


# -------------------------------------------------------
# STEP 4: DATA VISUALIZATION
# -------------------------------------------------------

sns.set_style("whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Netflix Data Analysis", fontsize=15, fontweight='bold', y=1.01)

# --- Chart 1: Most Watched Genres (Seaborn) ---
genres_list = []
for entry in netflix_shows_movies['listed_in']:
    genres_list.extend([g.strip() for g in str(entry).split(',')])

genre_counts = pd.Series(genres_list).value_counts().head(15).reset_index()
genre_counts.columns = ['genre', 'count']

sns.barplot(data=genre_counts, y='genre', x='count', ax=axes[0, 0], palette='Reds_r')
axes[0, 0].set_title('Most Watched Genres', fontweight='bold')
axes[0, 0].set_xlabel('Number of Titles')
axes[0, 0].set_ylabel('')

# --- Chart 2: Ratings Distribution (Matplotlib) ---
rating_counts = netflix_shows_movies['rating'].value_counts()
axes[0, 1].bar(rating_counts.index, rating_counts.values, color='#E50914', edgecolor='black')
axes[0, 1].set_title('Ratings Distribution', fontweight='bold')
axes[0, 1].set_xlabel('Rating')
axes[0, 1].set_ylabel('Count')
axes[0, 1].tick_params(axis='x', rotation=45)

# --- Chart 3: Movies vs TV Shows (Pyplot pie) ---
type_counts = netflix_shows_movies['type'].value_counts()
axes[1, 0].pie(type_counts.values, labels=type_counts.index,
               autopct='%1.1f%%', colors=['#E50914', '#221F1F'], startangle=90)
axes[1, 0].set_title('Movies vs TV Shows', fontweight='bold')

# --- Chart 4: Content Added Per Year (Seaborn line) ---
year_added = (
    netflix_shows_movies[netflix_shows_movies['date_added'] != 'Unknown']['date_added']
    .str.extract(r'(\d{4})')[0]
    .dropna()
    .astype(int)
)
year_df = year_added.value_counts().sort_index().reset_index()
year_df.columns = ['year', 'count']

sns.lineplot(data=year_df, x='year', y='count', ax=axes[1, 1],
             color='#E50914', marker='o', linewidth=2)
axes[1, 1].set_title('Content Added Per Year', fontweight='bold')
axes[1, 1].set_xlabel('Year')
axes[1, 1].set_ylabel('Titles Added')

plt.tight_layout()
plt.savefig('netflix_visualizations.png', dpi=300, bbox_inches='tight')
print("Visualizations saved to netflix_visualizations.png")
plt.show()


# -------------------------------------------------------
# STEP 5: STATISTICAL ANALYSIS
# -------------------------------------------------------

print("\n=== Statistical Analysis ===")
print(f"Average release year     : {netflix_shows_movies['release_year'].mean():.1f}")
print(f"Median release year      : {netflix_shows_movies['release_year'].median():.0f}")
print(f"Most common release year : {netflix_shows_movies['release_year'].mode()[0]}")
print(f"Most common rating       : {netflix_shows_movies['rating'].mode()[0]}")
print(f"Unique countries         : {netflix_shows_movies['country'].nunique()}")
print(f"Total unique genres      : {pd.Series(genres_list).nunique()}")

countries_list = []
for entry in netflix_shows_movies['country']:
    if entry != 'Unknown':
        countries_list.extend([c.strip() for c in str(entry).split(',')])

print("\nTop 10 Countries by Content:")
print(pd.Series(countries_list).value_counts().head(10))
