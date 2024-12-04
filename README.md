**E-COMMERCE SENTIMENT ANALYSIS**

The objective of this project is to analyze customer reviews and ratings 
on E-COMMERCE platforms to understand the sentiment expressed by users. This 
analysis will help in identifying the overall perception of products, 
highlighting areas for potential improvement.

The proposed system aims to address the challenge of predicting the sentiment of customer reviews on Flipkart, categorizing them as positive or negative. This involves 
leveraging data analytics and machine learning techniques to accurately classify the sentiment expressed in the reviews based on the provided ratings. The solution will consist 
of the following components:

**Data Collection:**

Utilize historical data of user reviews and ratings from Flipkart, focusing on the text reviews and star ratings.

**Data Preprocessing:**

The text data is preprocessed by removing punctuations, converting text to lowercase, and removing stopwords.

The TF-IDF vectorizer is used to convert the preprocessed text data into numerical representations.

Created a label column where reviews with ratings >= 4 are marked as positive (1), and others are marked as negative (0).

**Machine Learning Algorithm:**

A Decision Tree Classifier is implemented to classify the reviews as positive or negative.

**Deployment:**

The machine learning model is deployed using a Streamlit user interface to provide real-time sentiment analysis for new reviews.

**Evaluation:**

The model is evaluated on the accuracy of the model on both the training and test datasets to ensure it generalizes well to n ew data.

**Result:**

Training Accuracy: 0.98 Test Accuracy: 0.84.

**Screenshots**

![image](https://github.com/user-attachments/assets/2429219b-2ea8-4231-bb85-40d0499514b6)

![image](https://github.com/user-attachments/assets/c9875b47-5fbd-417d-b7ad-e347f4d3d7d2)

**FUTURE SCOPE**

The sentiment analysis system has laid a strong foundation for understanding customer feedback, 
but there are several avenues for enhancement and expansion that could significantly improve its 
functionality and impact:
a. Integrating data from customer support interactions, chat logs, and social media could provide 

a more comprehensive understanding of customer sentiment and issues.

b. Exploring advanced machine learning techniques such as BERT, GPT, or other Transformerbased models could improve sentiment classification accuracy and handle complex sentiment 
nuances better.

