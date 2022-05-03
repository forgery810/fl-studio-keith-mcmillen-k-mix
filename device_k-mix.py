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
			else:					
				MixAct.track_volume(0, self.event.data2/127)

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

	def set_track(track_num):
		mixer.setTrackNumber(track_num)

	def track_volume(track_num, value, pickupMode = 2):
		mixer.setTrackVolume(track_num, value, pickupMode)

	def track_panning(track_num, value, pickupMode = 2):
		mixer.setTrackPan(track_num, value, pickupMode)

	def mute_track(track_num):
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
	
class ChanAct:

	def channel_volume(channel, volume, pickup):
		channels.setChannelVolume(channel, volume, pickup)

	def channel_panning(channel, pan, pickup):
		channels.setChannelPan(channel, pan, pickup)

