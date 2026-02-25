from textblob import TextBlob

with open('myText.txt', 'r') as file:
    text = file.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #to get the sentiment polarity from -1 to 1
print(f'Sentiment Polarity: {sentiment}')