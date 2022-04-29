# name=Keith McMillen K-Mix
# Author: ts-forgery
# Version 0.1

import device
import data as d
import transport
import mixer

def OnMidiMsg(event):

	print(event.midiId, event.data1, event.data2, event.midiChan)
	km = KM(event)



class KM:

	def __init__(self, event):
		self.midi_chan = event.midiChan
		self.event = event
		self.decide()

	def decide(self):

		if self.event.midiId == 144:
			if self.event.data1 == d.play:
				transport.start()
				self.event.handled = True

			elif self.event.data1 == d.stop:
				transport.stop()
				self.event.handled = True

			elif self.event.data1 == d.back:
				transport.setSongPos(0)
				self.event.handled = True

			elif self.event.data1 == d.record:
				transport.record()
				self.event.handled = True

		elif self.event.midiId == 176:
			if self.event.data1 == d.master_vol:
				mixer.setTrackVolume(0, self.event.data2/127)

		else:
			self.event.handled = True
	
