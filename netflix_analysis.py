import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Data Preparation
df = pd.read_csv('netflix_data.csv')
netflix_shows_movies = df.copy()

print("=" * 60)
print("NETFLIX DATA ANALYSIS")
print("=" * 60)

# Data Cleaning
print("\n1. DATA CLEANING")
print("-" * 60)

# Check for missing values
missing_values = netflix_shows_movies.isnull().sum()
print(f"\nMissing Values:\n{missing_values[missing_values > 0]}")

# Fill missing values
netflix_shows_movies['director'].fillna('Unknown', inplace=True)
netflix_shows_movies['cast'].fillna('Unknown', inplace=True)
netflix_shows_movies['country'].fillna('Unknown', inplace=True)
netflix_shows_movies['date_added'].fillna('Unknown', inplace=True)
netflix_shows_movies['rating'].fillna('Not Rated', inplace=True)

print("\nMissing values addressed.")

# Data Exploration
print("\n2. DATA EXPLORATION")
print("-" * 60)

print(f"\nDataset Shape: {netflix_shows_movies.shape}")
print(f"\nColumn Names and Types:\n{netflix_shows_movies.dtypes}")

# Basic statistics
print(f"\nBasic Statistics:\n{netflix_shows_movies.describe()}")

# Content type distribution
print(f"\nContent Type Distribution:\n{netflix_shows_movies['type'].value_counts()}")

# Rating distribution
print(f"\nRating Distribution:\n{netflix_shows_movies['rating'].value_counts()}")

# Release year statistics
print(f"\nRelease Year Statistics:\n{netflix_shows_movies['release_year'].describe()}")

# Data Visualization
print("\n3. DATA VISUALIZATION")
print("-" * 60)

sns.set_style("whitegrid")

# Figure 1: Most Watched Genres
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Parse genres from listed_in column
genres_list = []
for genres in netflix_shows_movies['listed_in']:
    if pd.notna(genres):
        genre_split = [g.strip() for g in str(genres).split(',')]
        genres_list.extend(genre_split)

genre_counts = pd.Series(genres_list).value_counts().head(15)

ax1 = axes[0, 0]
genre_counts.plot(kind='barh', ax=ax1, color='#E50914')
ax1.set_xlabel('Count')
ax1.set_title('Top 15 Genres on Netflix', fontsize=12, fontweight='bold')
ax1.invert_yaxis()

# Figure 2: Ratings Distribution
ax2 = axes[0, 1]
rating_counts = netflix_shows_movies['rating'].value_counts()
ax2.bar(range(len(rating_counts)), rating_counts.values, color='#221F1F')
ax2.set_xticks(range(len(rating_counts)))
ax2.set_xticklabels(rating_counts.index, rotation=45, ha='right')
ax2.set_ylabel('Count')
ax2.set_title('Content Rating Distribution', fontsize=12, fontweight='bold')

# Figure 3: Content Type Distribution
ax3 = axes[1, 0]
type_counts = netflix_shows_movies['type'].value_counts()
colors = ['#E50914', '#221F1F']
ax3.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
ax3.set_title('Movie vs TV Show Distribution', fontsize=12, fontweight='bold')

# Figure 4: Content Added Over Time
ax4 = axes[1, 1]
date_added_clean = netflix_shows_movies[netflix_shows_movies['date_added'] != 'Unknown']['date_added'].str.extract(r'(\d{4})')[0]
date_added_clean = pd.to_numeric(date_added_clean, errors='coerce').dropna().astype(int)
year_counts = date_added_clean.value_counts().sort_index()
ax4.plot(year_counts.index, year_counts.values, marker='o', color='#E50914', linewidth=2)
ax4.set_xlabel('Year')
ax4.set_ylabel('Content Added')
ax4.set_title('Netflix Content Added Over Years', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('netflix_visualizations.png', dpi=300, bbox_inches='tight')
print("\nVisualizations saved as 'netflix_visualizations.png'")
plt.show()

# Statistical Analysis
print("\n4. STATISTICAL ANALYSIS")
print("-" * 60)

print(f"\nAverage Release Year: {netflix_shows_movies['release_year'].mean():.2f}")
print(f"Median Release Year: {netflix_shows_movies['release_year'].median():.0f}")
print(f"Most Common Release Year: {netflix_shows_movies['release_year'].mode()[0]}")

print(f"\nMost Common Rating: {netflix_shows_movies['rating'].mode()[0]}")
print(f"Number of Unique Countries: {netflix_shows_movies['country'].nunique()}")
print(f"Number of Unique Genres: {len(genres_list)}")

# Top countries by content
countries_list = []
for country in netflix_shows_movies['country']:
    if pd.notna(country) and country != 'Unknown':
        country_split = [c.strip() for c in str(country).split(',')]
        countries_list.extend(country_split)

country_counts = pd.Series(countries_list).value_counts().head(10)
print(f"\nTop 10 Countries by Content:\n{country_counts}")

print("\n" + "=" * 60)
print("Analysis Complete")
print("=" * 60)
