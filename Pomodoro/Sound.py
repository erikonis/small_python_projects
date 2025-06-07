import pygame

pygame.mixer.init()

class Sound():
    def __init__(self):
        pass
    def countdown(self):
        pygame.mixer.music.load("data/sounds/countdown.mp3")
        pygame.mixer.music.play()

    def countdown_finish(self):
        pygame.mixer.music.load("data/sounds/Countdown finish.mp3")
        pygame.mixer.music.play()

    def reset(self):
        pygame.mixer.music.load("data/sounds/reset.mp3")
        pygame.mixer.music.play()

    def start(self):
        pygame.mixer.music.load("data/sounds/start.mp3")
        pygame.mixer.music.play()

    def finish(self):
        pygame.mixer.music.load("data/sounds/finish work.mp3")
        pygame.mixer.music.play()

    def button_click(self):
        pygame.mixer.music.load("data/sounds/button_click.mp3")
        pygame.mixer.music.play()