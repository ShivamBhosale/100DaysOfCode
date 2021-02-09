""" Sentiment Analysis using textblob """
from textblob import TextBlob
from newspaper import Article

url = input("Enter the url of the article to run the analysis:\n")

article=Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)


blob = TextBlob(text)
sentiment = blob.sentiment.polarity 
""" -1 To 1 (Bad --> Good) """
print(sentiment)

if sentiment == 0:
    print("The content of the article looks neutral")
elif (0<sentiment < 0.5 ):
    print("The Article is some-what positive")
elif sentiment >= 0.5:
    print("The Article is Postive")
elif sentiment <= -0.5:
    print("The Article is Negative")
elif (-0.5 < sentiment < 0):
    print("The Article is some-what negative ")