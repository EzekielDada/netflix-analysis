# Netflix Data Analysis - R Visualization
# Replicates the genre chart from the Python analysis using ggplot2

library(tidyverse)

# Load the renamed dataset
netflix_shows_movies <- read.csv("Netflix_shows_movies.csv", stringsAsFactors = FALSE)

# Parse individual genres from the comma-separated listed_in column
genres_df <- netflix_shows_movies %>%
  select(listed_in) %>%
  separate_rows(listed_in, sep = ",") %>%
  mutate(listed_in = trimws(listed_in)) %>%
  rename(genre = listed_in)

# Count and keep top 15 genres
top_genres <- genres_df %>%
  count(genre, name = "count") %>%
  arrange(desc(count)) %>%
  slice_head(n = 15)

print(top_genres)

# Build the bar chart
p <- ggplot(top_genres, aes(x = reorder(genre, count), y = count)) +
  geom_col(fill = "#E50914", width = 0.7) +
  coord_flip() +
  labs(
    title = "Most Watched Genres on Netflix",
    x = "Genre",
    y = "Number of Titles"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", hjust = 0.5),
    axis.text = element_text(color = "black")
  )

ggsave("netflix_genres_r.png", plot = p, width = 10, height = 6, dpi = 300)
print("Chart saved as netflix_genres_r.png")
