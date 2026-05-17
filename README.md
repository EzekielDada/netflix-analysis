# Netflix Data Analysis

## Overview
This project analyzes Netflix's dataset of shows and movies to derive insights on genres, ratings, content types, and trends. The analysis includes data preparation, cleaning, exploration, statistical analysis, and visualizations using Python and R.

## Project Structure
```
├── netflix_analysis.py        # Main Python analysis script
├── netflix_analysis.R         # R visualization script
├── netflix_data.csv           # Netflix dataset
├── netflix_visualizations.png # Python-generated visualizations
├── netflix_genres_r.png       # R-generated genre visualization
└── README.md                  # This file
```

## Dataset Description
The Netflix dataset contains the following columns:
- `show_id`: Unique identifier for each title
- `type`: Movie or TV Show
- `title`: Name of the title
- `director`: Director(s) of the title
- `cast`: Main cast members
- `country`: Country/countries of origin
- `date_added`: Date added to Netflix
- `release_year`: Year the title was released
- `rating`: Content rating (TV-MA, PG-13, etc.)
- `duration`: Length of content
- `listed_in`: Genres/categories
- `description`: Brief description

## Requirements

### Python Requirements
- pandas
- numpy
- matplotlib
- seaborn

Install using:
```bash
pip install pandas numpy matplotlib seaborn
```

### R Requirements
- tidyverse
- ggplot2
- stringr

Install using:
```R
install.packages(c("tidyverse", "ggplot2", "stringr"))
```

## How to Run

### Python Analysis
Navigate to the project directory and run:
```bash
python netflix_analysis.py
```

**Output:**
- Console output with data exploration, statistics, and analysis
- `netflix_visualizations.png` containing 4 visualizations:
  1. Top 15 Genres
  2. Content Rating Distribution
  3. Movie vs TV Show Distribution
  4. Content Added Over Years

### R Visualization
Run in R or RStudio:
```R
source('netflix_analysis.R')
```

**Output:**
- `netflix_genres_r.png` - Top 15 Genres visualization

## Analysis Summary

### Data Cleaning
- Handled missing values by replacing with 'Unknown' or 'Not Rated'
- Preserved data integrity throughout the cleaning process

### Key Findings
- Dataset includes both Movies and TV Shows
- Contains titles from multiple countries and years
- Diverse range of ratings and genres
- Growth in content addition over time

### Visualizations
1. **Top Genres**: Bar chart showing the 15 most common genres
2. **Rating Distribution**: Distribution of content across different ratings
3. **Content Type**: Pie chart comparing Movies vs TV Shows
4. **Timeline**: Trend of content added to Netflix over years

### Statistical Metrics
- Average and median release year
- Most common rating
- Number of unique countries and genres
- Top 10 countries by content volume

## File Descriptions

### netflix_analysis.py
Comprehensive Python script that performs:
- Data loading and copying
- Missing value handling
- Data exploration with descriptive statistics
- Multiple visualizations using Matplotlib and Seaborn
- Statistical analysis

### netflix_analysis.R
R script that performs:
- Data loading
- Genre parsing and counting
- ggplot2 visualization of top genres
- Professional formatted output

## Results Interpretation

**Genre Analysis**: Indicates which genres are most represented on Netflix, useful for content strategy and user recommendations.

**Rating Distribution**: Shows which content ratings dominate the platform, reflecting the audience demographics Netflix targets.

**Content Type Split**: Displays the proportion of Movies vs TV Shows, showing Netflix's content mix.

**Timeline Analysis**: Reveals how Netflix's content library has grown and evolved over time.

## Notes
- Some entries have missing values in director, cast, or country fields; these are handled appropriately
- Genres are parsed from the comma-separated `listed_in` column
- Analysis is based on the dataset snapshot provided
