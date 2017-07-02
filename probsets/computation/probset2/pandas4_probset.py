import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
# problem 1
# readin the data
djia = pd.read_csv("DJIA.csv")
# cleaning the missing values
#djia = djia.fillna(np.nan)
values = {"VALUE": djia['VALUE'].values}
djia = pd.DataFrame(values, index = djia['DATE'])
djia[djia.VALUE == "."]= np.nan
djia.index = pd.to_datetime(djia.index)
djia.VALUE = pd.to_numeric(djia.VALUE)

#problem 2
# readin the data
paychecks = pd.read_csv("paychecks.csv", header = None)
date1 = pd.date_range(start = '2008-03-13', periods = (len(paychecks)+1)/2,freq = "WOM-1FRI")
date2 = pd.date_range(start = '2008-03-13', periods = (len(paychecks)-1)/2,freq = "WOM-3FRI")
date = date1.union(date2)
values = {"paychecks": paychecks[0].values}
paychecks = pd.DataFrame(values, index = date)
paychecks.index = pd.to_datetime(paychecks.index)

#problem4
# readin the data
finances = pd.read_csv("finances.csv")
p = pd.period_range("1978-09-01", periods = len(finances), freq="Q-DEC")
p += 1
values = {"Ear"}
finances.index = p

#problem 5
web_traffic = pd.read_csv("website_traffic.csv")
start = pd.to_datetime(web_traffic['ENTER'])
end = pd.to_datetime(web_traffic['LEAVE'])
duration = (end -start).mean()
print(duration)

#firstly create a column with 1s
web_traffic['Total number of visit'] = np.ones_like(range(len(web_traffic)))
web_traffic.index = start
visit = web_traffic['Total number of visit'].resample("H").sum()
visit.index = visit.index.to_period()
visit.index.names = ['Range']
print(visit)

#proble6
#daily change
dailychange = djia - djia.shift(1)
maxvalue = dailychange.VALUE.max()
maxdate = dailychange.VALUE.idxmax()
print("Date with largest gain: ", maxdate)
print("Largest gain: ", maxvalue)
minvalue = dailychange.VALUE.min()
mindate = dailychange.VALUE.idxmin()
print("Date with largest loss: ", mindate)
print("Largest loss: ", minvalue)
# monthly change
monthlychange = dailychange.resample("M").sum()
maxvalue_m = monthlychange.VALUE.max()
maxdate_m = monthlychange.VALUE.idxmax()
print("Month with largest gain: ", maxdate_m)
print("Largest monthly gain: ", maxvalue_m)
minvalue_m = monthlychange.VALUE.min()
mindate_m = monthlychange.VALUE.idxmin()
print("Month with largest loss: ", mindate_m)
print("Largest monthly loss: ", minvalue_m)

#probelm 7
rolling_30 = djia.rolling(30).mean()
rolling_365= djia.rolling(365).mean()
ewma_30 = djia['VALUE'].ewm(span = 30).mean()
ewma_365 = djia['VALUE'].ewm(span = 365).mean()
djia['rolling_30'] = rolling_30.VALUE.values
djia['rolling_365'] = rolling_365.VALUE.values
djia['exponential weighted ma (30)'] = ewma_30.values
djia['exponential weighted ma (365)'] = ewma_365.values
djia.plot(title = 'Dow Jones Industrial Average')
plt.show()
