from elevenlabs import ElevenLabs
import elevenlabs
from elevenlabs import play
        #from dotenv import load_dotenv
import os

       # load_dotenv() # Load variables from .env file
client = ElevenLabs(api_key="key")


#voice_id = 

class tune:
	def __init__(self, n):
		tune.stability = 0.0 + n/5
		tune.speed = 0.7 + n/10
		tune.style = 0.0 + n/5	
	

def read(line, voice):
	audio = client.text_to_speech.convert( text=line, voice_id = voice.voice_id ,voice_settings = voice.settings)
	play(audio)	

	
n = 5


tune_voice = tune(n)

voice = elevenlabs.Voice(voice_id = "21m00Tcm4TlvDq8ikWAM" , settings = elevenlabs.VoiceSettings( stability = tune_voice.stability , speed = tune_voice.speed , style = tune_voice.style)) 

