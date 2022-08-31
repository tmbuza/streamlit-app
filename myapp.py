


import yfinance as yf
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


sns.set_style("whitegrid")

df = sns.load_dataset('iris')


"""
## DataFrames Structure
"""
st.dataframe(df.head())

"""
## Tables
"""
st.table(df.head())


"""
## Scatter with Seaborn
"""
fig = sns.FacetGrid(df, hue ="species",
              height = 6).map(plt.scatter,
                              'sepal_length',
                              'petal_length').add_legend()

# fig, ax = plt.subplots()
# ax.scatter(df.loc[0:10, ['Sepal_Length', 'Petal_Length']])
st.pyplot(fig)


"""
## Congratulations for reaching this end!
"""
st.balloons()
