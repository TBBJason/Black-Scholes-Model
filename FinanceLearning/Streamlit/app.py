import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import plotly.graph_objects as go

# Setting up the user input section
st.write("""
# Black-Scholes Model
Hello *world!*
""")
st.sidebar.title("Input Section")
stock = st.sidebar.number_input("Enter Current Stock Price", value=100.00,step=1.00)

strike = st.sidebar.number_input("Enter Strike Price Of Option", value=100.00,step=1.00)

time = st.sidebar.number_input("Time To Expiration of Option (in years)", value=1.00, step=0.5)

risk = st.sidebar.number_input("Risk-free Interest Rate (annualized)", value=0.5, step=0.01)

volatility = st.sidebar.number_input("Volatility Of The Underlying Asset (Annualized)",value=3.0, step=0.5) 

X = np.arange(stock-25, stock+25, 1)
Y = np.arange(strike-25,strike+25, 1)

X, Y = np.meshgrid(X,Y)

def bs(stock, strike):
    d_1 = (np.log(stock/strike) + (risk + volatility**2) * time) / (volatility * np.sqrt(time))
    d_2 = d_1 - (volatility * np.sqrt(time))

    call = stock * norm.cdf(d_1) - (strike * (np.exp)(-risk*time)*norm.cdf(d_2))
    put = (strike * np.exp(-risk * time) * norm.cdf(-d_2) - stock * norm.cdf(-d_1)) 
    return call
Call = bs(X, Y)

fig = go.Figure(data=[go.Surface(z=Call, x=X, y=Y, colorscale='Viridis')])
fig.update_layout(
    title='Black-Scholes Call Option Pricing',
    scene=dict(
        xaxis_title='Underlying Asset Price (S)',
        yaxis_title='Strike Price (K)',
        zaxis_title='Call Option Price'
    ),
)

# Display the plot in Streamlit
st.plotly_chart(fig)