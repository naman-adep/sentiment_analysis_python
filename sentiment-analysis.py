#Import textblob module
from textblob import TextBlob

#Enter the text whose sentiment is to be found
analysis =TextBlob("She is really talented. Perfect example of beauty with brain.")

#Calculate the Sentiment Polarity
print(analysis.sentiment.polarity)

#Calculate the Sentiment Subjectivity
analysis.sentiment.subjectivity