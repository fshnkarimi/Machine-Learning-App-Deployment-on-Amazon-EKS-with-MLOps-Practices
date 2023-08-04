from sklearn import naive_bayes
import streamlit as st 

import joblib
import time

# Load the saved model Vectorizer
imported_vectorizer = open("models/gender_model_vectorizer.pkl","rb")
cv = joblib.load(imported_vectorizer)

# Load the saved gender prediction Model
naive_bayes_model = open("models/gender_classification_model.pkl","rb")
clf = joblib.load(naive_bayes_model)

# Creating the Prediction function
def gender_prediction(data):
    vect = cv.transform(data).toarray()
    result = clf.predict(vect)
    return result   

def main():
    """Gender Classifier App"""

    st.title("Gender Classifier with Streamlit")
    html_temp = """
    <div style="background-color:purple;padding:10px">
    <h2 style="color:white;text-align:center;">Gender Classification App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    name = st.text_input("Enter Person Name")
    result = None  # Initialize the result variable outside the if block
    if st.button("Predict Gender"):
        result = gender_prediction([name])

    # Check if 'result' is not None before using it
    if result is not None:
        if result[0] == 0:
            prediction = 'Female'
        else:
            prediction = 'Male'

        st.success('Name: {} was classified as {}'.format(name.title(), prediction))

if __name__ == '__main__':
    main()
