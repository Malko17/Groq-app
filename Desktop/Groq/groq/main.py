

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
import os
# import chainlit as cl


# import os
# from groq import Groq

# client = Groq(
#     # This is the default and can be omitted
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of low latency LLMs",
#         }
#     ],
#     model="llama3-8b-8192",
# )
# print(chat_completion.choices[0].message.content)

#-------------------------------------------------------------------------------

# import os
# import asyncio
# from groq import AsyncGroq

# client = AsyncGroq(
#     # This is the default and can be omitted
#     api_key=os.environ.get("GROQ_API_KEY"),
# )


# async def main() -> None:
#     chat_completion = await client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Explain the importance of low latency LLMs",
#             }
#         ],
#         model="llama3-8b-8192",
#     )
#     print(chat_completion.choices[0].message.content)


# asyncio.run(main())
#-----------------------------------------------------------------------------


# @cl.on_chat_start
# async def on_chat_start():
    
#     # Sending an image with the local file path
#     elements = [
#     cl.Image(name="image1", display="inline", path="Groq.png")
#     ]
#     await cl.Message(content="Hello there, I am Groq. How can I help you ?", elements=elements).send()

#     model = ChatGroq(temperature=0,api_key = os.environ.get("GROQ_API_KEY"), model_name="llama3-8b-8192")
#     prompt = ChatPromptTemplate.from_messages(
#         [
#             (
#                 "system",
#                 "You're a very knowledgeable Machine Learning Engineer.",
#             ),
#             ("human", "{question}"),
#         ]
#     )
#     runnable = prompt | model | StrOutputParser()
#     cl.user_session.set("runnable", runnable)

# @cl.on_message
# async def on_message(message: cl.Message):
#     runnable = cl.user_session.get("runnable")  # type: Runnable

#     msg = cl.Message(content="")

#     async for chunk in runnable.astream(
#         {"question": message.content},
#         config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
#     ):
#         await msg.stream_token(chunk)

#     await msg.send()

# chat = ChatGroq(tclee=0, api_key="gsk_0fu5je6EcFcOH94jVZQ1WGdyb3FYDg6CJzCZPeVB7093CXXTCiP", model_name="mixtral-8x7b-32768")
# system = "You are a helpful assistant."
# human = "{text}"
# prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

# chain = prompt | chat
# chain.invoke({"text": "Explain the importance of low latency LLMs."})