import os
import pygame
from gtts import gTTS


def play_audio(text):
    tts = gTTS(text=text, lang='pt')
    pygame.mixer.quit()
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def main():
    while True:
        text = input("Digite uma expressão ou palavra (ou '!' para encerrar): ")
        if text.lower() == '!':
            break
        play_audio(text)


if __name__ == "__main__":
    main()