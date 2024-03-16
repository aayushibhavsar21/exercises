
print("______shoutout to everyone using your system's voice______")
import win32com.client

list=[]
for i in range(5):
    name=input("enter name to give shoutout:")
    list.append(name)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in list: 
    speaker.Speak(f"Shoutout to {name}")
