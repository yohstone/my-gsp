
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


#process dataset
try: 
	input_file = PcapReader('8commands-1comm5s-90s.pcap') # input file
	num = 0 # packet amount
	mydict = {}

	# f = open('./8commands-1comm5s-90s-alldata-str.txt', 'r')
	# dataset = []
	# for line in f.readlines():
	# 	dataset.append(line.strip())
	# 	#print(line)

	# print(dataset)
	# sys.exit()

	output_file = open('8commands-1comm5s-90s-alldata-str.txt', 'a') # output file

	while num <= 100:
		num = num + 1  # count packet amount 
		pprint.pprint(num)
		data = input_file.read_packet()
		if data is None:
			break
		else:
			p = repr(data)
			loaddata = data['Raw'].load

			timestamp = round(data.time, 1)
			slen = len(data['Raw'].load) # packet load data length
			#pprint.pprint(loaddata)
			#pprint.pprint(slen)
			if slen != 20:
				continue

			# save sequences to the file
			all_byte_str = binascii.b2a_hex(loaddata) # convert binary sequence to byte string
			all_text_str = all_byte_str.decode()	  # convert byte string to text string
			pprint.pprint(all_text_str)
			output_file.write(all_text_str + '\n')

	input_file.close()
	output_file.close()

except Exception as e:
	print('error')
	pprint.pprint(e)

















