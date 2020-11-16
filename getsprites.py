#pirmansx
#date nov 16 2020 / 21:39
#getsprites.py
#python3

from PIL import Image

img = Image.open("img.png")
w,h = img.size
index = 0

print(img.mode)
if(img.mode != "RGBA"):
	img = img.convert("RGBA")
	print("converted to RGBA")

def in_range(n,x):
	return (x[0] >= n[0] and x[0] <= n[2] and x[1] >= n[1] and x[1] <= n[3])

def getcor(s):
	openlist = []
	closelist = []
	x = []
	y = []
	openlist.append(s)
	while(len(openlist) > 0):
		for i in openlist:
			openlist.remove(i)
			closelist.append(i)
			for j in range(-1,2):
				for k in range(-1,2):
					if( j != 0 or k != 0):
						n = (i[0]+j,i[1]+k)
						if(in_range((0,0,w-1,h-1),n)):
							if(img.getpixel(n)[3] != 0 and n not in openlist and n not in closelist):
								openlist.append(n)
	for i in closelist:
		x.append(i[0])
		y.append(i[1])
	x.sort()
	y.sort()
	cor = (x[0],y[0],x[len(x)-1]+1,y[len(y)-1]+1)
	return cor

for x in range(w):
	for y in range(h):
		if(img.getpixel((x,y))[3] != 0):
			cor = getcor((x,y))
			bg = Image.new("RGBA", (cor[2] - cor[0], cor[3] - cor[1]), (255,255,255,0))
			img2 = img.crop(cor)
			img.paste(bg,(cor[0],cor[1]))
			img2.save(str(index)+"_s.png")
			print(str(index)+"_s.png save")
			index += 1
