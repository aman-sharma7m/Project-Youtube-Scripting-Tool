from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import BraveSearch
from bs4 import BeautifulSoup
import requests

brave_api_key = ""

def generate_script(key,query,video_len,creativity):
    
    #template for the title
    title_template=PromptTemplate(
        template='''Please come up with the creative title for the youtube video on {sub}.''',
        input_variables=['sub']
    )
    #template to generate the script 
    script_template=PromptTemplate(
        template='''Create a script for a youtube video based on this title for me. TITLE: {title} of duration:{duration} minutes exact using this search data and expand on this data, if required go deep in details of {duckgo}''',
        input_variables=['title','duration','duckgo']
    )

    llm=OpenAI(model='gpt-3.5-turbo-instruct',temperature=creativity,openai_api_key=key)

    title_chain=LLMChain(llm=llm,prompt=title_template,verbose=True)
    script_chain=LLMChain(llm=llm,prompt=script_template,verbose=True)

    # search=DuckDuckGoSearchRun()
    search=BraveSearch.from_api_key(api_key=brave_api_key, search_kwargs={"count": 3})
    search_result=eval(search.run(query))
    links=[i['link'] for i in search_result]
    content=''
    for i in links:
      page=requests.get(i)
      soup=BeautifulSoup(page.text,'lxml')
      text=soup.get_text()
      content+=text
    # search_result=search.run(query)

    title=title_chain.run(query)
    script=script_chain.run(title=title,duration=video_len,duckgo=content)
    return script,title,content

