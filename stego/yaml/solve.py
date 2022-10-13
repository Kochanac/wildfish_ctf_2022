x = open("fish.yaml").read().split("\n")

blocks = zip(x[::4], x[1::4], x[2::4], x[3::4])


# edit fish yaml to make 4 lines start

letters = []

for bl in blocks:
	letters.append({
		"addr": bl[0].split("&")[1],
		"letter": bl[1].split(": ")[1][1:-1],
		"prev": bl[3].split("*")[1]
	})


mp = {}
for l in letters:
	mp[l["addr"]] = {'let': l["letter"], "prev": l["prev"]}


f = "0f7bf63a71126824fd11afac7ddf1fa8"
# f = "b8c9d8ae4b0ef96eaf9cc71f1760817e"

genstr = ""

lox = mp[f]
while lox["prev"] != "":
	genstr += lox["let"]
	lox = mp[lox["prev"]]

genstr += lox["let"]

print(genstr[::-1])
