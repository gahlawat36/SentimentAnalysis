import pickle
import numpy as np
from processing import text_processing

# Bog of words vectorizer model for reviews text
review_vect = pickle.load(open('bow_text.pkl', 'rb'))

# Bag of words vectorizer model for summary text
summary_vect = pickle.load(open('bow_summary.pkl', 'rb'))

# Random forest model
classifier = pickle.load(open('rf_bow_classifier.pkl', 'rb'))


def predictions(review, summary):
    ''' This function takes in the review and summary text to output final prediction'''

    # text processing function is used to pre-process the input text
    processed_review = text_processing(review)
    processed_summary = text_processing(summary)

    # Bag of Words vectorizer is used to vectorize the processed text
    vectorized_review = review_vect.transform(processed_summary).toarray()
    vectorized_summary = summary_vect.transform(processed_review).toarray()

    # stack both vectors to prepare input to the classifier
    text = np.hstack((vectorized_review, vectorized_summary))

    # final prediction
    final_prediction = classifier.predict(text)

    return final_prediction