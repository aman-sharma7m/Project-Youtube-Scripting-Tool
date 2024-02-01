# Project Youtube-Scripting-Tool

## Introduction

In today's digital age, content creation has become more accessible and diverse. YouTube, being one of the most popular platforms for sharing videos, requires creators to come up with engaging and creative content. However, brainstorming ideas and writing scripts can be time-consuming and challenging. That's where AI comes in. In this project, we will explore how to generate a YouTube video script using AI.

## Installation & create environment

Clone the project

```bash
  git clone link_to_copy
```

Go to the project directory

```bash
  cd proj_dir
```

Create the enviroment

```bash
  conda create --prefix ./lang_env
  conda activate {path}/lang_env
  python -m ipykernel install --user --name=lang_env
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```

## Code Explanation

To generate a YouTube video script using AI, we will be using the following key concepts:

OpenAI: OpenAI is an artificial intelligence research laboratory that provides powerful language models capable of generating human-like text.
Prompt Template: A prompt template is a predefined structure that guides the AI model to generate specific types of text. It helps in providing context and input variables for generating the desired output.
LLMChain: LLMChain is a Python library that simplifies the process of interacting with OpenAI's language models. It handles the prompt template, AI model, and generates the desired text.
DuckDuckGoSearchRun: DuckDuckGoSearchRun is a tool that allows us to search for specific information on the web using the DuckDuckGo search engine.
BraveSearch: BraveSearch is a privacy-focused search engine that provides search results without compromising user privacy.
BeautifulSoup: BeautifulSoup is a Python library used for web scraping. It helps in extracting data from HTML and XML files.

### Detailed Explanation:

The code provided consists of the following sections:

Importing the required libraries and setting up the BraveSearch API key.
Defining a function named generate_script that takes in parameters such as the OpenAI API key, query, video length, and creativity level.
Creating prompt templates for the title and script of the YouTube video.
Initializing the OpenAI language model and LLMChain objects.
Using the BraveSearch API to search for relevant information based on the query.
Extracting the text content from the search results using web scraping with BeautifulSoup.
Running the title and script chains to generate the YouTube video title and script.
Returning the generated script, title, and content.

## libraries

```
import streamlit as st
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import BraveSearch
from bs4 import BeautifulSoup
import requests
```

## Conclusion

Generating a YouTube video script using AI can save time and provide creative ideas for content creators. In this article, we explored how to use Python and the OpenAI GPT-3.5 Turbo model to generate YouTube video scripts. By leveraging prompt templates, LLMChain, and web scraping tools like BeautifulSoup, we can create engaging and informative video scripts. Experiment with different queries, video lengths, and creativity levels to generate unique and compelling content for your YouTube channel. Happy scripting!
