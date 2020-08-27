"""Reverse a song by playing its beats forward starting from the end of the song"""
import echonest.remix.audio as audio

# Easy around wrapper mp3 decoding and Echo Nest analysis
audio_file = audio.LocalAudioFile("file_example_WAV_1MG.wav")

# You can manipulate the beats in a song as a native python list
beats = audio_file.analysis.beats
beats.reverse()

# And render the list as a new audio file!
audio.getpieces(audio_file, beats).encode("file_example_WAV_1MGBackwardsByBeat.wav")