# Load/Save settings to a JSON file
import json 
import os 

DEFAULT_SETTINGS = {
    'resolution': '1920x1080',
    'microphone': 'default',
    'display': 0,
    'time_before': 90, # 1min 30s
    'time_after': 30, # 30s
    'hotkey': 'shift+f3',
    'save_location': './recordings'
}

def load_settings():
    """
    Load settings from config.json, create with defaults if none
    """
    pass 

def save_settings(settings):
    """
    Save settings dict to config.json
    """
    pass 

def get_microphones():
    """
    Returns list of available microphones
    """
    pass 

def get_displays():
    """
    Returns list of available displays (may extend to windows)
    """
    pass

def validate_settings(settings):
    """
    Check if settings are valid
    """
    pass