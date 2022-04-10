import random
import webbrowser

begin = "http://gs.3g.cn/D/"
end = "/w"
amount = 5 #

def spawn():
	i = 0
	while i < amount:
		x = random.randint(1118481, 14803425)
		code = hex(x)[2:]
		webbrowser.open(begin + code + end)
		print(begin + code + end)
		i = i + 1
input("Start?")
spawn()
while True:
	input("Run again?")
	spawn()

