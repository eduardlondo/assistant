import speech_recognition as sr
import whisper
import asyncio


recognizer = sr.Recognizer()

async def main():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print(f"Waiting for wake words 'ok bing' or 'ok chat'...")
            while True:
                audio = recognizer.listen(source)
                try:
                    with open("audio.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                    # Use the preloaded small_model
                    model = whisper.load_model("small")
                    result = model.transcribe("audio.wav")
                    phrase = result["text"]
                    print(f"You said: {phrase}")
                except Exception as e:
                    print("Error transcribing audio: {0}".format(e))
                    continue


if __name__ == "__main__":
    asyncio.run(main())