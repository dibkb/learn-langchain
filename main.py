from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
system_template = """
Given the {information} about a person I give you. You need to create
1. a short summary
2. two interesting facts about them
"""

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{information}")]
)

model = ChatOpenAI(model_name="gpt-3.5-turbo-16k",temperature=0.0)
parser = StrOutputParser()
chain = prompt_template | model | parser
information = """
William Henry "Bill" Gates III is an American business magnate, software developer, and philanthropist. He co-founded Microsoft Corporation with Paul Allen in 1975, which became the world's largest personal computer software company. Gates is widely recognized for his role in developing and popularizing the Microsoft Windows operating system and the Microsoft Office suite.

Bill Gates was born on October 28, 1955, in Seattle, Washington. He dropped out of Harvard University to pursue his passion for computer programming and co-founded Microsoft with Paul Allen. The company initially developed and sold BASIC interpreters for the Altair 8800 and other microcomputers. In 1980, Microsoft released the first version of MS-DOS, which became the standard operating system for personal computers.

In 1985, Microsoft released the first version of Windows, which quickly gained market share and became the dominant operating system for personal computers. Windows 95, released in 1995, further solidified Microsoft's dominance in the desktop operating system market. The company also released the first version of Office in 1989, which became a widely used productivity suite.

Throughout his career, Bill Gates has been a prominent figure in the technology industry. He has been ranked as the world's richest person multiple times by Forbes magazine. In addition to his business accomplishments, Gates is also known for his philanthropic work. He co-founded the Bill & Melinda Gates Foundation with his wife, Melinda French Gates, in 1994. The foundation focuses on improving health and education outcomes in developing countries, with a particular emphasis on vaccines, sanitation, and education.

Bill Gates stepped down as the chairman of Microsoft's board of directors in 2014 but remains the company's largest individual shareholder. He continues to be involved in various projects and initiatives, including the development of artificial intelligence and the fight against climate change. Gates is also a prolific author, having written several books on technology and business.

In summary, Bill Gates is a visionary business leader and philanthropist who co-founded Microsoft and played a crucial role in the development and popularization of the Windows operating system and the Microsoft Office suite. His contributions to the technology industry have made him one of the most influential figures in the world, and his philanthropic work has had a significant impact on improving health and education outcomes in developing countries.
"""
result = chain.invoke({"information": information})
print(result)