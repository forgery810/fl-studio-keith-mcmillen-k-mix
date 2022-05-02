import device
from data import *
from utilities import Send

class Modes():

	modes = {
			'master': {
						'index': 0,
						'options': ['Master Volume', 'Scroll'],
						'led': [127, 0],
						'midi_num': [144, 0, 9]
						},
			}

	def change_mode(self, mode_name):

		m = Modes.modes[mode_name]
		m['index'] += 1
		if m['index'] >= len(m['options']):
			m['index'] = 0
		# Send.midi_msg(m['midi_num'][0], m['midi_num'][1], m['midi_num'][2], m['led'][m['index']])

		# device.midiOutMsg(144, 0, Modes.modes[mode_name]['midi_num'], Modes.modes[mode_name]['led'][Modes.modes[mode_name]['index']])

	@staticmethod
	def get_mode_option(mode_name):
		return Modes.modes[mode_name]['index']



