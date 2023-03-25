import pyttsx3  # pip install pyttsx3

engine = pyttsx3.init()
arr = ["Rahul", "Shail"]
for i in arr:
    print(i)
    engine.say(f"Shoutout to {i}")
engine.runAndWait()
