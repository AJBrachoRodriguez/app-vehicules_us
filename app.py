# libraries
import pandas as pd
import streamlit as st
import plotly.express as px

## load the dataset
df = pd.read_csv("https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv")

## title the app
st.header('Car Sales Dashboard')

## vehicles types by manufacturer
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
fig = px.histogram(df, x='manufacturer', color='type',title = 'Vehicles types by manufacturer')
# display the figure with streamlit
st.write(fig)

## condition by the year of the model
fig = px.histogram(df, x='model_year', color='condition',title = 'Condition by the year of the model')
# display the figure with streamlit
st.write(fig)

## compare price distribution between manufacturers: the user must pick them
# 1. obtain the list of all the manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# 2. get the user's input from a dropdown menu for manufacturer 1
manufacturer_1 = st.selectbox(
    label = 'Select manufacturer 1', # title of the select box
    options = manufac_list, # options listed in the select box
    index = manufac_list.index('chevrolet') # default pre-selected option
                            )
# 3. get the user's input from a dropdown menu for manufacturer 2
manufacturer_2 = st.selectbox(
    label = 'Select manufacturer 2', # title of the select box
    options = manufac_list, # options listed in the select box
    index = manufac_list.index('hyundai') # default pre-selected option
                            )
# 4. filter the dataframe
mask_filter = ((df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2))
df_filtered = df[mask_filter]
# 5. add a checkbox if a user wants to normalize the histogram 
normalize = st.checkbox('Normalize histogram', value = True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
# 6. create a plotly histogram figure
fig = px.histogram(
                    df_filtered,
                    x = 'price',
                    nbins = 30,
                    color = 'manufacturer',
                    histnorm = histnorm,
                    barmode = 'overlay'
                    )
# 7. display the figure with streamlit
st.write(fig)

#st.dataframe(df)
print("Ok!")