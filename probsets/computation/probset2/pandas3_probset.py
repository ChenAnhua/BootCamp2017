'''
Problem set for the pandas3 lab

'''
import numpy as np
from pydataset import data
import pandas as pd
from matplotlib import pyplot as plt


diamonds = data("diamonds")
diamonds['price_per_carat'] = pd.Series(diamonds['price']/diamonds['carat'], index = diamonds.index)
cut = diamonds.groupby("cut")
color = diamonds.groupby("color")

cut_means = cut.mean()
cut_errors = cut.std()

color_means = color.mean()
color_errors = color.std()


cut_means.loc[:,["price_per_carat",]].plot(kind="bar", yerr=cut_errors, title= "Average price per carat by different cut")
plt.legend(loc = 'upper left')
plt.ylabel("Average price per carat")


color_means.loc[:,["price_per_carat",]].plot(kind="bar", yerr=color_errors, title= "Average price per carat by color")
plt.legend(loc = 'upper left')
plt.ylabel("Average price per carat")


plt.show()
print("Grouped by the different cut categories, we could see that price per cut is, in general, positively correlated with the level of cut. However, the variation of price per carat also becomes larger when cut is rated higher.")

#readin and clean the data first
titanic = pd.read_csv("titanic.csv")
avg_age = titanic['Age'].mean()
titanic = titanic.dropna(axis = 0, how = "all")
titanic['Age'] = titanic['Age'].fillna(value = avg_age)

# 1. using groupby call
embark_town = titanic.groupby('Embarked')
embark_town_means = embark_town.mean()
print(embark_town_means['Survived'])

#2. creating pivot table
tpivot = titanic.pivot_table('Survived', index=['Sex'], columns=['Embarked'])
print("Pivot table of survival rate:\n",tpivot)
tpviot_count = titanic.pivot_table('Survived', index=['Sex'], columns=['Embarked'], aggfunc= 'count')
print("Pivot table of sampling count: \n",tpviot_count)

#3. delving deeper into the data
tpivot_1 = titanic.pivot_table('Survived', index=['Sex'], columns=['Embarked', 'Pclass'])
print("Pivot table of survival rate (sex, embark town and class\n",tpivot_1)
tpivot_1_count = titanic.pivot_table('Survived', index=['Sex'], columns=['Embarked', 'Pclass'], aggfunc= 'count')
print("Pivot table of sampling size (sex, embark town and class\n",tpivot_1_count)
# printing some conclusion
print("Just by using the groupby call, we find the average survival rate of passenger embarking from C is higher than those from Q and S. Also, it holds true when we break down into different gender.However, when we further divide different ambarking location into different class, we found something interesting. The distribution of classed is different among three embarking locations. Embarking point C has a very large relative proportion of class 1 passengers while boarding points Q and S have more class 3 passengers. We find the survival rate of the same class between different locations actually don't differ much. Therefore, what explains the difference in survival rate between different embarking points we observed before is simply because the distribution of class between these three ports are different and class 1 and 2 passengers tend to have a larger survival rate.")
