from modes import Modes
from utilities import Send
from acquire import Get
from data import Button, Fader, Knob

class Led:

	def __init__(self):
		self.window_leds = [Button.main, Button.aux1, Button.aux2, Button.aux3, Button.comp]


	def update(self):

		self.light_window()

		if Get.is_playing():
			Send.midi_msg(144, 0, Button.stop, 0)

		else:
			Send.midi_msg(144, 0, Button.stop, 1)

		if Get.record_status():
			Send.midi_msg(144, 0, Button.record, 1)

		else:
			Send.midi_msg(144, 0, Button.record, 0)

		if Modes.get_mode_option('master'):
			Send.midi_msg(144, 0, Button.master, 0)

		else:
			Send.midi_msg(144, 0, Button.master, 1)

	def reset(self):
		Send.midi_msg(144, 0, Button.master, 1)

	def light_window(self):

		for led in self.window_leds:
			if Get.focused_window() == self.window_leds.index(led):
				Send.midi_msg(144, 0, self.window_leds[Get.focused_window()], 1)
			else:
				Send.midi_msg(144, 0, led, 0)


