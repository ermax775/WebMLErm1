import statsmodels
import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

# regressor = data["model"]
# le_country = data["le_country"]
# le_education = data["le_education"]
fmodel = data["model"]
start = data["start"]
end = data["end"]

def show_predict_page():
    st.title("Agricultural Production Prediction")

    st.write("""### We need some other relevant information to forecast the sp.crop productions""")

    crop = (
        "Maize",
        "Sorghum",
        "Teff",
        "Wheat")

    factor = (
        "Temperature",
        "Precipitation/Rainfall",
        "Soil Type",
        "Others",
    )


    crop = st.selectbox("Crop Item", crop)
    factor = st.selectbox("Determinant Factor", factor)

    yr = st.slider("Years to be forecasted", 0, 15, 1, 1)

    ok = st.button("Forecast Production")
    if ok:
        # X = np.array([[country, education, yr ]])
        # X[:, 0] = le_country.transform(X[:,0])
        # X[:, 1] = le_education.transform(X[:,1])
        # X = X.astype(float)
        # -- X = np.array([[ start, end, yr ]])
        # start=len(train_df + test_df),end=len(train_df + test_df) + yr-1

        prod_pred = fmodel.predict(start, end + yr - 1)
        # st.write(f"The estimated Productions are ${prod_pred:.2f}")
        st.table(prod_pred)

