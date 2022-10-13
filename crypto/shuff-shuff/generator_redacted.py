import random

flag = """
SOME TEXT
SOME FLAG (NOT FORMATTED)
""".strip()
sd = random.randint(1, 10**5)
random.seed(sd)

fl = list(flag)
random.shuffle(fl)

print(''.join(fl), end="")
