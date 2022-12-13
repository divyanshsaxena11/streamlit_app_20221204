import streamlit
import snowflake.connector
import pandas
streamlit.title("hellow world")


# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["Snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE;")
my_catalog = my_cur.fetchall()
# put the dafta into a dataframe
df = pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
# streamlit.write(df)
# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)
# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
# use the option selected to go back and get all the info from the datab


my_cur.execute("select direct_url, price, size_list, upsell_product_desc from ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
caption= product_caption
)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])



import streamlit as sl
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Title of App
sl.write('Snowflake Warehouse Report')

sl.header('st.button')
if sl.button('hello world'):
    sl.write('why hello there')
else:
    sl.write('good bye')

# Side bar sections
sb_loyalty = sl.sidebar.selectbox('KILO-Loyalty Reports',('Warehouse Usage','Alerts'))
sb_teradata = sl.sidebar.selectbox('Teradata MIG Reports',('Warehouse Usage','Alerts'))

# KILO Loyalty
if sb_loyalty == 'Warehouse Usage':
    sl.write('warehouse usage')
    df = 1
    sl.metric('views',df,45)