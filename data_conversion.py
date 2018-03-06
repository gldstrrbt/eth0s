import os
from glob import glob
from datetime import datetime
from pprint import pprint 
import json
from itertools import groupby
import collections 
from collections import Counter
from scipy import *
from pprint import pprint

filesDir = 'testData.json'
f = 0 
countListA = []
countListB = []
entries = {}
entries['pair'] = []

strBreak = str('\n')

with open(filesDir) as b:
	for r, c in enumerate(b):
		c = c.strip(strBreak).strip().strip('    {').strip('    }').strip('      }').strip('   }, ').strip('"comms",').strip('"  "').strip('""').strip('" "').strip().strip('"'+'"').strip('"'+' ').strip('":",').strip(': [",').strip('[').strip(']').strip('strangers')
		rr = ''
		ss = ''		
		c = c.replace(', ', '"   ')

		if 'strangerA' in c and r%1 == 0:
			rr = c
			countListA.append(c)
		else:
			ss = c
			countListA.append(c)
		countListB.append((str(rr) + '' + str(ss)))

uu = filter(len, countListB)
ww = Counter(uu)


vv = []
qq = []

for yy, zz in enumerate(uu):
	pear_b = str(uu[yy + 0]).strip('B' + '": ' + '"').strip('A' + '": ' + '"')
	
	if yy % 2 == 0:
		vv.append(pear_b)
	if yy % 2 == 1:
		qq.append(pear_b)

new_list = []

en_a = 0
en_b = len(vv)
while en_a < en_b:
	wu = qq[en_a] + ' ' + vv[en_a]
	new_list.append(wu)
	en_a += 1 

encounters = {}
encounters['occurences'] = []
encounters['unique_calls'] = []

fin = Counter(new_list)
for enum, dev in enumerate(fin):
	val_a = fin.values()
	val_b =	fin.keys()
	val_c =	val_a[enum]
	val_d =	val_b[enum]
	val_e =	dev

	print enum
	print val_c
	print val_d

	encounters['occurences'].append({
			'num' : enum,
			'freq' : val_c,
			'addresses' : val_d
		})

print encounters['occurences']
uniq_calls = len(encounters['occurences'])
print uniq_calls

encounters['unique_calls'].append(uniq_calls)

with open("_callers.json", "w+") as outfile:
	jDate = json.dump(encounters, outfile, indent=2)
