# Pynput to listen for hotkey
from pynput import keyboard
import threading

class HotkeyListener:
    def __init__(self, hotkey, callback):
        """
        Initialize hotkey listener; 
        hotkey = string like 'shift+f3'
        callback = function to call when hotkey is pressed
        """
        pass 

    def start(self):
        """
        Start listening for hotkey in background thread
        """
        pass

    def stop(self):
        """
        Stop listening
        """
        pass 

    def _parse_hotkey(self, hotkey):
        """
        Convert 'shift+f3' tp pynput key combination
        """
        pass 

    def _on_hotkey_pressed(self):
        """
        Called when hotkey is pressed
        """
        pass