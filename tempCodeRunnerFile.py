
from tkinter import *
from tkinter import filedialog, messagebox
import requests
import os
import sys, os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import N
from tkinter import *
import urllib.request
import re


connect='https://www.scribd.com/'
problsub='embeds/'
ect='/content?start_page=1&view_mode=scroll&access_key=key-fFexxf7r1bzEfWu3HKwf'
crssub="coursevideos/"
#number in  / /
url= "https://www.scribd.com/document/320772811/Schiavone-Construction-Co-And-Ronald-A-Schiavone-Individually-v-Time-Inc-Appeal-of-Schiavone-Construction-Company-and-Ronald-A-Schiavone-735-F"


match = re.search(r'/(\d+)/', url)
if match:
    number = match.group(1)
    print(number)  # In ra chuỗi số tương ứng với mỗi URL


url_end=connect+problsub+number+ect

###########
response = requests.get(url_end)
with open('example.html', 'w', encoding='utf-8') as f:
    f.write(response.text)