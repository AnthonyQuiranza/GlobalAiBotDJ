import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="4c78ecdefac744f89d5999936cd7db20", region="brazilsouth")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# Set either the `SpeechSynthesisVoiceName` or `SpeechSynthesisLanguage`.
speech_config.speech_synthesis_language = "es-CO" 
speech_config.speech_synthesis_voice_name ="es-CO-GonzaloNeural"
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

def textToVoice(text):
    synthesizer.speak_text_async(text)


