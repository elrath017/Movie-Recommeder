# 🎬 Movie Recommendation System

A movie recommendation system that suggests similar movies based on your choice using machine learning.

## Features

- Browse and select from 5,000+ movies
- Get 5 movie recommendations similar to your choice
- View poster images for recommended movies
- Simple web interface powered by Streamlit

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
streamlit run app.py
```

Then:
1. Select a movie from the dropdown menu
2. Click "Show Recommendation"
3. View the 5 recommended movies with their posters

## Dependencies

- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning and similarity calculations
- **streamlit**: Web application framework
- **requests**: HTTP requests for TMDB API
- **matplotlib**: Data visualization

See `requirements.txt` for complete list.

## About the Data

- Uses The Movie Database (TMDB) with 5,000 movies
- Analyzes genres, keywords, cast, and director information
- Compares movies to find similar ones