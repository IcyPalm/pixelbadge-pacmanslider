"""
Pixelbadge Founders edition PacMan scroller
Copyright Marijn Pool (IcyPalm) 
"""
import rgb, time

ghost_right = [
0x000000FF, 0x000000FF, 0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0x000000FF, 0x000000FF,
0x000000FF, 0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0x000000FF, 
0x000000FF, 0xD50000FF, 0xFFFFFFFF, 0xFFFFFFFF, 0xD50000FF, 0xFFFFFFFF, 0xFFFFFFFF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0x3F51B5FF, 0xFFFFFFFF, 0xD50000FF, 0x3F51B5FF, 0xFFFFFFFF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0x000000FF, 0xD50000FF, 0x000000FF, 0xD50000FF, 0x000000FF, 0xD50000FF,  
]
ghost_left = [
0x000000FF, 0x000000FF, 0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0x000000FF, 0x000000FF,
0x000000FF, 0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0x000000FF, 
0x000000FF, 0xD50000FF, 0xFFFFFFFF, 0xFFFFFFFF, 0xD50000FF, 0xFFFFFFFF, 0xFFFFFFFF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0xFFFFFFFF, 0x3F51B5FF, 0xD50000FF, 0xFFFFFFFF, 0x3F51B5FF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 0xD50000FF, 
0x000000FF, 0xD50000FF, 0x000000FF, 0xD50000FF, 0x000000FF, 0xD50000FF, 0x000000FF, 0xD50000FF,  
]
pacman_left_1 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0x000000FF, 0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,  
]
pacman_left_2 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0x000000FF, 0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,  
]
pacman_left_3 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0x000000FF, 0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,  
]
pacman_left_4 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,  
]
pacman_right_1 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF, 0x000000FF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
]

pacman_right_2 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF, 0x000000FF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
]

pacman_right_3 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF, 0x000000FF, 0x000000FF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
]

pacman_right_4 = [
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0xA6880FFF, 0xA6880FFF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0xA6880FFF,
0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF,	0x000000FF,
0x000000FF, 0x000000FF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0xA6880FFF, 0x000000FF,	0x000000FF,
]


while True:
	for y in range(0,4):
		base=-8+12*y
		rgb.clear()
		rgb.image(pacman_right_1, pos=(base,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_2, pos=(base+1,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_3, pos=(base+2,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_4, pos=(base+3,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_3, pos=(base+4,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_2, pos=(base+5,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_1, pos=(base+6,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_2, pos=(base+7,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_3, pos=(base+8,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_4, pos=(base+9,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_3, pos=(base+10,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_right_2, pos=(base+11,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
	for y in range(0,40):
		rgb.clear()
		rgb.image(ghost_left, pos=(31-y,0), size=(8,8))
		time.sleep(0.15)
	for y in range(-8,32):
		rgb.clear()
		rgb.image(ghost_right, pos=(y,0), size=(8,8))
		time.sleep(0.15)
	for y in range(0,4):
		base=32-12*y
		rgb.clear()
		rgb.image(pacman_left_1, pos=(base,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_2, pos=(base-1,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_3, pos=(base-2,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_4, pos=(base-3,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_3, pos=(base-4,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_2, pos=(base-5,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_1, pos=(base-6,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_2, pos=(base-7,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_3, pos=(base-8,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_4, pos=(base-9,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_3, pos=(base-10,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()
		rgb.image(pacman_left_2, pos=(base-11,0), size=(8,8))
		time.sleep(0.1)
		rgb.clear()