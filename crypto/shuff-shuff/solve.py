from requests import get
import json


common_words = ["the"]
def score(text):
	tx = text.lower()
	sc = 0
	for x in text.split():
		if x in common_words:
			sc += 1
	return sc


def score(text):
	tx = text.lower()
	sc = 0

	for a, b in zip(tx, tx[1:]):
		if a + b in ["th", "he", "in", "er", "an", "re", "on", "at"]:
			sc += 1
		# if a + b in ["th", "he", "in"]:
		# 	sc += 1
	return sc


import random
flag = open("out.txt", 'r').read()

max = [{"ans": "", "score": 0} for _ in range(50)]
def max_add(ans, score):
	if max[-1]["score"] > score:
		return
	
	max[-1] = {"ans": ans, "score": score}
	i = 1
	while max[-i-1]["score"] < max[-i]["score"] and i + 1 != len(max):
		tmp = max[-i-1]
		max[-i-1] = max[-i]
		max[-i] = tmp
		i += 1

def unshuffle(fl):
	x = list(range(len(fl)))
	random.shuffle(x)
	ush = [0]*len(fl)
	for ind in range(len(fl)):
		ush[ind] = fl[x.index(ind)]
	return ''.join(ush)


from tqdm import tqdm
for x in tqdm(range(10**5)):
	random.seed(x)
	
	fl = list(flag)
	ans = unshuffle(fl)
	
	max_add(ans, score(ans))
	

for x in max[::-1]:
	print(x)
