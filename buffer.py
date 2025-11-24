# Circular buffer
from collections import deque
import numpy as np

class BufferManager:
    def __init__(self, time_before, fps, resolution, audio_rate):
        """
        Initialize cirular buffers for video and audio
        """
        pass

    def add_frame(self, frame, timestamp):
        """
        Add video frame to buffer and remove oldest if full
        """
        pass 

    def add_audio(self, audio_chunk, timestamp):
        """
        Add audio chunk to buffer, and remove oldest if full
        """
        pass 

    def get_buffer_contents(self):
        """
        Return all frames and audio from buffer with timestamps
        """
        pass 

    def clear(self):
        """
        Clears both buffers
        """
        pass 

