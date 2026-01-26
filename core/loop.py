from voice.listen import listen
from voice.speak import speak

def run_assistant():
    speak("Hello you bitch. do you want anything?")

    while True:
        command = listen()

        if not command:
            speak("Come again I can not hear you.")
            continue

        if "exit" in command or "quit" in command or "sleep" in command:
            speak("Goodbye, see you later. HA HA")
            break

        # Phase 1 behavior: repeat
        speak(f"You said: {command}")
