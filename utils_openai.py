import openai

# API OPENAI
def retorna_resposta_modelo(mensagens,
                            openai_key,
                            modelo='gpt-4o',
                            temperatura=0,
                            stream=True):
    openai.api_key = openai_key
    response = openai.ChatCompletion.create(
        model=modelo,
        messages=mensagens,
        temperature=temperatura,
        stream=stream
    )
    return response