import os
import sys
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
    os.system('@echo off')
    if len(sys.argv) > 1:
        texto = ' '.join(sys.argv[1:])
        print(texto)
        play_audio(texto)
    else:
        while True:
            text = input("Digite uma expressão ou palavra (ou '!' para encerrar): ")
            if text.lower() == '!':
                break
            play_audio(text)


if __name__ == "__main__":
    main()