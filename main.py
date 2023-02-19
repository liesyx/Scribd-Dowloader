
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import N
from tkinter import *
import re

def main():
    connect='https://www.scribd.com/'
    problsub='embeds/'
    crssub="coursevideos/"
    #number in  / /
    url= "https://cdn.std/document/320772811/"
    
    match = re.search(r'/(\d+)/', url)
    if match:
        number = match.group(1)
        print(number)  
    url_end=connect+problsub+number+crssub
    ###########
    response = requests.get(url_end)
    print(response)