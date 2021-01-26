import pygame
import os
import tkinter
from tkinter.filedialog import askdirectory

def play():
    pygame.mixer.music.load(play_list.get(tkinter.ACTIVE))
    var.set(play_list.get(tkinter.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def order():
    var = 0
    pygame.mixer.music.load(music_list[var])
    pygame.mixer.music.play()
    var += 1
    while var != len(music_list):   
        pygame.mixer.music.queue(music_list[var])
        var += 1

music_player = tkinter.Tk()
music_player.title("Music Player")
music_player.geometry("350x400")

directory = askdirectory()
os.chdir(directory)
music_list = os.listdir()

play_list = tkinter.Listbox(music_player, font = "Arial 12 bold", bg = "black", fg = "white", selectmode = tkinter.SINGLE)

for item in music_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

Button1 = tkinter.Button(music_player, width = 3, height = 2, font = "Arial 12 bold", text = "Play", command = play, bg = "white")
Button2 = tkinter.Button(music_player, width = 3, height = 2, font = "Arial 12 bold", text = "Stop", command = stop, bg = "white")
Button3 = tkinter.Button(music_player, width = 3, height = 2, font = "Arial 12 bold", text = "Pause", command = pause, bg = "white")
Button4 = tkinter.Button(music_player, width = 3, height = 2, font = "Arial 12 bold", text = "Unpause", command = unpause, bg = "white")
Button5 = tkinter.Button(music_player, width = 3, height = 2, font = "Arial 12 bold", text = "Play in Order", command = order, bg = "white")

var = tkinter.StringVar()
music_title = tkinter.Label(music_player, font = "Arial 12 bold", textvariable = var)

music_title.pack()
Button1.pack(fill = "x")
Button2.pack(fill = "x")
Button3.pack(fill = "x")
Button4.pack(fill = "x")
Button5.pack(fill = "x")
play_list.pack(fill = "both", expand = "yes")

music_player.mainloop()