import pyttsx3

class TextToSpeech:
    def __init__(self, voice_lang="english", rate=160, volume=1.0, debug=False):
        self.engine = pyttsx3.init()
        self.debug = debug
        self.set_properties(rate, volume, voice_lang)

    def set_properties(self, rate, volume, voice_lang):
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        voices = self.engine.getProperty('voices')

        # Try to find the voice that matches the desired language
        for voice in voices:
            if voice_lang.lower() in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                if self.debug:
                    print(f"[DEBUG] Voice set to: {voice.name}")
                break

    def speak(self, text):
        if self.debug:
            print(f"[DEBUG] Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
