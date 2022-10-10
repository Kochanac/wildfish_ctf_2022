import string, random, hashlib

"""
Решение:

1. Догадаться что в ямле означают эти буквы
2. Прочитать остальное и найти циклы

2 alt: Догадаться что это мд5

"""


letters_available = string.ascii_letters + "{}6"

flag = "PbI6bI{hi_katya}"



def randstr(ln: int) -> str:
	return ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(ln)])

fmt = """
{randstr}: &{hash}
  letter: "{let}"
  prev:
    <<: *{prev_hash}
""".strip()
fmt_0 = """
{randstr}: &{hash}
  letter: "{let}"
""".strip()

def genfmt(ind: int, let: str, prev: str):
	if prev == "":
		return fmt_0.format(
			randstr=randstr(3),
			hash=gethash(ind, let),
			let=let
		)
	return fmt.format(
		randstr=randstr(3),
		hash=gethash(ind, let),
		let=let,
		prev_hash=prev
	)

def gethash(ind, let):
	return hashlib.md5(f"{ind}{let}".encode()).hexdigest()

flag = [(a, b, gethash(a, b)) for a, b in enumerate(flag)]


letters = []

for i in range(len(flag)):
	if i == 0:
		letters.append(genfmt(flag[0][0], flag[0][1], ""))
	else:
		letters.append(genfmt(flag[i][0], flag[i][1], gethash(flag[i-1][0], flag[i-1][1])))


for x in range(20):
	flagref = random.choice(flag)
	letters.append(
		genfmt(random.randint(0, 3), random.choice(letters_available), gethash(flagref[0], flagref[1]))
	)


random.shuffle(letters)
print("\n".join(letters))



