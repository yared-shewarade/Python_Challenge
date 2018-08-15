
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


csvpath = os.path.join(os.getcwd(), "Resources", "budget_data.csv")


# In[5]:


with open(csvpath, newline='') as csvdata:
    budget = csv.reader(csvdata, delimiter=',')
    next(budget, None)
    csvdata = list(budget)
    dates = []
    revenues = []
    
    for row in csvdata:
        dates.append(row[0])
        revenues.append(int(row[1]))


# In[6]:


revchange = []


# In[8]:


revchange = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]


# In[40]:


from statistics import mean
max_change = max(revchange)
big_loss = min(revchange)
avg_change = mean(revchange)
total_month = len(dates)
total_revenue = sum(revenues)
max_month = None
loss_month = None


# In[44]:


initial_val = None
for row in csvdata:
    if initial_val is None:
        initial_val = int(row[1])
        continue
    if int(row[1]) - initial_val == big_loss:
        loss_month = row[0]
    initial_val = int(row[1])

initial_val2 = None
for row in csvdata:
    if initial_val2 is None:
        initial_val2 = int(row[1])
        continue
    if abs(int(row[1]) - initial_val2) == max_change:
        max_month = row[0]
    initial_val2 = int(row[1])


# In[45]:


print("Financial Analysis")
print("-------------------------------------------------------")
print("Total Months:" + " " + str(total_month))
print("Total Months" + " " + "$" + str(total_revenue))
print("Average Change:" " " + "$" + str(avg_change))
print("Greatest Increase in Profits:" + " " + "$"  + str(max_month) + " " + "$" + str(max_change))
print("Greatest Decrease in Profits:" + " " + "$" + str(loss_month) + " " + "$" + str(big_loss))

