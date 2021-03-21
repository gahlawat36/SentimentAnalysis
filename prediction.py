import pickle
import numpy as np
from processing import text_processing

review_vect = pickle.load(open('bow_text.pkl', 'rb'))
summary_vect = pickle.load(open('bow_summary.pkl', 'rb'))
classifier = pickle.load(open('rf_bow_classifier.pkl', 'rb'))


def predictions(review, summary):

    processed_review = text_processing(review)
    processed_summary = text_processing(summary)

    vectorized_review = review_vect.transform(processed_summary).toarray()
    vectorized_summary = summary_vect.transform(processed_review).toarray()

    text = np.hstack((vectorized_review, vectorized_summary))

    final_prediction = classifier.predict(text)
    return final_prediction
    # sentiment = str(final_prediction[0])
    # if sentiment == '1':
    #     return 'That looks like  a positive review'
    # else:
    #     return 'Oops that review doesnt sound good'