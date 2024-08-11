!pip install streamlit
import streamlit as st

# Your Streamlit app code here
st.title("Health Insurance Analysis")

config = {
    "include_colab_link": True,
    "title": "Health Insurance Project"
}

# Access the title using the correct key
st.title(config["title"])

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# loading the data frm csv
insurance_dataset = pd.read_csv('/content/drive/MyDrive/insurance.csv')
# first 5 rows
insurance_dataset.head(5)
# Number of rows and coulmns
insurance_dataset.shape
# getting some basic information about the datases
insurance_dataset.info()
