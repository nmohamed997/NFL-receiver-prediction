import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for NFL wide receiver stats for 2023
url = "https://www.pro-football-reference.com/years/2023/receiving.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the stats
table = soup.find('table', {'id': 'receiving'})
df = pd.read_html(str(table))[0]

# Save the data to a CSV file
df.to_csv('nfl_wide_receivers_2023.csv', index=False)
