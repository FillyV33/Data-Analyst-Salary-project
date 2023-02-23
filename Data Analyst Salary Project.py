import pandas as pd
import matplotlib.pyplot as plt

jobs = pd.read_csv("C:/ExampleUser/Name/Documents/Directory/DataDirectory/gsearch_jobs.csv")

#scrubbing through the data, I can easily tell "data analyst" is the most searched term
#but I want to be able to show that on the code and make a graph of it somehow.

##create a graph to show the most searched term

jobs.head()
count= jobs['search_term'].count()
count2= (jobs['search_term']=='data analyst').sum()
print(count)
print(count2)
# So using two strings of code, the first one I made a general count to see the overall number 
#the second string is to count just data analyst, since scrubbing through it seemed to be the only one that popped up
#It's the same number, so data analyst is the most searched term. 
x= ['data analyst', 'data scientist', 'data engineer']
y = [8026, 0, 0]

plt.bar(x, y)
#The code above is my graph to show the most searched terms, I threw two other terms even though they aren't in the data to showcase that 
# data analyst really is the only thing there. 

##are there more work from home jobs?

#This string of code removes NA's while keeping the TRUE value in the data
num_work_from_home = (jobs['work_from_home'].dropna() == True).sum()
print(num_work_from_home)
#there are 3924 jobs that are work from home in this data set. Basic math tells us there are less remote work jobs according to the data.

##What is the average salary for data analysts?

AvgSalary= jobs["salary_avg"]


#this portion of code is to remove the hourly rate in salary rate column, i chose 300 because i would say it's safe to assume data analysts don't usually get paid 300 an hour
#we are trying to find the average pay for remote work for a data analyst in this data set.  
AvgSalary2= AvgSalary[jobs["salary_avg"] >= 300]
print(AvgSalary2)

#this is the code for the average 

AvgSalary3 = sum(AvgSalary2)/len(AvgSalary2)
print(AvgSalary3)
#there is the number 103,163.79, this is the average people get paid to work from home according to this data.





