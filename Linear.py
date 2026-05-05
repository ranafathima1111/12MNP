import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv("data.csv")
x = df[['HoursStudied']]
y = df['ExamScore']
