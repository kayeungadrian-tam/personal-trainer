import sys
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[73].id)
engine.setProperty("rate", 120)


def speak(str):
    engine.say(str)
    engine.runAndWait()


if __name__ == "__main__":
    speak(sys.argv[1])
