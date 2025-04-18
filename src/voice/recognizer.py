import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self, recognizer_backend="google", debug=False):
        self.recognizer = sr.Recognizer()
        self.backend = recognizer_backend
        self.debug = debug

    def listen_for_move(self):
        with sr.Microphone() as source:
            print("🎙️ Say your move (e.g., 'e2 to e4'):")
            audio = self.recognizer.listen(source)

        try:
            raw_text = self.recognizer.recognize_google(audio)
            if self.debug:
                print(f"[DEBUG] Raw speech: {raw_text}")

            cleaned_move = self._process_text(raw_text)
            print(f"🧠 Interpreted move: {cleaned_move}")
            return cleaned_move

        except sr.UnknownValueError:
            print("❌ Could not understand audio. Try again.")
            return None
        except sr.RequestError as e:
            print(f"⚠️ Could not request results: {e}")
            return None

    def _process_text(self, text):
        """
        Clean and format speech input into UCI-like format.
        For now it's a basic heuristic.
        """
        text = text.lower().replace(" to ", "").replace("free", "3").replace(" ", "")
        return text
