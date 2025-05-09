from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Grabbing the correct table
table = soup.find_all('table')[1]

# Extracting column titles
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles[:len(table.find_all('tr')[1].find_all('td'))]]

df = pd.DataFrame(columns=world_table_titles)

# Extracting row data
rows = table.find_all('tr')
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols) == len(world_table_titles):  # Only include rows with correct number of columns
        data = [col.text.strip() for col in cols]
        df.loc[len(df)] = data

print(df)
df.to_csv(r'C:\Users\paris\OneDrive\Desktop\web_scraping\company.csv', index=False)


