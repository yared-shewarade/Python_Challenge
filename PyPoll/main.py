
# coding: utf-8

# In[88]:


#importing the neccesary dependencies
import os
import csv
from collections import OrderedDict
from operator import itemgetter


# In[15]:


# determine the path for csv data


# In[9]:


csvpath=os.path.join(os.getcwd(), "Resources", "election_data.csv")


# In[77]:


#defining variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = []
Candidate_Dictionary = {}


# In[44]:


with open (csvpath) as election_data:
    election = csv.DictReader(election_data)
    
    for row in election:
        votes= votes + 1
        total_candidates = row["Candidate"]
        
        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])
            
            candidate_votes[row["Candidate"]] = 1
        
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1


# In[20]:


# Determining the winners for this election

#if (votes > winner_votes[2]):
    #greatest_increase[1] = revenue_change
    #greatest_increase[0] = row["Candidate"]


# In[47]:


print()
print()
print()
print("ELection Results")
print("__________________")
print("Total Votes" " " +  str(votes))
print("__________________")


# In[74]:


# Results


# In[87]:


for candidate in candidate_votes:
    print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100),3))+"%" + "(" + str(candidate_votes[candidate]) + ")")
    candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100),3))+"%" + "(" + str(candidate_votes[candidate]) + ")")


# In[89]:


winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)


# In[90]:


print("______________________")
print("Winner:" + str(winner[0]))
print("______________________")

