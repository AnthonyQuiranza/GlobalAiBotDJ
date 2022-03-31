from cgitb import text
from http import client
import os
import time

from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.runtime import QnAMakerRuntimeClient
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import QnADTO, MetadataDTO, CreateKbDTO, OperationStateType, UpdateKbOperationDTO, UpdateKbOperationDTOAdd, EndpointKeysDTO, QnADTOContext, PromptDTO
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QueryDTO
from msrest.authentication import CognitiveServicesCredentials

from answer import *
from party import listenMusic
from speechToText import voiceToText
from textToSpeech import textToVoice

#------------------------- ENDPOINT ------------------
subscription_key = '0c4434df35f540d9b36f282648a9032a'
authoring_endpoint = 'https://globalaibot2022.cognitiveservices.azure.com/'
runtime_endpoint = 'https://globalaibot2022.azurewebsites.net'
client = QnAMakerClient(endpoint=authoring_endpoint, credentials=CognitiveServicesCredentials(subscription_key))
kb_id= "26876a40-0149-47b2-9a0e-a2d6b64c7dd2"
runtime_key= "0c8fb782-4831-4a38-8edb-e4777dae00a3"
runtimeClient = QnAMakerRuntimeClient(runtime_endpoint=runtime_endpoint, credentials=CognitiveServicesCredentials(subscription_key))
exit = False
#------------------------- ENDPOINT ------------------
textToVoice("Hola! Bienvenido al bot DJ, ¡Empecémos con la fiesta!")
print("Hola! Bienvenido al bot DJ, ¡Empecémos con la fiesta!")
textToVoice("Elige 1 para interactuar por texto o 2 para interactuar por voz, para salir escribe SALIR")
print("Elige 1 para interactuar por texto o 2 para interactuar por voz, para salir escribe SALIR")
while exit == False:
    option = input("¿Cuál es tu elección?")
    if (option=="1"):
        textToVoice("¿Tienes algo que decirme?")
        print("¿Tienes algo para decirme?")
        question = input("")
        answer,id = generate_answer(runtimeClient,kb_id,runtime_key,question)
        textToVoice(answer)
        print(answer)
        if id =="89":
            textToVoice("¿Qué canción quieres escuchar?")
            song = input("¿Qué canción quieres escuchar?")
            listenMusic(song)
    elif (option =="2"):
        textToVoice("¿Tienes algo que decirme?")
        question = voiceToText()
        answer,id = generate_answer(runtimeClient,kb_id,runtime_key,question)
        textToVoice(answer)
        print(answer)
        if id =="89":
            textToVoice("¿Qué canción quieres escuchar?")
            song = voiceToText()
            listenMusic(song)
    else:
        exit = True
        


question = input("¿Qué tienes para decirle al bot?")
#getEndpointKeys_kb(client)
answer = generate_answer(runtimeClient,kb_id,runtime_key,question)
print(answer)
textToVoice(answer)