from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
model = ChatOpenAI(model_name="gpt-3.5-turbo-16k")
messages = [
    SystemMessage(content="Translate the following from English into Hinglish"),
    HumanMessage(content="hi!"),
]
parser = StrOutputParser()
result = parser.invoke(model.invoke(messages))
print(result)
