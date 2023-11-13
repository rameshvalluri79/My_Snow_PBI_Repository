import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Orange")
streamlit.text(fruityvice_response)

