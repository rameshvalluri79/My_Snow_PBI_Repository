import streamlit
streamlit.title('Oh ! My God Its My New First streamlit Message')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and BluBerry Oatmeal')
streamlit.text('🥗 Kale & Spinach Rocket meal')
streamlit.text('🐔 Hard Boiled Egg')
streamlit.text('🥑🍞 Brandy Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
