import pydub
from pydub import AudioSegment
import pycse

# Load the audio file
audio = AudioSegment.from_file("audio_file.mp3")

# Split the audio file into two separate files
first_half = audio[:len(audio)//2]
second_half = audio[len(audio)//2:]

# Save the split audio files
first_half.export("first_half.mp3", format="mp3")
second_half.export("second_half.mp3", format="mp3")

# Connect to the Bluetooth speakers
speaker1 = pycse.AudioDevice('{0000111e-0000-1000-8000-00805f9b34fb}', 'Speaker 1')
speaker2 = pycse.AudioDevice('{0000111e-0000-1000-8000-00805f9b34fb}', 'Speaker 2')

# Play the split audio files on each speaker
speaker1.play("first_half.mp3")
speaker2.play("second_half.mp3")

# Disconnect from the speakers
speaker1.disconnect()
speaker2.disconnect()

# replace 'Speaker 1' and 'Speaker 2' with the actual names of your Bluetooth speakers

"""
Pair the bluetooth speakers with the computer before running the code.
"""

###################
## MAC ############
###################

import pyaudio
import time

# Set up the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=44100,
                output=True)

# Connect to the Bluetooth speakers
speaker1 = pyaudio.paDeviceInfo(index=1)
speaker2 = pyaudio.paDeviceInfo(index=2)

# Load the audio file
audio = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=2,
                                rate=44100,
                                file="audio_file.mp3",
                                stream_callback=lambda in_data, frame_count, time_info, status: (in_data, pyaudio.paContinue))

# Start playing the audio on both speakers
audio.start_stream()
time.sleep(1)

# Disconnect from the speakers
speaker1.disconnect()
speaker2.disconnect()

# Close the audio stream
audio.stop_stream()
audio.close()
p.terminate()
