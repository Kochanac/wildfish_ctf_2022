flag = """
🐠🎣
🐟🐡🎣
♓🎣
🐟🍣🐠🐡
🐟🐡🎣
♓🎣
🐟♓🐠🐡🎣
🐟🍣🐡🎣
♓🐡🎣
🐟🐠🐡🎣
♓🎣
🐟🍣♓🐠🎣
🐟🎣
🐡🎣
🐟🍣♓🐡🎣
🐟🍣♓🐠🎣
🐟🍣🐠🐡
🍣🐡🎣
🐟🍣♓🐠🎣
🍣🎣
♓🐡🎣
🐟🍣🐡🎣
🐟🍣🎣
🍣🐡🎣
🐟🐠🎣
🍣🐡🎣
🐟🍣♓🐡🎣
🍣🐠🐡🎣
🍣♓🐠🐡🎣
""".strip().split("\n")

print(flag)

real_flag = ["$"]*len(flag)

from string import printable
import re
from requests import get

printable = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"{}"

for ch in printable:
	rsp = get(f"http://shrimp.fish.lyceumctf.ru/?eng_text={ch}").text
	t = re.findall("<p>(.*)</p>", rsp)
	for i, f in enumerate(flag):
		if f in t:
			real_flag[i] = ch


print(''.join(real_flag))

