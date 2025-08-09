        from elevenlabs.client import ElevenLabs
        #from dotenv import load_dotenv
        import os

        load_dotenv() # Load variables from .env file
        client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

        audio = client.generate(
            text="This is an example of text-to-speech using ElevenLabs.",
            voice="Rachel" # Or a Voice object: voice=Voice(voice_id="VOICE_ID", settings=VoiceSettings(...))
        )

        from elevenlabs import play
        play(audio)
