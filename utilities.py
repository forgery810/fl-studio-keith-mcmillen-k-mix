import device

def mapvalues(value, tomin, tomax, frommin, frommax):
	input_value = value
	if input_value == float('-inf'):
		input_value = -88
	solution = tomin + (tomax-(tomin))*((input_value - frommin) / (frommax - (frommin)))
	if  -0.01 < solution < 0.01:
		solution = 0
	return solution

class Send():

	def midi_msg(midi_id, chan, cc, data):
		device.midiOutMsg(midi_id, chan, cc, data)



