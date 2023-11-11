import socket
import pyaudio
import threading
import tkinter as tk

# Client configuration
SENDER_HOST = '0.0.0.0'
SENDER_PORT = 12345     # Port for client
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
MAX_PACKET_SIZE = 4096  # Maximum size of each packet

server_ip = '192.168.41.219'  # Server's IP address
server_port = 12345  # Server's port

# Initialize PyAudio
audio = pyaudio.PyAudio()
sender_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Set up sender socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start sender thread
def send_audio():
    while True:
        data = sender_stream.read(CHUNK)
        for i in range(0, len(data), MAX_PACKET_SIZE):
            chunk = data[i:i+MAX_PACKET_SIZE]
            sender_socket.sendto(chunk, (server_ip, server_port))

sender_thread = threading.Thread(target=send_audio)
sender_thread.start()

# Rest of the code (key bindings, etc.) remains unchanged
