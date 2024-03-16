print("_______robo speaker_______")

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    str=input("enter what you want to speak:")
    if str == 'q':
        speaker.Speak("bye bye")
        break    
    speaker.Speak(str)