import transport
import patterns
import ui
import channels 
import mixer

class Get:

	def is_playing():
		return transport.isPlaying()

	def song_length():
		return transport.getSongLength()

	def pattern_length(pattern):
		return patterns.getPatternLength(pattern)

	def pattern_number():
		return patterns.patternNumber()

	def record_status():
		return transport.isRecording()

	def mixer_focused():
		return ui.getFocused(0)

	def track_volume(track, mode):
		return mixer.getTrackVolume(track, mode)

	def current_track():
		return mixer.trackNumber()

	def channels_focused():
		return ui.getFocused(1)

	def trig_bit(channel, step):
		return channels.getGridBit(channel, step)

	def current_channel():
		return channels.channelNumber()

	def channel_volume(chan):
		return channels.getChannelVolume(chan)

	def focused_window():
		return ui.getFocusedFormID()

	def pattern_trigs(pattern):
		trigs = []
		for step in range(0, Get.pattern_length(pattern)):
			trigs.append(Get.trig_bit(pattern, step))
		print(trigs)

	def track_panning(track):
		return mixer.getTrackPan(track)

	def channel_panning(track):
		return channels.getChannelPan(track)

	def loop_mode():
		return transport.getLoopMode()

	def metronome_status():
		return ui.isMetronomeEnabled()

	


