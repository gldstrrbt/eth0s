import os 
from os import listdir
import os.path
import time
import sys
print(sys.path)
import json
from collections import Counter


path_a = '/Users/slessa/Desktop/SL/___P/_tests/_stranger_friends/__py/_current/_callers.json'

# exCon = 
total_a = 0
total_iter_a = 0

freq_curr = 0
num_curr = 0
add_curr = str()

level_a = []
level_b = []
level_c = []
uniq = ''

with open(path_a) as a:
	aa = json.load(a)
	total_a = aa['unique_calls'][0]

	for c, b in enumerate(aa):
			level_a.append(b)

	base_ms = aa[level_a[0]][30]

	


	for e, d in enumerate(base_ms):
		level_b.append(d)
		level_c.append(base_ms[level_b[e]])
		print base_ms[level_b[e]]

	while total_iter_a < total_a:
		uniq = aa[level_a[0]][total_iter_a] 
		m_weight = total_iter_a*0.1
		m_age = total_iter_a*1.05
		G.app.selectedHuman.age=m_age
		G.app.selectedHuman.weight=m_weight
		MHScript.getModelingParameters()
		MHScript.updateModelingParameter('macrodetails/Age', m_age)
		MHScript.updateModelingParameter('macrodetails-height/Height', 0.5)
		MHScript.updateModelingParameter('macrodetails-universal/Weight', (m_age))
		G.app.selectedHuman.hasWarpTargets=True
		MHScript.saveObj("modelNum_" + str(total_iter_a))
		MHScript.saveModel("modelNum_" + str(total_iter_a))
		total_iter_a += 1





MHScript.updateModelingParameter('macrodetails/Age', m_age)
MHScript.updateModelingParameter('macrodetails/Weight', m_age)














	# for e, d in enumerate(uniq):
	# 	level_b.append(d)
	# 	print level_b[e]
	# 	level_c.append(uniq[level_b[e]])
	# 	print uniq[level_b[e]]

	# print level_c
	# print uniq
	# print uniq
	# print uniq
	# print uniq
	# print uniq
	# print uniq
	# print uniq
	# print uniq
	# print uniq

	
		
			# bb = aa[b]

			# for d in bb:
			# 	for dd in d:
			# 		print dd


# 	print total_iter_a 
# # 	MHScript.saveModel("modelNum_" + str(total_iter_a))
# 	MHScript.saveObj("modelNum_" + str(total_iter_a))
# 	total_iter_a += 1






# Exportation
# To do:
	# Number of docs to process and produce based on number of mac addresses
		# Check if file already exists



# path_a = "/Users/slessa/Desktop/SL/___P/_tests/_stranger_friends/__py/_current/_json/"
# dir_files_a = listdir(path_a)
# dir_len_a = len(dir_files_a)
# total_iter_a = 0

# print path_a
# print dir_files_a
# print dir_len_a

# while total_iter_a < dir_len_a:
# 	print total_iter_a 
# 	total_iter_a += 1
# 	MHScript.saveModel("modelNum_" + str(total_iter_a) + "", "/Users/slessa/Documents/MakeHuman/v1/models/")
























# updateModelingParameter(parameterName, value)
#
# Sets the modeling parameter with specified name of the model to the specified value.
# The value is a float between 0 and 1, where 0 means nothing at all or minimal, and 1 is the maximum value.

# MHScript.updateModelingParameter('macrodetails/Age', 0.7)

