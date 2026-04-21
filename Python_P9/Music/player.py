import pygame

class Player:
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0
        self.is_playing = False

        pygame.mixer.init()

    def load_current(self):
        track = self.playlist[self.index]
        pygame.mixer.music.load(track)
        return track

    def play(self):
        if not self.is_playing:
            self.load_current()
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def pause(self):
        pygame.mixer.music.pause()
        self.is_playing = False

    def next(self):
        self.index += 1
        if self.index >= len(self.playlist):
            self.index = 0

        pygame.mixer.music.stop()
        self.load_current()
        pygame.mixer.music.play()
        self.is_playing = True

    def previous(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.playlist) - 1

        pygame.mixer.music.stop()
        self.load_current()
        pygame.mixer.music.play()
        self.is_playing = True

    def get_current_track(self):
        return self.playlist[self.index].split("/")[-1]