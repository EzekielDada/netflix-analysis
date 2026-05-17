# Netflix Data Analysis - R Visualization
# Genre Analysis with ggplot2

library(tidyverse)
library(stringr)

# Load data
netflix_data <- read.csv('netflix_data.csv', stringsAsFactors = FALSE)

# Parse genres from listed_in column
genres_df <- netflix_data %>%
  select(listed_in) %>%
  separate_rows(listed_in, sep = ",") %>%
  mutate(listed_in = str_trim(listed_in)) %>%
  rename(genre = listed_in)

# Count genres
genre_counts <- genres_df %>%
  group_by(genre) %>%
  summarise(count = n(), .groups = 'drop') %>%
  arrange(desc(count)) %>%
  slice_head(n = 15)

# Visualization
p <- ggplot(genre_counts, aes(x = reorder(genre, count), y = count)) +
  geom_col(fill = "#E50914", color = "#221F1F", width = 0.7) +
  coord_flip() +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    plot.background = element_rect(fill = "#221F1F", color = NA),
    panel.background = element_rect(fill = "#221F1F", color = NA),
    text = element_text(color = "white"),
    axis.text = element_text(color = "white", size = 10),
    panel.grid.major.x = element_line(color = "gray40", size = 0.3)
  ) +
  labs(
    title = "Top 15 Genres on Netflix",
    x = "Genre",
    y = "Number of Titles"
  )

ggsave('netflix_genres_r.png', plot = p, width = 10, height = 6, dpi = 300)
print("Genre visualization saved as 'netflix_genres_r.png'")
print(genre_counts)
