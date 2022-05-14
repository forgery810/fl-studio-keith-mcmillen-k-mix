import device
from data import *
from utilities import Send
from acquire import Get

# class Modes():



class Modes:

	def __init__(self, name, categories):
		self.name = name
		self.iter = 0
		self.categories = categories
		self.ranges = [range(1, 9), range(9, 17), range(17, 25), range(25, 33) ]
	

	def iterate(self):
		self.iter += 1
		if self.iter >= self.get_cat_len():
			self.iter = 0

	def get_cat_len(self):
		return len(self.categories)

	def get_current_mode_name(self):
		return self.categories[self.iter]

	def set_range(self, cc):
		if cc in range(0, 31):
			self.iter = 0
		elif cc in range(32, 63):
			self.iter = 1
		elif cc in range(63, 95):
			self.iter = 2
		elif cc in range(95, 127):
			self.iter = 3

	def update_iter(self, num):
		print(Get.current_track())
		for r in self.ranges:
			if num in r:
				self.iter = self.ranges.index(r)
				print(r)




