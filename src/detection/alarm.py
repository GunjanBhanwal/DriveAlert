import pygame
import os

alarm_playing = False

def play_alarm():
    global alarm_playing
    if not alarm_playing:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        alarm_file = r'C:\Users\Gunjan\OneDrive\Desktop\projecttt\DriveAlert\src\alarm\alarm.mp3'
        if not os.path.exists(alarm_file):
            raise FileNotFoundError(f"Alarm file not found at: {alarm_file}")
        pygame.mixer.music.load(alarm_file)
        pygame.mixer.music.play(-1)
        alarm_playing = True

def stop_alarm():
    global alarm_playing
    if pygame.mixer.get_init() and alarm_playing:
        pygame.mixer.music.stop()
        alarm_playing = False
