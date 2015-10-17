##########################################
# Playing audio using pygame module
##########################################

#!/usr/bin/python



import pygame
import time

print("Playback started")

pygame.init()
song = pygame.mixer.Sound('motion-sound.ogg')
song.play()
time.sleep(2)
pygame.quit()

print("Playback finished")

