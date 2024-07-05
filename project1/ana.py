import streamlit as st 
from textblob import TextBlob 
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import cleantext
import matplotlib.pyplot as plt

#Lets just get the dataset 

df = pd.read_csv("Review.csv")

analyzer = sentimentIntensityAnalyzer()

sentiment_scores = []
blob_subj = []
for review in review_text:
    sentiment_scores.append(analyzer.polarity_scores(review)["compound"])
    blob = textblob(review)
    blob_subj.append(blob.subjectivity)

# Classify sentiment based on the VADER scores

sentiment_classes = []
for sentiment_scores in sentiment_scores:
    if sentiment_scores > 0.8:
        sentiment_classes.append("highly positive")
    elif sentiment_scores > 0.4:
        sentiment_classes.append("positive")
    elif sentiment_scores <= 0.4:
        sentiment_classes.append("neutral")
    elif sentiment_scores < -0.4:
        sentiment_classes.append("negative")
    else:
        sentiment_classes.append("highly negative")

st.title("Sentiment Analysis On Customer Feedback")

user_input = st.text_area("Enter the Feedback:")
blob = Textblob(user_input)

user_sentimwnt_score = analyzer.polarity_scores(user_input)['coompound']
user_sentiment_score = analyzer.polarity_scores (user_input) ['compound']

if user_sentiment_score > 0.8:
    user_sentiment_class = "highly positive"
elif user_sentiment_score > 0.4:
    user_sentiment_class = "positive"
elif -0.4 <= user_sentiment_score <= 0.4:
    user_sentiment_class = "neutral"
elif user_sentiment_score < -0.4:
    user_sentiment_class = "negative"
else:
    user_sentiment_class = "highly megative"

    st.write("** VADER Sentiment CLass: **", user_sentiment_class,"**Vader Sentiment Scores: **", user_sentiment_score)
    st.write("**TextBlob Polaritty **", blob.sentiment.polarity, "**TextBlob Subjectivity: **", blob.sentiment.subjectivity)

    pre = st.wtext_input('Clean Text: ')
    if pre:
        st.write (cleantext.clean(pre, cleanall= False , extra_spaces = True , stopwords = True , lowercase = True ,numbers = True ,punct = True))
    else:
        st.write("No Text is sbeen provided from the user for cleaning.")

st.subheader("Graphical Representation of the Data")
plt.figure(figsize=(10,6))

sentiment_scores_by_class = {k: [] for k in set(sentiment_classes)}
for sentiment_scores, sentiment_class in zip(sentiment_scores, sentiment_classes):
    sentiment_scores_by_class[sentiment_class].append(sentiment_scores)

for sentiment_class, scores in sentiment_scores_by_class.items():
    plt.hist(scores , label=sentiment_class, alpha = 0.5)

plt.xlabel("sentiment_scores")
plt.ylabel("count")
plt.title("score distribution by class")
plt.legend()
st.pyplot(plt)

df["sentiment Class"] = sentiment_classes
df["sentiment score"] = sentiment_classes
df["subjectivity"] = blob_subj

new_df = df[["score", "text", "sentiment Score", "Sentiment Class" , "Subjectivity"]]
st.subheader("Input Datframe")
st.dataframe(new_df.head(10), use_container_width = True)
             