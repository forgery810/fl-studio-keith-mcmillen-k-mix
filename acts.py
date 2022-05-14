import transport
import mixer
import ui 
import channels
import midi

class TrAct:

	def start():
		transport.start()	

	def stop():
		transport.stop()

	def setPosition(position = 0):
		transport.setSongPos(position)

	def record():
		transport.record()

	def loop():
		transport.setLoopMode()

	def overdub():
		transport.globalTransport(midi.FPT_Overdub, 112)

	def metronome():
		transport.globalTransport(midi.FPT_Metronome, 110)

	def loop_record():
		transport.globalTransport(midi.FPT_LoopRecord, 113)

class MixAct:

	def set_track(track_num):
		mixer.setTrackNumber(track_num)

	def track_volume(track_num, value, pickupMode = 1):
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

