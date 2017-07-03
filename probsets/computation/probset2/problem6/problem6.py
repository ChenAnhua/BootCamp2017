'''
This script is for plotting the weather temperature chart
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

#readin the data
location_list = ['Indi', 'Pitt', 'Miam', 'Wash', 'Chic']

data = {}

for location in location_list:
    df = pd.read_csv("{}.csv".format(location))
    vars()[location] = df
#data manipulation

for location in location_list:
    globals()[location].index = pd.to_datetime(globals()[location]['DATE'], format = "%Y%m%d")
    globals()[location]['YEARindicator']= globals()[location].index.year % 4
    globals()[location]['DofY'] = globals()[location].index.dayofyear
    globals()[location].loc[globals()[location]['YEARindicator'] == 0,'DofY'] -= 265
    globals()[location].loc[(globals()[location]['YEARindicator'] == 0) & (globals()[location]['DofY'] < 0),'DofY'] +=366
    globals()[location].loc[globals()[location]['YEARindicator'] != 0,'DofY'] -= 264
    globals()[location].loc[(globals()[location]['YEARindicator'] != 0) & (globals()[location]['DofY'] < 0),'DofY'] +=365

#plotting
lifetimeweather_fig = plt.figure(figsize=(10, 5))
for location in location_list:
    if location == "Chic":
        style = dict(fillstyle = 'full', color = 'maroon', markersize = 0.3)
        plt.plot(globals()[location]['DofY'], globals()[location]['TMAX'], "o", **style)
        plt.plot(globals()[location]['DofY'], globals()[location]['TMIN'], "o", **style)
    style = dict(fillstyle = 'full', color = 'black', markersize = 0.1, alpha = 0.9)
    plt.plot(globals()[location]['DofY'], globals()[location]['TMAX'], "o", **style)
    plt.plot(globals()[location]['DofY'], globals()[location]['TMIN'], "o", **style)
style1 = dict(ms = 5, markerfacecolor="yellow", markeredgecolor='black', markeredgewidth=1)
born_x, born_y_max, born_y_min = Indi[Indi['DATE'] == 19750122]['DofY'], Indi[Indi['DATE'] == 19750122]['TMAX'], Indi[Indi['DATE'] == 19750122]['TMIN']
champ_x, champ_y_max, champ_y_min = Pitt[Pitt['DATE'] == 19880714]['DofY'],Pitt[Pitt['DATE'] == 19880714]['TMAX'], Pitt[Pitt['DATE'] == 19880714]['TMIN']
plt.plot(born_x, born_y_max, "o", **style1 )
plt.plot(born_x, born_y_min, "o", **style1 )
plt.plot(champ_x, champ_y_max, "o", **style1 )
plt.plot(champ_x, champ_y_min, "o", **style1 )
arrowstyle = dict(facecolor='black', shrink=0.05, width  = 1, headwidth = 5)
plt.annotate('Born (max temperature)', xy = (born_x, born_y_max), xytext = (25, 0), arrowprops= arrowstyle)
plt.annotate('Born (min temperature)', xy = (born_x, born_y_min), xytext = (200, -10), arrowprops= arrowstyle)
plt.annotate('little league all-star team wins \nregional championship (max temperature)', xy = (champ_x, champ_y_max), xytext = (50, 100), arrowprops = arrowstyle)
plt.annotate('little league all-star team wins \nregional championship (min temperature)', xy = (champ_x, champ_y_min), xytext = (200, 20), arrowprops = arrowstyle)

plt.xlabel("...Autumn...                     ...Winter...                     ...Spring...                     ...Summer...   \n Day of the year (starting from September 21)")
plt.ylabel("Temperature in Fahrenheit")
plt.show()
