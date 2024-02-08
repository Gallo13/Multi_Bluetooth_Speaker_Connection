# pip install pybluez

import os
import subprocess
from bluetooth import *

"""
1) add error handling
2) may need to fix play_audio to work with given audio file format and playback hardware
"""


# Scan for available Bluetooth devices
def scan_for_devices():
    nearby_devices = discover_devices(lookup_names=True)
    return nearby_devices


# Connect to a specific device
def connect_to_device(device):
    sock = BluetoothSocket(RFCOMM)
    sock.connect((device, 1))
    return sock


# Play an audio clip on a specific device
def play_audio(device, file_path):
    sock = connect_to_device(device)
    with open(file_path, 'rb') as f:
        data = f.read(1024)
        while data:
            sock.send(data)
            data = f.read(1024)
    sock.close()


# Scan - Connect - Play Audio
devices = scan_for_devices()
for i, device in enumerate(devices):
    play_audio(device, '/path/to/audio/files/{}.wav'.format(i))
  
