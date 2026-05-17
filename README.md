# Netflix Data Analysis

## Overview
This project analyzes a Netflix dataset of movies and TV shows. The analysis covers data preparation, cleaning, exploration, visualization, and statistical summaries using Python and R.

## Project Files
```
├── Netflix_Analysis.zip           # Original zipped dataset
├── netflix_analysis.py            # Main Python script
├── netflix_analysis.R             # R visualization script
├── Netflix_shows_movies.csv       # Extracted and renamed dataset (generated on first run)
├── netflix_visualizations.png     # Output charts from Python
├── netflix_genres_r.png           # Genre chart from R
└── README.md
```

## Dataset Columns
| Column | Description |
|---|---|
| show_id | Unique title ID |
| type | Movie or TV Show |
| title | Title name |
| director | Director(s) |
| cast | Main cast |
| country | Country of origin |
| date_added | Date added to Netflix |
| release_year | Release year |
| rating | Content rating (e.g. TV-MA, PG-13) |
| duration | Runtime or number of seasons |
| listed_in | Genres |
| description | Short description |

---

## Requirements

### Python
- Python 3.x
- pandas, numpy, matplotlib, seaborn

```bash
pip install pandas numpy matplotlib seaborn
```

### R
- R 4.x
- tidyverse

```R
install.packages("tidyverse")
```

---

## How to Run

### Python
```bash
python netflix_analysis.py
```

The script will:
1. Unzip `Netflix_Analysis.zip` and rename the CSV to `Netflix_shows_movies.csv`
2. Clean missing values
3. Print data exploration and statistical summaries to the console
4. Save `netflix_visualizations.png` with four charts:
   - Most Watched Genres (Seaborn)
   - Ratings Distribution (Matplotlib)
   - Movies vs TV Shows pie chart (Pyplot)
   - Content Added Per Year (Seaborn)

### R
Run in R or RStudio (after the Python script has created `Netflix_shows_movies.csv`):
```R
source("netflix_analysis.R")
```

Saves `netflix_genres_r.png` — a ggplot2 bar chart of the top 15 genres.

---

## Steps Performed

### 1. Data Preparation
Used Python's `zipfile` module to extract the dataset from `Netflix_Analysis.zip` and renamed the file to `Netflix_shows_movies.csv`.

### 2. Data Cleaning
Filled missing values in `director`, `cast`, `country`, `date_added`, and `rating` columns with `'Unknown'` or `'Not Rated'`.

### 3. Data Exploration
- Checked column types and shapes
- Ran `describe()` for descriptive statistics
- Reviewed content type and rating distributions

### 4. Data Visualization (Python)
- **Most Watched Genres** — horizontal bar chart using Seaborn
- **Ratings Distribution** — bar chart using Matplotlib
- **Movies vs TV Shows** — pie chart using Pyplot
- **Content Added Per Year** — line chart using Seaborn

### 5. R Integration
Reproduced the genre chart in R using ggplot2 (tidyverse).

### 6. Statistical Analysis
- Average, median, and mode of release year
- Most common content rating
- Unique country and genre counts
- Top 10 countries by number of titles
