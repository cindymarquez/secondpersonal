from PIL import Image
im = Image.open("dory.jpg.jpg")
im.rotate(0).show()
im.save("output.jpg", "jpeg")
list(im.getdata())
data = list(im.getdata())
'''
values = im.putdata(data)
'''
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
color = [darkBlue, red, lightBlue, yellow]
newimage = []
for i in data:
	sum = i[0] + i[1] + i[2] + i[3]
	if sum < 182:
		newimage.append(darkBlue)
	elif 182 <= sum  or sum < 364:
		newimage.append(red)
	elif 364 <= sum  or sum <= 546:
		newimage.append(lightBlue)
	elif sum > 546:
		newimage.append(yellow)
newdory = Image.new("RGB", (534,401))
newdory.putdata(newimage)
newdory.save("output.jpg", "jpeg")
newdory.show()
