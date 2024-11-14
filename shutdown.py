import speech_recognition as sr
import os

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        voice_text = listener.recognize_google(voice, language="ja-JP")
        print(voice_text)
        sample = ("講義を終了します", "お疲れ様でした", "講義を終了", "抗議を終了")
        if(voice_text in sample):
            os.system("shutdown /m LAPTOP-IFOSDIJA /s /t 1")
except:
    print(f"シャットダウンに失敗しました。")