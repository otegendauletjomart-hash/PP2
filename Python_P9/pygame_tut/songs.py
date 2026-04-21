import pygame

pygame.mixer.music.load('foo.mp3') #once s
pygame.mixer.music.play(0)

pygame.mixer.music.load('foo.mp3') # infinite 
pygame.mixer.music.play(-1)

pygame.mixer.music.queue('next_song.mp3') # queue 

pygame.mixer.music.stop() #stopping