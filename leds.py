from modes import Modes
from utilities import Send, mapvalues
from acquire import Get
from data import Button, Fader, Knob

class Led:

	def __init__(self):
		self.window_leds = [Button.aux1, Button.main, Button.aux2, Button.aux3, Button.comp]
		self.track_leds = Button.numbers
		self.fader_leds = [Fader.one, Fader.two, Fader.three, Fader.four, Fader.five, Fader.six, Fader.seven, Fader.eight]

	def update(self):

		self.light_window()
		self.light_track(Get.current_track())
		self.light_levels()

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

	def light_track(self, track_number):

		for track in self.track_leds:
			if track_number == self.track_leds.index(track) + 1:
				Send.midi_msg(144, 0, track, 1)
			else:
				Send.midi_msg(144, 0, track, 0)

	def light_levels(self):

		for fader in self.fader_leds:
			vol = Get.track_volume(self.fader_leds.index(fader), 1)

			if 0 > vol < -40:
				Send.midi_msg(176, 0, fader - 1, 0) 
			elif vol < 0:	
				Send.midi_msg(176, 0, fader - 1, int(mapvalues(vol, 0, 95, -40, 0)))
			else:
				Send.midi_msg(176, 0, fader - 1, int(mapvalues(vol, 96, 127, 0, 5.6)))

	

