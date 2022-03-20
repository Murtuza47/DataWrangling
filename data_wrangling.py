from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

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

Country = newdf["Country"].tolist()
GDP_Per_Capita = newdf["GDP per capita"].tolist()
Population_density = newdf["Population density"].tolist()
Total_road_deaths= newdf["Total road deaths"].tolist()
Road_deaths_per_Million_Inhabitants = newdf["Road deaths per Million Inhabitants"].tolist()

plt.bar(Country, GDP_Per_Capita)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=10)
plt.ylabel('GDP Per Capita', fontsize=10)
plt.show()

plt.bar(Country, Population_density)
plt.title('Country Vs Population density', fontsize=14)
plt.xlabel('Country', fontsize=10)
plt.ylabel('Population density', fontsize=10)
plt.show()

plt.bar(Country, Total_road_deaths)
plt.title('Country Vs Total road deaths', fontsize=14)
plt.xlabel('Country', fontsize=10)
plt.ylabel('Total road deaths', fontsize=10)
plt.show()

plt.bar(Country, Road_deaths_per_Million_Inhabitants)
plt.title('Country Vs Road deaths per Million Inhabitants', fontsize=14)
plt.xlabel('Country', fontsize=10)
plt.ylabel('Road deaths per Million Inhabitants', fontsize=10)
plt.show()
