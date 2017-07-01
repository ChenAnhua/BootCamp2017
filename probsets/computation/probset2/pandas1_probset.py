'''
This is the homework file for Pandas 1
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# problem 1
val = -3
n   = 5
s11 = pd.Series(val, index = 1 + np.arange(n))
print(s11)

dic = {'Bill': 31, 'Sarah': 28, 'Jane': 34, 'Joe': 26}
s12 = pd.Series(dic)
print("/n",s12)

# problem 2
#define the random walk function first
def rw(Nval, pval):
    s = np.zeros(Nval)
    s[1:] = np.random.binomial(1, pval, size = (Nval-1, ))*2 - 1
    s = pd.Series(s)
    s = s.cumsum()
    return(s)

#create the five-line charts
d = {'trial1':rw(100,.5), 'trial2': rw(100,.5), 'trial3':rw(100,.5),'trial4':rw(100,.5),'trial5':rw(100,.5)}
df = pd.DataFrame(d)
fig = df.plot()
plt.ylim([-50, 50])
plt.xlim([0, 100])
plt.show()

#create the biased random walk charts
df1 = rw(100, 0.51)
df2 = rw(1000, 0.51)
df3 = rw(10000, 0.51)

df1.plot()
plt.xlim([0, 100])
plt.show()

df2.plot()
plt.xlim([0, 1000])
plt.show()

df3.plot()
plt.xlim([0, 10000])
plt.show()

# problem 3 & 4
name = ['Mylan', 'Regan', 'Justin', 'Jess', 'Jason', 'Remi', 'Matt', 'Alexander', 'JeanMarie']
sex = ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F']
age = [20, 21, 18, 22, 19, 20, 20, 19, 20]
rank = ['Sp', 'Se', 'Fr', 'Se', 'Sp', 'J', 'J', 'J', 'Se']
ID = range(9)
aid = ['y', 'n', 'n', 'y', 'n', 'n', 'n', 'y', 'n']
GPA = [3.8, 3.5, 3.0, 3.9, 2.8, 2.9, 3.8, 3.4, 3.7]
mathID = [0, 1, 5, 6, 3]
mathGd = [4.0, 3.0, 3.5, 3.0, 4.0]
major = ['y', 'n', 'y', 'n', 'n']

studentInfo = pd.DataFrame({'ID': ID, 'Name': name, 'Sex': sex, 'Age': age, 'Class': rank})
otherInfo = pd.DataFrame({'ID': ID, 'GPA': GPA, 'Financial_Aid': aid})
otherInfo = pd.DataFrame({'ID': ID, 'GPA': GPA, 'Financial_Aid': aid})


prob3result = studentInfo[(studentInfo['Age'] > 19) & (studentInfo['Sex'] == 'M')][['ID', 'Name']]
print("Problem3 result: \n":, prob3result)

prob4result = pd.merge(studentInfo[studentInfo[('Sex')]== 'M'], otherInfo, on = 'ID', how = 'inner')[['ID', 'Age', 'GPA']]
print("Problem4 result: \n" , prob4result)

# problem 5
crime_data = pd.read_csv("crime_data.txt",header = 1, index_col = 0)
crime_data['Crime-Rate'] = pd.Series((crime_data['Total']/crime_data['Population']), index = crime_data.index)

# plotting the crime rate
cr_fig = plt.figure()
plt.plot(crime_data.index, crime_data['Crime-Rate'])
plt.xlabel('Year')
plt.ylabel('Crime Rate')

plt.show()

max5 = np.array(crime_data.sort_values(['Crime-Rate'], ascending=0).index[range(5)])
print("Five years with maximum crime rate: \n",max5)

avg1 = crime_data[(crime_data.index>= 1960) & (crime_data.index <= 2012)]['Total'].mean()
print("Average total crimes between 1960 and 2012: " ,avg1)
avg2 = crime_data[(crime_data.index>= 1960) & (crime_data.index <= 2012)]['Burglary'].mean()
print("Average burglary crimes between 1960 and 2012: " ,avg2)

desiredindex = np.array(crime_data[(crime_data['Total'] < avg1) & (crime_data['Burglary'] > avg2)].index)
print("Years where total crime is below average while burglary is above average: " ,desiredindex)

pm_fig = plt.figure()
plt.plot(crime_data['Population'], crime_data['Murder'])
plt.xlabel('Population')
plt.ylabel('Number of murders')

plt.show()

crime_subdata = crime_data[(crime_data.index >= 1980) & (crime_data.index<= 1989)][['Population', 'Violent', 'Robbery']]
crime_subdata.to_csv("crime_subset.txt")





#end
