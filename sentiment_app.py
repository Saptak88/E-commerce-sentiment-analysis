import streamlit as st
import joblib
import pandas as pd
import re 
import nltk 
from nltk.corpus import stopwords

# Load the saved model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Streamlit app layout
st.title('Ecommerce Sentiment Analysis App')

st.write('Enter a review to analyze its sentiment:')

# Input review
review_text = st.text_area('Review')

def preprocess_text(text_data): 
    preprocessed_text = [] 
  
    for sentence in text_data: 
        # Removing punctuations 
        sentence = re.sub(r'[^\w\s]', '', sentence) 
  
        # Converting lowercase and removing stopwords 
        preprocessed_text.append(' '.join(token.lower() 
                                          for token in nltk.word_tokenize(sentence) 
                                          if token.lower() not in stopwords.words('english'))) 
  
    return preprocessed_text 
# Predict sentiment
if st.button('Analyze Sentiment'):
    # Preprocess input text
    review_preprocessed = preprocess_text([review_text])
    
    # Transform text data
    review_vectorized = vectorizer.transform(review_preprocessed)
    
    # Make prediction
    prediction = model.predict(review_vectorized)
    
    # Display result
    sentiment = 'Positive' if prediction[0] == 1 else 'Negative'
    st.write(f"Sentiment: {sentiment}")