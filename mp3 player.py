import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init() # Initialize pygame

file_paths = []
paused = False
current_index = 0 # Initialize the global variables

window = tk.Tk() # Create window
window.title("MP3 Player")

def play_pause_button_click():
    global paused
    if not pygame.mixer.music.get_busy() or paused: #checks if the music mixer in Pygame is currently playing any music. 
        #The not pygame.mixer.music.get_busy() is True when there is no music playing.
        if file_paths:
            pygame.mixer.music.load(file_paths[current_index]) #load the file from the index in the file path
            pygame.mixer.music.play() #Play the music
            paused = False
        elif paused:
            pygame.mixer.music.unpause()
            paused = False
    else:
        pygame.mixer.music.pause() 
        paused = True #pauses the music when there is music playing

def open_file_button_click():
    global file_paths, current_index  # Declare file path and current_index as global
    directory = filedialog.askdirectory(title="Select a Directory") #allows you to select a directory
    if directory:
        file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".mp3")] #os.path.join(directory, file): For each selected filename (those that end with ".mp3"), os.path.join() is used to combine 
        #the directory path (directory) and the filename. This creates a full file path.  The list comprehension iterates through the list of filenames obtained from os.listdir(directory) 
        # and selects only the filenames that end with ".mp3"
        current_index = 0
        play_pause_button_click()

def next_track():
    global current_index  # Declare current_index as global
    if file_paths:
        current_index = (current_index + 1) % len(file_paths) #The % (modulo) operator is used here to ensure that the index wraps around when it reaches the end of the list. len(file_paths) gives you the length of the file_paths list, which represents the number of items in the list. When you take the modulo of (current_index + 1) with the length of the list, 
        #it will ensure that if the index exceeds the length of the list, it will wrap around to the beginning.
        play_pause_button_click()

def prev_track():
    global current_index  # Declare current_index as global
    if file_paths:
        current_index = (current_index - 1) % len(file_paths)
        play_pause_button_click()

next_button = tk.Button(window, text="Next", bg="orange", command=next_track) #creates button
next_button.pack() #places button

prev_button = tk.Button(window, text="Previous", bg="orange", command=prev_track)
prev_button.pack()

play_pause_button = tk.Button(window, text="Play/Pause", bg="orange", command=play_pause_button_click)
play_pause_button.pack()

open_file_button = tk.Button(window, text="Select Directory", bg="orange", command=open_file_button_click)
open_file_button.pack()

window.configure(bg="black") #sets window background to black
window.mainloop()
