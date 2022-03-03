import pygame
from pygame import mixer
mixer.init()
pygame.init()

mixer.music.load("song.mp3")
mixer.music.set_volume(1)
mixer.music.play()

pygame.time.wait(10000)