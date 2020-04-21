
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd        
import requests
import random
from itertools import count

# Request fails unless we provide a user-agent
api_response = requests.get('https://api.thevirustracker.com/free-api?countryTimeline=US', headers={"User-Agent": "Chrome"})
covid_stats = api_response.json()['timelineitems']
 
# Break out individual stats
date= []
deaths = []  
daily_deaths =[]
total_casesL = []
daily_cases = []
z = 0


for i in covid_stats:
    print (i)
    del i['stat']

for c_date, info in i.items():
    print("\nDate:", c_date)
    date.append(c_date)
    print ('Total Cases:',info['total_cases'])
    total_casesL.append(info['total_cases'])
    print ('New Cases:',info['new_daily_cases'])
    daily_cases.append(info['new_daily_cases'])
    daily_deaths.append(info['new_daily_deaths'])
    deaths.append(info['total_deaths'])

print(total_casesL) 
print(daily_cases)   
print(daily_deaths) 
print (date)
print (plt.style.available)

death_rate = deaths[-1]/total_casesL[-1]
c = str(death_rate)
print('Death rate: ' + c[1:6])

y = np.arange(len(date))
 
plt.plot(y,total_casesL, label = 'Cases', marker = '.', linewidth=3  )    
plt.plot(y,daily_cases , 'y', label = 'New Cases', linestyle = '--', )
plt.plot(y, daily_deaths, 'k', label = 'New Deaths' )
plt.plot(y, deaths, color = 'r', label = 'Deaths' ,  )  

plt.ylabel('People')
plt.xlabel('Days') 
plt.title('Covid 19 Cases (USA)')
plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()












