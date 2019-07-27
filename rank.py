import camelot
import pandas as pd
import operator

gp = {
    'O': 10,
    'A+': 9,
    'A': 8.5,
    'B+': 8,
    'B': 7,
    'C': 6,
    'P': 5,
    'F': 0,
    'FE': 0,
    'd': 0,
    'E': 0,
    'I': 0
}

#Credits for this semester entered in order of slots
credits = [4,4,4,3,3,3,1,1,1]
tc = sum(credits)
# CREATING REGNO:NAME DICTIONARY
rolltables = camelot.read_pdf('roll.pdf', pages='2')

names = {}

table = rolltables[0].df


regnum = table[1].tolist() + table[4].tolist()
name = table[2].tolist() + table[5].tolist()


for i in range(len(regnum)):
    names[str(regnum[i])] = str(name[i])

# Remove and adding some names because the Class Roll List was not read properly
names['TVE18CS017'] = 'DHANESH P S'
names['TVE18CS018'] = 'DHRUV ELDHO PETER'
names['TVE18CS021'] = 'GOKUL K'
names['TVE18CS022'] = 'HIRA FATHIMA C P M'
names['TVE18CS023'] = 'HRISHIKESH T S'
names['TVE18CS032'] = 'MARIA PAUL T'
names['TVE18CS033'] = 'MEGHA NANDA J'

del(names['TVE18CS017 DHANESH P S'])
del(names['TVE18CS018 DHRUV ELDHO PETER'])
del(names['TVE18CS021 GOKUL K'])
del(names['TVE18CS022 HIRA FATHIMA C P M'])
del(names['TVE18CS023 HRISHIKESH T S'])
del(names['TVE18CS032 MARIA PAUL T'])
del(names['TVE18CS033 MEGHA NANDA J'])
del(names['Register No'])
#########################################

#The result was split across 5 pages
tables = camelot.read_pdf('result_TVE.pdf', pages='38,39,40,41,42')

regno = {}

#Looping through all the tables
for i in tables[1:]:
    df = i.df
    reg = df[0].tolist()
    score = df[1].tolist()
    for i in range(len(reg)):
        
        if str(reg[i])[0:5] != 'TVE18':
            continue
        arr = str(score[i]).split(',')
        gpa = 0
        for j in range(len(arr)):
            if(arr[j][-2] != '+'):
                arr[j] = gp[arr[j][-2]]
            else:
                arr[j] = gp[arr[j][-3:-1]]
        for k in range(len(arr)):
            gpa += arr[k]*credits[k]
        gpa /= float(tc)
        regno[str(reg[i])] = gpa

#Student left the College :)
del(regno['TVE18CS034'])

prev_rank = 1
rank = 1
people_passed = 0

sorted_ranklist = sorted(regno.items(), key=operator.itemgetter(1))[::-1]
for i in range(len(sorted_ranklist)):
    people_passed += 1
    if i != 0:
        if(sorted_ranklist[i-1][1] != sorted_ranklist[i][1]):
            rank=people_passed
        print str(rank) + ":" + names[sorted_ranklist[i][0]] + ":" + str(sorted_ranklist[i][1])
    else:
        print str(rank) + ":" + names[sorted_ranklist[i][0]] + ":" + str(sorted_ranklist[i][1])
