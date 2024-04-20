import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Assuming you have a CSV file with labeled data
data = pd.read_csv('labeled_journal_entries.csv')

# Preprocess description text (example using NLTK)
from nltk.tokenize import word_tokenize
analyzer = SentimentIntensityAnalyzer()

def preprocess_text(text):
  tokens = word_tokenize(text.lower())  # Lowercase and tokenize
  filtered_words = [w for w in tokens if w.isalpha()]  # Remove punctuation
  sentiment = analyzer.polarity_scores(text)  # Sentiment analysis
  return " ".join(filtered_words), sentiment['compound']

data['description_processed'], data['sentiment'] = zip(*data['description'].apply(preprocess_text))

# Feature engineering based on transaction data and text analysis
data['has_keywords'] = data['description_processed'].apply(lambda x: any(keyword in x[0] for keyword in ['urgent', 'cash', 'off-books']))
data['num_unique_vendors'] = data.groupby('entry_id')['vendor'].transform('nunique')  # Vendors per entry
data['is_large_amount'] = data['amount'].apply(lambda x: len(str(x)) > 8)
data['is_holiday'] = data['date'].apply(lambda x: x in holidays)  # Replace with holiday check

# Combine features and target variable
X = data[['has_keywords', 'sentiment', 'num_unique_vendors', 'is_large_amount', 'is_holiday']]
y = data['is_suspicious']

# Train-test split and model training (same as before)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# You can now evaluate the model's performance and use it to predict suspicious entries
#specific vendors/recipients flagged for past concerns.