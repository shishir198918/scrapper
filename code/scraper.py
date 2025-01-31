from urllib.request import urlopen

from bs4 import BeautifulSoup as BS4,SoupStrainer

from pprint import pprint
import json 

url="https://en.wikipedia.org/wiki/Prakash_Shukla"
url2="https://en.wikipedia.org/wiki/Purulia_arms_drop_case"
url3="https://en.wikipedia.org/wiki/Potato"



def connection(url):
    """Return Stringfy HTML"""
    page=urlopen(url) #return response object
    html_bytes=page.read()
    html=html_bytes.decode("utf-8")
    return html

m_filter=SoupStrainer(["main"])

content=BS4(connection(url),"html.parser",parse_only=m_filter)

content_tags_only=SoupStrainer()
title_tags_only=SoupStrainer(["h1","h2","h3"]) # only parse title tags 
header_tags=SoupStrainer(["head.meta['property']"])
footer_tags=SoupStrainer("script",attrs={"type":"application/ld+json"})

script=BS4(connection(url),"html.parser",parse_only=footer_tags)
title_soup=BS4(connection(url3),"html.parser",parse_only=title_tags_only)
soup=BS4(connection(url3),"html.parser",parse_only=content_tags_only)



def list_tag(tag):
    l=[]
    for sub_tag in tag.find_all(True):
        if sub_tag=='\n':
            continue
        if sub_tag.name in ["style","nav","button","noscript"]:
            continue
        if sub_tag.name in ["img","figure"]:
            l.append(sub_tag.name)
        elif sub_tag.string and sub_tag.name=="div":
            continue    
        elif sub_tag.string:
            l.append(sub_tag.name)
    return list(set(l))

text_tag_list=SoupStrainer(list_tag(content.main))

content_soup=BS4(connection(url),"html.parser",parse_only=text_tag_list)
          



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
                    content.append({title.text:obj[title.text]})                  
                    break
                else:
                    pass
    
        else:
            content.append(title.text)
  
                                  
    return content 

def dates(tag):
    date_dic=json.loads(tag.string)
    date={}
    date["datePublished"]=date_dic["datePublished"]
    date["dateModified"]=date_dic["dateModified"]
    return date

     
          
                






