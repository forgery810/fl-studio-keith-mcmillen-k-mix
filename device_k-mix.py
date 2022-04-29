# name=Keith McMillen K-Mix
# Author: ts-forgery
# Version 0.12

import device
from data import Button, Knob, Fader
import transport
import mixer
import ui

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
			if self.event.data1 == Button.play:
				TrAct.start()

			elif self.event.data1 == Button.stop:
				TrAct.stop()

			elif self.event.data1 == Button.back:
				TrAct.setPosition()

			elif self.event.data1 == Button.record:
				TrAct.record()

			elif self.event.data1 == Button.main:
				UIAct.focus("channels")

			elif self.event.data1 == Button.aux1:
				UIAct.focus("mixer")

			elif self.event.data1 == Button.aux2:
				UIAct.focus("piano")

			elif self.event.data1 == Button.aux3:
				UIAct.focus("playlist")

			elif self.event.data1 == Button.comp:
				UIAct.focus("browser")

			elif self.event.data1 == Button.byps:
				UIAct.enter()

			elif self.event.data1 == Button.fine:
				UIAct.up()

			elif self.event.data1 == Button.vu:
				UIAct.down()

			self.event.handled = True



		elif self.event.midiId == 176:
			if self.event.data1 == Fader.master:
				MixAct.setVol(0, self.event.data2/127)

		self.event.handled = True

class TrAct:

	def start():
		transport.start()	

	def stop():
		transport.stop()

	def setPosition(position = 0):
		transport.setSongPos(position)

	def record():
		transport.record()

class MixAct:

	def setVol(track_num, value, pickupMode = 2):
		mixer.setTrackVolume(track_num, value, pickupMode)

	def setPan(track_num, value, pickupMode = 2):
		mixer.setTrackPan(track_num, value, pickupMode)

	def mute(track_num):
		mixer.muteTrack(track_num)

class UIAct:

	window_constants = ["mixer", "channels", "playlist", "piano", "browser"]

	def up():
		ui.up()

	def down():
		ui.down()

	def left():
		ui.left()

	def right():
		ui.right()

	def enter():
		ui.enter()

	def message(message):
		ui.setHintMsg(message)

	def focus(window_index):
		ui.showWindow(UIAct.window_constants.index(window_index))

	
