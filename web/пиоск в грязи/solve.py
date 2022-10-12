import requests

fs = open('fishes.txt', 'r').read().split('\n')
addr = 'http://gryaz.fish.lyceumctf.ru/%s'
ans = []


from tqdm import tqdm
for f in tqdm(range(len(fs))):
	r = requests.get(addr % fs[f])
	#print(f'requesting {addr % fs[f]} {f}/{len(fs)}')
	if len(r.text) == 1:
		print('got %s' % r.text, end='\n')
		ans.append((r.text, r.headers['number']))
print(ans)
print(''.join([x for x, y in list(sorted(ans, key=lambda tup: tup[1]))]))
