# Read configuration file
import json
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

#Open environment file
with open('env.json') as json_file:
    data = json.load(json_file)
    openai_api_key = data['openai_api_key']
    temperature = data['openai_temperature']
    model = data['openai_model']

# A simple langchain skeleton with OpenAI configuration
# This is a simple skeleton for a language chain

with get_openai_callback() as cb:
    llm = OpenAI(openai_api_key = openai_api_key, temperature = temperature )
    result = llm.predict("What would be a good company name for a company that makes colorful socks?")
    print(result)
    print(cb)

with get_openai_callback() as cb:
    chat = ChatOpenAI(openai_api_key = openai_api_key, temperature=temperature)
    result =  chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
    print(result)
    print(cb)
