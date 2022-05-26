from modes import Modes
from utilities import Send, mapvalues
from acquire import Get
from data import Button, Fader, Knob

class Led:

	def __init__(self, modes):

		self.window_leds = [Button.aux1, Button.main, Button.aux2, Button.aux3, Button.comp]
		self.track_leds = Button.numbers
		self.fader_leds = [Fader.one, Fader.two, Fader.three, Fader.four, Fader.five, Fader.six, Fader.seven, Fader.eight, Fader.master]
		self.modes = modes

	def update(self, focused, master):

		self.light_window()
		self.light_track(Get.current_track() - (self.modes[1].iter * 8))
		self.light_levels()
		self.light_pan(Get.current_track(), Get.focused_window())

		if Get.focused_window() == 1:
			self.light_channel_volume(Get.current_channel())

		if Get.is_playing():
			Send.midi_msg(144, 0, Button.stop, 0)

		else:
			Send.midi_msg(144, 0, Button.stop, 1)

		if Get.record_status():
			Send.midi_msg(144, 0, Button.record, 1)

		else:
			Send.midi_msg(144, 0, Button.record, 0)

		if self.modes[0].get_current_mode_name() == 'Master':
			Send.midi_msg(144, 0, Button.master, 1)
		else:
			Send.midi_msg(144, 0, Button.master, 0)

		if Get.metronome_status():
			Send.midi_msg(144, 0, Button.gate, 1)
		else:
			Send.midi_msg(144, 0, Button.gate, 0)

		if master == 0:
			self.light_master()
			Send.midi_msg(176, 0, Fader.master, int(mapvalues(Get.track_volume(0, 1), 0, 95, -40, 0)))

		self.light_mode()


	def light_master(self):

		vol = Get.track_volume(0, 1)

		if 0 > vol < -40:
			Send.midi_msg(176, 0, Fader.master, 0) 
		elif vol < 0:	
			Send.midi_msg(176, 0, Fader.master, int(mapvalues(vol, 0, 95, -40, 0)))
		else:
			Send.midi_msg(176, 0, Fader.master, int(mapvalues(vol, 96, 127, 0, 5.6)))


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
			vol = Get.track_volume(self.fader_leds.index(fader)  + (self.modes[1].iter * 8), 1)

			if 0 > vol < -40:
				Send.midi_msg(176, 0, fader - 1, 0) 
			elif vol < 0:	
				Send.midi_msg(176, 0, fader - 1, int(mapvalues(vol, 0, 95, -40, 0)))
			else:
				Send.midi_msg(176, 0, fader - 1, int(mapvalues(vol, 96, 127, 0, 5.6)))

	def light_mode(self):

		if self.modes[1].iter == 0:
			Send.midi_msg(176, 0, Knob.kfour, 0)
		elif self.modes[1].iter == 1:
			Send.midi_msg(176, 0, Knob.kfour, 37)
		elif self.modes[1].iter == 2:
			Send.midi_msg(176, 0, Knob.kfour, 98)
		elif self.modes[1].iter == 3:
			Send.midi_msg(176, 0, Knob.kfour, 127)

	def light_pan(self, track, focused):

		if focused == 0:
			Send.midi_msg(176, 0, Knob.ktwo, int(mapvalues(Get.track_panning(track), 0, 127, -1, 1)))
		elif focused == 1:
			Send.midi_msg(176, 0, Knob.ktwo, int(mapvalues(Get.channel_panning(track), 0, 127, -1, 1)))

	def track_or_channel(self):
		if Get.focused_window() == 0:
			return Get.current_track() + (self.modes[1].iter * 8)

		elif Get.focused_window() == 1:
			return Get.current_channel()

	def light_channel_volume(self, channel):
		Send.midi_msg(176, 0, Knob.kone, int(Get.channel_volume(channel) * 127))

