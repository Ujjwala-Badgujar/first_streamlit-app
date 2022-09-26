import streamlit
streamlit.title('My parents New Healthy Dinner')
streamlit.header('Breakfast favourites')
streamlit.text('✨Vada Sambhar')
streamlit.text('✌Omlet')
streamlit.text('🤞Dosa')
streamlit.text('😁uttappa')
streamlit.header('🎂🎂Build your own fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
