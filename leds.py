from modes import Modes
from utilities import Send
from acquire import Get
from data import Button, Fader, Knob

class Led:

	def update(self):
		print('led update')
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



