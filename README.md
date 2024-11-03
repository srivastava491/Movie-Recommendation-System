
# Movie Recommendation System

This project implements a Movie Recommendation System using Natural Language Processing (NLP) techniques such as TF-IDF vectorization and cosine similarity to recommend movies based on user preferences. The system analyzes the plot and metadata of movies to find and suggest similar movies.

## Features

- **Content-Based Filtering**: Recommends movies similar to a given movie based on plot descriptions.
- **User-Friendly Interface**: Accepts a movie name and provides recommendations based on similarity.
- **Efficient Processing**: Uses TF-IDF and cosine similarity to ensure fast and accurate recommendations.

## Project Structure

```bash
.
├── app.py                    # Main application script
├── recommendation.py         # Recommendation system logic
├── requirements.txt          # Python dependencies
├── requirements.txt          # Python dependencies
├── movies2.csv               # Movies Dataset
└── README.md                 # Project documentation
```

## Requirements

- **Python 3.7+**
- **Pandas**
- **scikit-learn**
- **NLTK**

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Dataset

The dataset should include:
- **Movie Titles**
- **Plot Summaries**
- **Genres**

You can use publicly available datasets like [The Movies Dataset by Kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset).

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Run the Application**

   ```bash
   python app.py
   ```

3. **Get Recommendations**

   - Enter a movie name in the interface or command line.
   - The system will return a list of recommended movies based on content similarity.

## Implementation Details

### Text Preprocessing

The project uses the following text preprocessing steps to handle the movie plots:
- **Tokenization**: Break down text into individual words.
- **Lemmatization**: Convert words to their base forms.
- **Stopwords Removal**: Remove common words that don’t contribute to similarity (e.g., “the,” “and”).

### TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert the text data into numerical format. Each word in the movie plot is weighted based on its frequency in the plot and rarity across all movies.

### Cosine Similarity

Cosine similarity is applied to compute the similarity between movies based on their TF-IDF vectors. The system recommends movies with the highest cosine similarity scores to the given input.

## Example Output

Input Movie: **Tangled**

**Recommended Movies:**
1. Out of Inferno
2. The Princess and the Frog
3. Home on the Range
4. Animals United
5. Toy Story 3

## Future Improvements

- **Hybrid Recommendation System**: Combine content-based filtering with collaborative filtering for better recommendations.
- **Enhanced Metadata Usage**: Incorporate additional features such as directors, cast, and user ratings.
- **Personalized Recommendations**: Enable recommendations based on user watch history.

## References

- Scikit-learn Documentation: [TF-IDF and Cosine Similarity](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting)
