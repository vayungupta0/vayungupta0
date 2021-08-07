from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from tkinter import*

app = Ursina()
grass_texture  = load_texture('assets/grass.png')
stone_texture  = load_texture('assets/stone.png')
brick_texture  = load_texture('assets/wood.png')
dirt_texture   = load_texture('assets/soil.png')
wool_texture   = load_texture('assets/wool.png')
sky_texture    = load_texture('assets/sky.png')
plank_texture  = load_texture('assets/plank.png')
slime_texture  = load_texture('assets/slime4.png')
glass_texture  = load_texture('assets/glass2.png')
arm_texture    = load_texture('assets/arm_texture.png')
punch_sound    = Audio('assets/assets_punch_sound.wav',loop = False, autoplay = False)
block_pick     = 1

window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
	global block_pick

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8

class Voxel(Button):
	def __init__(self, position = (0,0,0),texture=grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)))

	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = wool_texture)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = slime_texture)
				if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = plank_texture)
				if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)

			if key == 'left mouse down':
				punch_sound.play()
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

for z in range(60):
	for x in range(60):
		voxel = Voxel(position = (x,3,z))

player = FirstPersonController()
sky = Sky()
app.run()
