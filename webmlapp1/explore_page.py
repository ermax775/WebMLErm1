import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import pickle
# from predict_page import show_explore_page
# from predict_page import load_model

# def load_model():
#     with open('saved_steps.pkl', 'rb') as file:
#         data = pickle.load(file)
#     return data


# data1 = load_model()
# fmodel = data1["model"]
# start = data1["start"]
# end = data1["end"]


@st.cache
def load_data():
    df = pd.read_csv("sampledata1.csv")
    # df = pd.read_csv("sampledata1.csv", parse_dates=['Year'], index_col='Year')
    df = df[["Year", "TempMean", "PrecipMean", "Product"]]
    df = df[df["Product"].notnull()]
    df = df.dropna()
    # df = df[df["Employment"] == "Employed full-time"]
    # df = df.drop("Employment", axis=1)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Agri Products Productions")

    st.write(
        """
    ### Sample Survey and previous recorded data from WB (2020)
    """
    )

    # data = df["Country"].value_counts()
    data = df["Year"]

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from a specific crop item""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Production Based On TempMean
    """
    )

    # data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    data = df.groupby(["TempMean"])["Product"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Production Based On PrecipMean
    """
    )

    data = df.groupby(["PrecipMean"])["Product"].mean().sort_values(ascending=True)
    st.line_chart(data)
