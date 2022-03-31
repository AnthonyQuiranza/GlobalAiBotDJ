
from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.runtime import QnAMakerRuntimeClient
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import QnADTO, MetadataDTO, CreateKbDTO, OperationStateType, UpdateKbOperationDTO, UpdateKbOperationDTOAdd, EndpointKeysDTO, QnADTOContext, PromptDTO
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QueryDTO
from msrest.authentication import CognitiveServicesCredentials

def generate_answer(client, kb_id, runtimeKey,question):
    print ("Conectando con el bot...")

    authHeaderValue = "EndpointKey " + runtimeKey

    listSearchResults = client.runtime.generate_answer(kb_id, QueryDTO(question = question), dict(Authorization=authHeaderValue))

    for i in listSearchResults.answers:
        print (f"ID de respuesta: {i.id}")
        """ print(f"Answer ID: {i.id}.")
        print(f"Answer: {i.answer}.")
        print(f"Answer score: {i.score}.")  """
        answer = i.answer
        id = str(i.id)
    return answer, id


def getEndpointKeys_kb(client):
    print("Getting runtime endpoint keys...")
    keys = client.endpoint_keys.get_keys()
    print("Primary runtime endpoint key: {}.".format(keys.primary_endpoint_key))

    return keys.primary_endpoint_key