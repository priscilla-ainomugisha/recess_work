from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url= 'https://xeno-canto.org/explore?query=since:31&dir=0&order=xc/'
response = requests.get(url)

# Get title of the website
soup = BeautifulSoup(response.content,'html.parser')
title = soup.find('title')

print(title)

# response headers
print(response.headers)

# checking the status code for the HTTPP request we made 
print('Status code\n',response.status_code)

print('\n---\n')
print('================================')
# printing the webpage content
print('SOUP OBJECT\n')
print('content of the website\n',response.content[:2000] )

soup_object = BeautifulSoup(response.content, features="html.parser")

# Uncomment the below line and look into the contents of soup_object
print(soup_object)
print('================================')
print('Table data \n')
data_table = soup_object.find_all('table', 'results')[0]

# Uncomment the below line and look into the contents of data_table
print(data_table)

print('================================')
all_values = data_table.find_all('tr')
print(all_values[:10]) # Prints the first 10 captured tag elements

print('================================================================================================')
xeno_canto_df= pd.DataFrame(columns = ['Common_name', 'scientific_name', 'Duration','Recordist','Date','Time','Country','Location','Elev','Type','Remarks','Actions','Cat.nr']) # Create an empty dataframe
ix = 0 # Initialise index to zero

for row in all_values[1:]:
    values = row.find_all('td') # Extract all elements with tag <td>
    # Pick only the text part from the <td> tag
    Common_name= values[0].text
    scientific_name= values[1].text
    Duration= values[2].text
    Recordist = values[3].text
    Date = values[4].text
    Time = values[5].text
    Country = values[6].text
    Location = values[7].text
    Elev = values[8].text
    Type = values[9].text
    Remarks = values[10].text
    Actions = values[11].text
    Cat_nr=values[12].text

    xeno_canto_df.loc[ix] = [Common_name, scientific_name, Duration, Recordist, Date, Time , Country , Location , Elev , Type , Remarks, Actions ,Cat_nr]#store it in the datframe as a row
    ix += 1

# Print the first 5 rows of the dataframe
xeno_canto_df.head()

xeno_canto_df.to_csv('xeno_canto.csv', index=False)
"""

# opening the url
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, 'html.parser') 

print(soup.get_text())
Content to get
XC819337-file
Animal
    -common name
    -scientific name
    -
recordist
loacation
----------------------------------------------------------------
ID
Recordings
Species
SubSpecies
Recordist
Recording Time
REcords to GBIF"""
"""
# Getting the data from the page
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'new-species'}):
    new_species=a.find('div', attrs={'class':'new-species'})
    xc_mini_audio=a.find('div', attrs={'class':'xc-mini-audio'})
    common_name=a.find('div', attrs={'class':'common-name'})
    scientific_name=a.find('div', attrs={'class':'sci-name'})
    new_species.append(new_species.text)
    xc_mini_audio.append(xc_mini_audio.text)
    common_name.append(common_name.text) 
    scientific_name.append(scientific_name.text)
# Assignment day 12
# Extract all bird species from this website https://xeno-canto.org/and genrate 
# the csv file for the JSON format the bird species, family and more 
# to extract the data, we use the end point of the API to extract the data
# https://xeno-canto.org/api/2/recordings https://xeno-canto.org/api/2/recordings
"""