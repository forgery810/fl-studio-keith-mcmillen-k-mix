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

	def current_track():
		return mixer.trackNumber()

	def channels_focused():
		return ui.getFocused(1)

	def current_channel():
		return channels.channelNumber()

	def focused_window():
		return ui.getFocusedFormID()

	def pattern_trigs(pattern):
		trigs = []
		for step in range(0, pattern_length(pattern)):
			trigs.append(step)
		print(trigs)

