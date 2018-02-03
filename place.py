import requests
from bs4 import BeautifulSoup
import re

def jag(city):
    search = city +"hotels tripadvisor"
    results=100
    page = requests.get("https://www.google.co.in/search?q={}".format(search))
    soup = BeautifulSoup(page.text, "html.parser")
    all=soup.find("div",{"id":"res"})
    j=all.find("a",{"class":"_Zkb"})
    d=str(j)[99:200]
    d = d.replace("%","").replace("hotels","")
    return(d)
