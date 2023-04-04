import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import warnings
warnings.simplefilter(action='ignore', category=Warning)


df = pd.read_csv('IMDB Dataset.csv')

df['review'] = df['review'].str.lower()
df['review'] = df['review'].str.replace('[^\w\s]','')
df['review'] = df['review'].str.replace('\d+', '')
df['review'] = df['review'].str.strip()

X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)


model = MultinomialNB()
model.fit(X_train_vect, y_train)


y_pred = model.predict(X_test_vect)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


new_reviews = ['This movie is great!', 'This movie is terrible!']
new_reviews_vect = vectorizer.transform(new_reviews)
new_reviews_pred = model.predict(new_reviews_vect)
print("New reviews predicted sentiment")
for i in range(len(new_reviews)):
    print(f"review: {new_reviews[i]}\npredicted Sentiment: {new_reviews_pred[i]}")
