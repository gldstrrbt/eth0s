import os
from glob import glob
from datetime import datetime
from pprint import pprint 
import json
from itertools import groupby
from collections import Counter

# dataFile = json.dumps(dataFile)
dataFile = open("testData.json", "r+")
countListA = []
countListB = []
countListC = []

with open("testData.json") as z:
	w = json.load(z)
	v = w["strangers"]
	countListA.append(w)
	countListB.append(v)
	for y in v:
		countListC.append(y)


initA = countListA[0]
initAa = initA

initB = initAa["strangers"]
initBb = initB[0]

initC = initBb["comms"]

print len(initB)

cLfile = Counter({countListC})

for s in cLfile:
	print s
# print(cLfile[0])
# print countListA.count()
# for t in countListC:
	# print t
	# print countListC.count(t)

# doo = json.loads(cLfile)

# with open("testOccurrences.json", "w+") as outfile:
# 	jDate = json.dump(cLfile, outfile, indent=2)




