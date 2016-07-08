#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
	
def deal(x_bond, y_bond, draw_op):  

	# font setting 
	fontsize = min(x_bond, y_bond) // 11
	font_1 = ImageFont.truetype("/Library/Fonts/Tahoma.ttf", fontsize)
	# add 
	draw_op.text([x_bond*0.9 - fontsize , y_bond*0.1], "999", fill=(255, 0, 0), font = font_1)



# open
img = Image.open("self_1.jpg")
# show page
# size 
bond1,bond2 = img.size 

# draw 
draw_op = ImageDraw.Draw(img)
deal(bond1, bond2, draw_op)

# save
img.show()
img.save("after_draw.jpg")
 
