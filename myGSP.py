
 #-*- coding:utf-8 -*-
import scapy
from scapy.all import *
import math
import pylab as pl
import pprint
import sys
import binascii
import csv
import pandas as pd


#get dataset
try: 

	f = open('./8commands-1comm5s-90s-alldata-str.txt', 'r')
	dataset = []
	for line in f.readlines():# read file and get data
		dataset.append(line.strip())
		#print(line)

	min_sup = 0.2
	min_sup_num = min_sup * len(dataset)

	# cal L_1
	L_1 = []
	support = {} # each pattern's support
	count = 0
	for s in dataset:
		i = 0
		pos = 0
		while i < len(s):
			byte = [s[i] + s[i + 1], pos] # save each byte, it's position and support [byte, position]
			i += 2
			pos += 1
			if L_1.count(byte) == 0:      # keep item in L_1 is unique
				L_1.append(byte)
				support[tuple(byte)] = 1
				count += 1
			else:
				support[tuple(byte)] += 1

	#print(L_1)
	#print(len(L_1))
	pprint.pprint(support)

	# cal L_k

	
	

except Exception as e:
	print('error')
	pprint.pprint(e)

















