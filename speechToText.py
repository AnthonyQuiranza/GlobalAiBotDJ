import azure.cognitiveservices.speech as speechsdk
speech_config = speechsdk.SpeechConfig(subscription="4c78ecdefac744f89d5999936cd7db20", region="brazilsouth")
speech_config.speech_recognition_language="es-ES"
def voiceToText():
    
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    recognized = False

    print("Por favor habla...")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    while recognized == False:
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(speech_recognition_result.text)
            recognized = True
            return speech_recognition_result.text
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No se pudo reconocer texto: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Reconocimiento cancelado: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Detalles de error: {}".format(cancellation_details.error_details))

