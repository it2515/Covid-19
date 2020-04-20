

import matplotlib.pyplot as plt
import pandas as pd        
import requests
import random
from itertools import count
# useful data


# Get data on only confirmed cases
#api_response = requests.get('https://covid19api.herokuapp.com/confirmed')
 
# Print latest data for location ID 100: California, USA
#print(api_response.json()['latest'])


#import requests

# Request fails unless we provide a user-agent
api_response = requests.get('https://api.thevirustracker.com/free-api?countryTimeline=US', headers={"User-Agent": "Chrome"})
covid_stats = api_response.json()['timelineitems']
 
# Break out individual stats
date= []
for i in covid_stats:
    print (i)
    del i['stat']
   
daily_deaths =[]
total_casesL = []
daily_cases = []
y = []
z = 0
for c_date, info in i.items():
    print("\nDate:", c_date)
    date.append(c_date)
    print ('Total Cases:',info['total_cases'])
    total_casesL.append(info['total_cases'])
    print ('New Cases:',info['new_daily_cases'])
    daily_cases.append(info['new_daily_cases'])
    daily_deaths.append(info['new_daily_deaths'])

print(total_casesL) 
print(daily_cases)   
print(daily_deaths) 
print (date)

x = len(date)

for l in date :
    l = z 
    z = l+1
    y.append(z)
plt.plot(y,total_casesL)    
plt.plot(y,daily_cases)
plt.plot(y, daily_deaths)
plt.ylabel('People')
plt.xlabel('Days') 
plt.title('Daliy Covid 19 Cases')


plt.legend(['New Cases', ' New Deaths'])
plt.show()












