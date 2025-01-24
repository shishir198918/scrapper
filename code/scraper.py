from urllib.request import urlopen
from bs4 import BeautifulSoup as BS4,SoupStrainer

url="https://en.wikipedia.org/wiki/Prakash_Shukla"
url2="https://en.wikipedia.org/wiki/Web_scraping"


def connection(url):
    """Return Stringfy HTML"""
    page=urlopen(url) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html_bytes


title_tags_only=SoupStrainer(["h1","h2","h3"]) # only parse title tags 
title_soup=BS4(connection(url),"html.parser",parse_only=title_tags_only)
soup=BS4(connection(url),"html.parser")

def list_of_content(title_soup):
    content=[]
    obj={}
    for title in title_soup.find_all("h2"):        
        if title.next_sibling and title.next_sibling.name !="h2":
            obj[title.text]=[]
            for sub_title in title.next_siblings:
                if sub_title.name=="h3":
                    obj[title.text].append(sub_title.text)
                elif sub_title.name=="h2":
                    
                    break
                else:
                    pass
    
        else:
            content.append(title.text)
    content.append(obj)        
                     
    return content 


def text_content(soup):
    content={}
    
    for title in soup.h1.next_sibilings:
        content[title.text]=""
        if title.name  in ["h1","h2","h3"]:
            break
        if title.name=="img":
            content[title.text]=content[title.text]+title["src"]+title.text
        if title.name in ["p","ul","ol","a"]:
            content[title.text]=content[title.text]+title.get_text()
    return content   
print(text_content(soup))         






                
                






