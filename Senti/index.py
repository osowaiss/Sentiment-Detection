import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not downloaded
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    
    # Determine sentiment type
    if sentiment_score['compound'] >= 0.05:
        sentiment = "Positive 😀"
    elif sentiment_score['compound'] <= -0.05:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    return sentiment_score, sentiment

# Example Usage
if __name__ == "__main__":
    text = input("Enter a sentence or paragraph: ")
    scores, sentiment = analyze_sentiment(text)
    
    print("\nSentiment Scores:", scores)
    print("Overall Sentiment:", sentiment)
