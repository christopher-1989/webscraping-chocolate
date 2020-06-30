import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
website = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html'
)
soup = BeautifulSoup(website.content, 'html.parser')
soup_data = soup.find_all(attrs={"class": 'Rating'})
ratings = []
for idx in range(1, len(soup_data)):
  ratings.append(float(soup_data[idx].get_text()))
plt.hist(ratings)
plt.show()
soup_names = soup.select('.Company')
#print(soup_names)
names = []
for idx in range(1, len(soup_names)):
  names.append(soup_names[idx].get_text())
#print(names)
df = pd.DataFrame.from_dict({'company-name':names, 'rating':ratings})
print(df.head())
mean_ratings = df.groupby('company-name').rating.mean()
print(mean_ratings)

ten_best = mean_ratings.nlargest(10)
print(ten_best)
soup_percent = soup.select('.CocoaPercent')
#print(soup_names)
percentage = []
for td in soup_percent[1:]:
  try: 
    percent = int(td.get_text().strip('%'))
  except:
    percent = int(td.get_text().strip('%')[:2])
  percentage.append(percent)
#print(percentage)
df['CocoaPercentage'] = percentage
print(df.head())
plt.clf()
plt.scatter(df.CocoaPercentage, df.rating)
z = np.polyfit(df.CocoaPercentage, df.rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()