{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "#importing the neccesary dependencies\n",
    "import os\n",
    "import csv\n",
    "from collections import OrderedDict\n",
    "from operator import itemgetter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# determine the path for csv data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "csvpath=os.path.join(os.getcwd(), \"Resources\", \"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "#defining variables\n",
    "votes = 0\n",
    "winner_votes = 0\n",
    "total_candidates = 0\n",
    "greatest_votes = [\"\", 0]\n",
    "candidate_options = []\n",
    "candidate_votes = []\n",
    "Candidate_Dictionary = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open (csvpath) as election_data:\n",
    "    election = csv.DictReader(election_data)\n",
    "    \n",
    "    for row in election:\n",
    "        votes= votes + 1\n",
    "        total_candidates = row[\"Candidate\"]\n",
    "        \n",
    "        if row[\"Candidate\"] not in candidate_options:\n",
    "            \n",
    "            candidate_options.append(row[\"Candidate\"])\n",
    "            \n",
    "            candidate_votes[row[\"Candidate\"]] = 1\n",
    "        \n",
    "        else:\n",
    "            candidate_votes[row[\"Candidate\"]] = candidate_votes[row[\"Candidate\"]] + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Determining the winners for this election\n",
    "\n",
    "#if (votes > winner_votes[2]):\n",
    "    #greatest_increase[1] = revenue_change\n",
    "    #greatest_increase[0] = row[\"Candidate\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\n",
      "ELection Results\n",
      "__________________\n",
      "Total Votes 3521001\n",
      "__________________\n"
     ]
    }
   ],
   "source": [
    "print()\n",
    "print()\n",
    "print()\n",
    "print(\"ELection Results\")\n",
    "print(\"__________________\")\n",
    "print(\"Total Votes\" \" \" +  str(votes))\n",
    "print(\"__________________\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "for candidate in candidate_votes:\n",
    "    print(candidate + \" \" + str(round(((candidate_votes[candidate]/votes)*100),3))+\"%\" + \"(\" + str(candidate_votes[candidate]) + \")\")\n",
    "    candidate_results = (candidate + \" \" + str(round(((candidate_votes[candidate]/votes)*100),3))+\"%\" + \"(\" + str(candidate_votes[candidate]) + \")\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'items'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-89-cd85f98c12bf>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mwinner\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msorted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcandidate_votes\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mitemgetter\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreverse\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'list' object has no attribute 'items'"
     ]
    }
   ],
   "source": [
    "winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "______________________\n",
      "Winner:('Correy', 704200)\n",
      "______________________\n"
     ]
    }
   ],
   "source": [
    "print(\"______________________\")\n",
    "print(\"Winner:\" + str(winner[0]))\n",
    "print(\"______________________\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
