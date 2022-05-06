# name=Keith McMillen K-Mix
# Author: ts-forgery
VERSION = 0.16

from data import Button, Knob, Fader
from modes import Modes
from utilities import mapvalues, Send
from leds import Led
import device
import transport
import mixer
import channels
import ui
import general
from midi import *
import midi
from acquire import Get
from acts import TrAct, MixAct, UIAct, ChanAct 

mode = Modes()
lights = Led()

def OnInit():
	print(f'Keith McMillen - K-Mix Version: {VERSION}')
	lights.reset()

def OnMidiMsg(event):

	print(event.midiId, event.data1, event.data2, event.midiChan)
	km = KM(event)
	lights.update()

def OnRefresh(flag):
	print(flag)
	if flag:
		lights.update()	

def OnIdle():
	pass

class KM:

	def __init__(self, event):
		self.midi_chan = event.midiChan
		self.channel = Get.current_channel()
		self.track = Get.current_track()
		self.event = event
		self.decide()
		lights.update()

	def decide(self):

		if self.event.midiId == 144:
			self.buttons()

		elif self.event.midiId == 176:
			if self.event.data1 in Fader.fader_numbers:
				self.faders()
			elif self.event.data1 in Knob.knob_numbers:
				self.knobs()

	def buttons(self):

		if self.event.data1 == Button.play:
			device.midiOutMsg(144, 0, 9, 127)
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
			UIAct.focus("playlist")

		elif self.event.data1 == Button.aux3:
			UIAct.focus("piano")

		elif self.event.data1 == Button.comp:
			UIAct.focus("browser")

		elif self.event.data1 == Button.byps:
			UIAct.enter()

		elif self.event.data1 == Button.fine:
			UIAct.up()

		elif self.event.data1 == Button.vu:
			UIAct.down()

		elif self.event.data1 == Button.master:
			mode.change_mode('master')

		if Get.mixer_focused():

			if self.event.data1 in Button.numbers:
				MixAct.set_track(Button.numbers.index(self.event.data1) + 1)

			else:
				pass



		self.event.handled = True

	def faders(self):

		if self.event.data1 == Fader.master:
			if mode.get_mode_option('master') == 1:
				if Get.mixer_focused():
					MixAct.set_track(int(mapvalues(self.event.data2, 0, 64, 0, 127)))
					ui.scrollWindow(0, self.track)
				elif Get.channels_focused():
					print('channels focus')
					channels.selectOneChannel(int(round(mapvalues(self.event.data2, channels.channelCount()-1, 0, 0, 127), 0)))	
				self.handled = True	
			else:					
				MixAct.track_volume(0, self.event.data2/127)

				self.event.handled = True

		if Get.mixer_focused() and self.event.data1 != Fader.master:
			MixAct.track_volume(self.event.data1 - 21, self.event.data2 / 127)

		self.event.handled = True

	def knobs(self):

		if Get.channels_focused():
			if self.event.data1 == Knob.kone:
				ChanAct.channel_volume(self.channel, self.event.data2/127, 2)

			elif self.event.data1 == Knob.ktwo:
				ChanAct.channel_panning(self.channel, mapvalues(self.event.data2, -1, 1, 0, 127), 2)

		elif Get.mixer_focused():
			if self.event.data1 == Knob.kone:
				MixAct.track_volume(self.track, self.event.data2/127, 2)

			elif self.event.data1 == Knob.ktwo:
				MixAct.track_panning(self.track, mapvalues(self.event.data2, -1, 1, 0, 127), 2)
		self.event.handled = True
