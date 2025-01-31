# Importing the necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = pd.read_csv('/content/tweets.csv')  # Replace 'tweets.csv' with the path to your dataset

# Preprocess the data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['target']

# Train the logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Function to predict if a tweet is a disaster tweet or not
def predict_tweet(tweet):
    tweet_vector = vectorizer.transform([tweet])
    prediction = model.predict(tweet_vector)
    if prediction[0] == 1:
        return "This is a disaster tweet."
    else:
        return "This is not a disaster tweet."

# Example usage
tweet = input("Enter the tweet:")
prediction = predict_tweet(tweet)
print(prediction)
