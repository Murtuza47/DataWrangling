from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"
df = pd.read_html(url)[1]
newdf = df.drop(
  [
    "Road Network Length (in km) in 2013[26]", 
    "Number of People Killed per Billion km[27]", 
    "Number of Seriously Injured in 2017/2018[27]"], axis=1).rename(columns={
  "Area (thousands of km2)[21]": "Area",
  "Population in 2018[22]": "Population",
  "GDP per capita in 2018[23]": "GDP per capita",
  "Population density (inhabitants per km2) in 2017[24]": "Population density",
  "Vehicle ownership (per thousand inhabitants) in 2016[25]":"Vehicle ownership",
  "Total Road Deaths in 2018[27]": "Total road deaths",
  "Road deaths per Million Inhabitants in 2018[27]":"Road deaths per Million Inhabitants"
}).sort_values(by=["Road deaths per Million Inhabitants"])
newdf['Year'] = 2018

newdf.to_csv("lsr.csv")
