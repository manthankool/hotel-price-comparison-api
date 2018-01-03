import requests
from bs4 import BeautifulSoup
import re
def jag(city):
    l=list()
    search =city + "hotels tripadvisor"
    results = 1 # valid options 10, 20, 30, 40, 50, and 100
    page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results))
    soup = BeautifulSoup(page.content, "html5lib")
    links = soup.findAll("a")
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            l.append(link.get('href').split("?q=")[1].split("&sa=U")[0])
    return(l[3])


