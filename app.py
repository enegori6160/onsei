import time
import pygame
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def add_echo(audio_segment, gain_in=0.6, gain_out=0.6, delay=100):
    """音声にエコー効果を追加する関数"""
    segment = audio_segment
    # エコー効果の追加
    for _ in range(3):  # 3回繰り返しでエコーを重ねる
        segment = segment.overlay(audio_segment - delay, gain_during_overlay=gain_in)
        gain_in *= gain_out  # 徐々にエコーを小さくする
    return segment

def text_to_speech(text, language='ja'):
    tts = gTTS(text=text, lang=language)
    file_name = "output.mp3"
    tts.save(file_name)

    # 再生速度を変更しながらエコーを追加
    sound = AudioSegment.from_mp3(file_name)
    echo_sound = add_echo(sound)
    output_file_name = "output_with_echo.mp3"
    echo_sound.export(output_file_name, format="mp3")
    
    return output_file_name

def play_audio(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # 再生が終了するまで待機
    pygame.mixer.music.stop()
    pygame.mixer.quit()

if __name__ == "__main__":
    pygame.init()
    print("音声化を開始します")
    while True:
        text = input("=> ")
        if len(text) > 0:
            file_name = text_to_speech(text)
            play_audio(file_name)
        time.sleep(1)
