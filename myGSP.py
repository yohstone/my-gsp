
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

def calSupport(dataset, L_k):
	support = {}
	for seq in dataset:
		# print(seq)
		for item in L_k:
			# print(item)
			if item[0] in seq : # seq has contain the item[0] -- the pattern
				if support.has_key(tuple(item)) :					
					support[tuple(item)] += 1
				else :
					support[tuple(item)] = 1

	return support

def createLk(S_k):
	i = 0
	S_k_len = len(S_k)
	L_k = []
	while i < S_k_len - 1:
		j = i + 1
		while j < S_k_len:
			new_pattern = []
			if S_k[i][1] - S_k[j][1] == (len(S_k[i][0]) / 2): # S_k[i] is in the right of S_k[j]
				new_pattern = [ S_k[j][0] + S_k[i][0], S_k[j][1] ]
			elif  S_k[i][1] - S_k[j][1] == - (len(S_k[i][0]) / 2): # S_k[i] is in the left of S_k[j]
				new_pattern = [ S_k[i][0] + S_k[j][0], S_k[i][1] ]
			if L_k.count(new_pattern) == 0 and new_pattern:
				L_k.append(new_pattern)
			j += 1
			
		i += 1
	return L_k


#get dataset
try: 

	f = open('./8commands-1comm5s-90s-alldata-str.txt', 'r')
	dataset = []
	for line in f.readlines():# read file and get data
		dataset.append(line.strip())
		#print(line)

	min_sup = 0.2
	min_sup_num = min_sup * len(dataset)
	seq_len = len(dataset[0])

	# --- 1. cal L_1 ---
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
	#pprint.pprint(support)

	# --- 2. cal L_k ---
	k = 2
	L = [ [], [] ]
	L[1] = L_1
	S = [ [], [] ]

	while L[k - 1]:
		S.append([])
		# --- 2.1 cal S_k
		for item in L[k - 1]:
			if(support[tuple(item)]) > min_sup_num:
				S[k].append(item)
		print(" --- S_" + str(k) + " ---")
		pprint.pprint(S[k])

		L.append([])
		# --- 2.2 create L_k
		L[k] = createLk(S[k])
		print("--- L_" + str(k) + " ---")
		pprint.pprint(L[k])

		support = calSupport(dataset, L[k])
		print("--- L_" + str(k) + " support")
		pprint.pprint(support)
		#support.clear()
		k += 1


	
	

except Exception as e:
	print('error')
	pprint.pprint(e)

















