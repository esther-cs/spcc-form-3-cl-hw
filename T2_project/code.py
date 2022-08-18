import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

class Workforce:
    def __init__(self,district,area,employee,employer,home_maker,retired,low_income,high_income):
        self.district=district
        self.area=area
        self.employee=employee
        self.employer=employer
        self.home_maker=home_maker
        self.retired=retired
        self.low_income=low_income
        self.high_income=high_income
    def Workforce_area(self):
        return self.employee+self.employer+self.home_maker+self.retired
    def __str__(self):
        return f"district: {self.district}\narea: {self.area}\nemployee: {self.employee}\nemployer: {self.employer}\nhomemaker: {self.home_maker}\nlowincome: {self.low_income}\n highincome:{self.high_income}"
def readWorkforceData( fname ):
    lst = []
    f = open( fname , "r")
    for j in f.read().split('\n'):
        if len(j) > 0:
            items = j.split(',')
            items[2:] = [ int(i) for i in items[2:] ]
            lst.append( Workforce( *items ) )
    f.close()
    return lst
alldata = readWorkforceData("workforce.txt")
def sortEmployer():
    for i in range(len(alldata)):
        min_idx=i
        for j in range(i+1, len(alldata)):
            if alldata[j].employer<alldata[min_idx].employer:
                min_idx=j 
        alldata[i],alldata[min_idx]=alldata[min_idx],alldata[i]
    print("first ten areas with the smallest # of employers:")
    for n in range(1,11):
        print(str(n)+". "+str(alldata[n-1].area))
    print("first ten areas with the largest # of employers:")
    alldata.reverse()
    for n in range(1,11):
        print(str(n)+". "+str(alldata[n-1].area))
sortEmployer()
def sumRetired():
    total_number_x=0
    total_number_y=0
    for i in range(len(alldata)):
        if alldata[i].district=="Southern":
            total_number_x+=alldata[i].retired
        elif alldata[i].district=="Sham Shui Po":
            total_number_y+=alldata[i].retired
    print("the total number of retired people in District X is "+str(total_number_x))
    print("the total number of retired people in District Y is "+str(total_number_y))
sumRetired()
counter_x=0
for i in range(len(alldata)):
    if alldata[i].district=="Southern":
        if (((alldata[i].high_income)/Workforce.Workforce_area(alldata[i]))*100)>15:
            counter_x+=1

print("# of areas in District X with more than 15% of people having monthly income > $40000 : "+str(counter_x))
counter_y=0
for i in range(len(alldata)):
    if alldata[i].district=="Sham Shui Po":
        if (((alldata[i].low_income)/Workforce.Workforce_area(alldata[i]))*100)>1:
            counter_y+=1
print("names of areas with more than 1% of people having monthly income < $2000 : "+str(counter_y))

employer_lst=[]
high_income_lst=[]
for i in range(len(alldata)):
    if alldata[i].district=="Southern" or alldata[i].district=="Sham Shui Po":
        employer_lst.append(alldata[i].employer)
        high_income_lst.append(alldata[i].high_income)

employer_lst=np.array(employer_lst)
high_income_lst=np.array(high_income_lst)
plt.scatter(employer_lst, high_income_lst)
plt.show()

model = Sequential([Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit((employer_lst-employer_lst.min())/(employer_lst.max()-employer_lst.min()),(high_income_lst-high_income_lst.min())/(high_income_lst.max()-high_income_lst.min()),epochs=1000)

[[w]], [b] = model.layers[0].get_weights()
print( f"Learned parameters: w = {w}, b = {b}")

plt.plot(employer_lst, high_income_lst, 'ro', label = 'original')
high_income_lst_predict = model.predict(employer_lst/(employer_lst.max()-employer_lst.min()))*(high_income_lst.max()-high_income_lst.min())
plt.plot(employer_lst, high_income_lst_predict , label = 'predict')
plt.legend()
plt.show()
