import random

flag = """
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
the answer is l c t f bracket five h u f f underscore five h u f f underscore five h u f f
"""
sd = random.randint(1, 10**5)
random.seed(sd)

fl = list(flag)
random.shuffle(fl)

print(''.join(fl))
