from plyer import notification  # pip install plyer
import pyttsx3  # pip install pyttsx3
import time

engine = pyttsx3.init()

# Set up the notification
notification_title = "Notification Title"
notification_message = "Drink water"

notification_timeout = 5  # in seconds

# Display the notification
for i in range(3):
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout,
    )

    # engine.say(f"{notification_message}")
    # time.sleep(notification_timeout)

engine.runAndWait()
