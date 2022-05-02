import transport
import patterns
import ui

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

	def channels_focused():
		return ui.getFocused(1)