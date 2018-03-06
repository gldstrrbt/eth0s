import os
from glob import glob
import json
from pprint import pprint
from datetime import datetime

dirContents = os.listdir('_json/')
print dirContents
theD = datetime.now().strftime('%Y-%m-%d---%H_%M_%S')
print theD

filew = open('_data-gen/' + theD + '.json', 'w+')
filew.truncate()
da = []
ta = []
ga = []
cols = []
store_a = []
store_b = []
dir_contents = glob('_json/*.json')
print dir_contents

filew.write('{0}\n'.format(dirContents))

for v in dir_contents:
	fPath = v
	with open(fPath) as data_file:  
		data = json.load(data_file)
		
		# DEBUG
		# print data
		# DEBUG
		
		for c, d in enumerate(data):
			
			cd = d['_source']
			for e in cd:
				de = cd[e]
				if 'wlan.ta' in de:
					wda = de['wlan.ta']
					wta = de['wlan.da']
					filew.write('{0} {1}\n'.format(wda[0], wta[0]))
					da.append(wda[0])
					ta.append(wta[0])
for g in da:
	ga.append(g[0])
	filew.write('{0}\n'.format(g))

for i in ga:
	gadd = i.replace(':', ' ')
	cols.append(gadd)
# print len(cols)
for l in cols:
	holdM = []
	for n, m in enumerate(l):
		if m != ' ' and (n)%3 == 0:
			intMa = int((l[n]) ,16)
			intMb = int((l[n+1]) ,16)
			intM = intMa + intMb
		 	holdM.append(intM)
		if n == 15:
			store_a.append(holdM)
	holdM = []

for o in store_a:
	holdP = []
	for q, p in enumerate(o):
		if (q+1)%2 == 0:
			intPa = o[q-1]
			intPb = o[q]
			intP = intPa + intPb 
			holdP.append(intP)
		if q == 5:
			store_b.append(holdP)
	holdP = []
# print store_b

filew.close()