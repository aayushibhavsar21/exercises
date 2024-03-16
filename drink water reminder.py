
print("_______reminder to drink water in every 2 hr_______")
from plyer import notification
import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def notified(title,msg):
    notification.notify(
        title=title,
        message=msg,
        app_icon=None,
        timeout=5,
    )
    speaker.Speak(f"hey,drink water")

title="imp notification"
msg="drink water and take rest for some time"

try:
    while True:
        notified(title, msg)
        time.sleep(7200)  # Sleep for 2 hours
except KeyboardInterrupt:
    print("\nScript stopped by user.")
